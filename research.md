\# Urban Company Demand Forecasting



\## About this project

This is a 3-month AI/ML internship project for Urban Company (done through Cynaris Solutions). The goal is to build a demand forecasting pipeline that predicts how many bookings will happen per city and per service type over the next 7 days. This is an internal tool meant for staffing/planning decisions, not a customer-facing feature.



\## Problem

Given past booking data (date, city, service type, weather), predict the number of bookings for the next 7 days, for each city + service type combination.



\## Data

The original data pack provided for this project did not match the project brief (it contained unrelated chatbot intent data and medical Q\&A data, not booking data). After confirming this with the project coordinator, a substitute dataset was sourced from Kaggle: the Retail Store Inventory Forecasting Dataset, which has an equivalent structure (date, location, category, weather, demand count). Columns were relabeled to match this project's use case: Store becomes City, Category becomes Service Type, Units Sold becomes Bookings.



\## Approach

A single global LSTM model will be trained, using city and service type as input features, rather than training a separate model per city/service combination. This avoids splitting the data too thin. The model takes recent days of bookings, weather, and calendar features (day of week, holidays) as input, and outputs the next 7 days of predicted bookings. If a plain LSTM does not reach the target accuracy, a seq2seq LSTM (encoder-decoder) architecture will be tried next, based on research showing it performs better for multi-step forecasting.



\## Evaluation

The primary metric is MAPE (Mean Absolute Percentage Error), with a target of 12 percent or lower on a 4-week hold-out set. RMSE and MAE are tracked as secondary metrics.



\## Project structure

data folder: raw and processed data files

notebooks folder: exploratory analysis

src/features folder: feature engineering code

src/models folder: LSTM model training and evaluation code

src/api folder: Flask API serving forecasts

research.md: notes on papers and repos reviewed, and architecture decisions



\## How to run

Setup, training, and API usage instructions will be added here once those parts are built.



\## Status

Currently in Milestone 1: research, architecture design, and project setup.

