import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Client Portal Feedback Analyzer",
    page_icon="💬",
    layout="wide"
)

st.title("Client Portal Feedback Analyzer")
st.write(
    "A simulated product management case study that analyzes customer feedback "
    "for a B2B client-facing web platform."
)

st.info(
    "Note: This project uses synthetic feedback data created for portfolio demonstration purposes. "
    "It is designed to resemble realistic enterprise platform feedback without using confidential data."
)

feedback = pd.read_csv("data/feedback.csv")

st.subheader("Raw Feedback Dataset")
st.dataframe(feedback, width="stretch")


def classify_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"


def classify_priority(row):
    rating = row["Rating"]
    feature_area = row["Feature_Area"]

    high_risk_areas = [
        "Access Management",
        "Authentication",
        "Performance",
        "Onboarding"
    ]

    if rating <= 2 and feature_area in high_risk_areas:
        return "High"
    elif rating <= 3:
        return "Medium"
    else:
        return "Low"


feedback["Sentiment"] = feedback["Rating"].apply(classify_sentiment)
feedback["Product_Priority"] = feedback.apply(classify_priority, axis=1)

st.subheader("Analyzed Feedback")
st.dataframe(feedback, width="stretch")

st.subheader("Executive Summary")

total_feedback = len(feedback)
average_rating = round(feedback["Rating"].mean(), 2)
negative_count = len(feedback[feedback["Sentiment"] == "Negative"])
high_priority_count = len(feedback[feedback["Product_Priority"] == "High"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Feedback Items", total_feedback)
col2.metric("Average Rating", average_rating)
col3.metric("Negative Feedback", negative_count)
col4.metric("High Priority Items", high_priority_count)

st.subheader("Feedback by Feature Area")

feature_summary = (
    feedback.groupby("Feature_Area")
    .agg(
        Feedback_Count=("Feedback_ID", "count"),
        Average_Rating=("Rating", "mean"),
        Negative_Count=("Sentiment", lambda x: (x == "Negative").sum()),
        High_Priority_Count=("Product_Priority", lambda x: (x == "High").sum())
    )
    .reset_index()
)

feature_summary["Average_Rating"] = feature_summary["Average_Rating"].round(2)

feature_summary = feature_summary.sort_values(
    by=["High_Priority_Count", "Negative_Count", "Feedback_Count"],
    ascending=False
)

st.dataframe(feature_summary, width="stretch")

st.subheader("Feedback by User Segment")

segment_summary = (
    feedback.groupby("User_Segment")
    .agg(
        Feedback_Count=("Feedback_ID", "count"),
        Average_Rating=("Rating", "mean"),
        Negative_Count=("Sentiment", lambda x: (x == "Negative").sum())
    )
    .reset_index()
)

segment_summary["Average_Rating"] = segment_summary["Average_Rating"].round(2)

st.dataframe(segment_summary, width="stretch")

st.subheader("Feedback by Channel")

channel_summary = (
    feedback.groupby("Channel")
    .agg(
        Feedback_Count=("Feedback_ID", "count"),
        Average_Rating=("Rating", "mean")
    )
    .reset_index()
)

channel_summary["Average_Rating"] = channel_summary["Average_Rating"].round(2)

st.dataframe(channel_summary, width="stretch")

st.subheader("High Priority Product Attention Areas")

high_priority_feedback = feedback[feedback["Product_Priority"] == "High"]

if len(high_priority_feedback) > 0:
    st.warning(
        "The following items represent high-priority product attention areas based on low ratings "
        "and risk-sensitive feature areas."
    )

    st.dataframe(
        high_priority_feedback[
            [
                "Feedback_ID",
                "User_Segment",
                "User_Role",
                "Feature_Area",
                "Feedback",
                "Rating",
                "Channel"
            ]
        ],
        width="stretch"
    )
else:
    st.success("No high-priority product attention areas found.")

st.subheader("Recommended Product Actions")

top_areas = feature_summary.head(3)

for _, row in top_areas.iterrows():
    st.write(
        f"- Review **{row['Feature_Area']}**: "
        f"{row['Feedback_Count']} feedback item(s), "
        f"{row['Negative_Count']} negative item(s), "
        f"{row['High_Priority_Count']} high-priority item(s), "
        f"average rating {row['Average_Rating']}."
    )

st.subheader("Case Study Takeaway")

st.write(
    "Based on the synthetic dataset, the strongest product opportunities are areas with repeated "
    "negative feedback, low average ratings, and operational risk. These areas should be reviewed "
    "for discovery, usability testing, and roadmap prioritization."
)
