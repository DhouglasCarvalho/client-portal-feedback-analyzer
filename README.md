--Streamlit: https://client-app-feedback-analyzer-5hphqpcvnsndkkad4ewfcr.streamlit.app/

# Client Portal Feedback Analyzer

A Streamlit-based product management case study that analyzes customer feedback for a simulated B2B client-facing web platform.

## Overview

This project demonstrates how Python can help Product Managers turn qualitative customer feedback into structured product insights.

The app reads synthetic feedback data from a CSV file, classifies feedback by sentiment and product priority, summarizes patterns by product area, and highlights recommended product actions.

## Case Study Scenario

This project simulates feedback analysis for a B2B client-facing web portal used by client administrators, operations leads, support analysts, and client users.

The dataset reflects realistic enterprise platform themes such as onboarding, access management, reporting, authentication, performance, dashboard usability, mobile experience, audit logs, and navigation.

## Portfolio Note

This project uses synthetic data created for demonstration purposes. It is designed to resemble realistic enterprise platform feedback without using confidential or proprietary data.

## Product Management Use Case

Product teams often receive feedback through support tickets, surveys, interviews, and client conversations. This tool helps organize that feedback into themes so teams can identify patterns, quantify pain points, and prioritize discovery or roadmap improvements.

## Features

- Loads customer feedback from CSV
- Displays raw and analyzed feedback
- Classifies sentiment based on rating
- Assigns product priority based on rating and risk-sensitive feature areas
- Summarizes feedback by feature area
- Summarizes feedback by user segment
- Summarizes feedback by feedback channel
- Highlights high-priority product attention areas
- Generates recommended product actions

## Technologies Used

- Python
- Pandas
- Streamlit

## How to Run Locally

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the app:

```bash
python3 -m streamlit run app.py
```

## Live Demo

Streamlit App: paste-your-streamlit-url-here

## Project Purpose

This project demonstrates beginner Python skills applied to a realistic product management use case: analyzing user feedback and identifying actionable product opportunities.
