# Uber Price Prediction & Ride Analytics System

## Overview

This project is a complete end-to-end Data Analytics and Machine Learning solution based on Uber/Ola-style ride booking data.

The project includes:

* Data Cleaning & Exploratory Data Analysis (EDA)
* Business KPI Analysis
* Interactive Power BI Dashboard
* Feature Engineering
* Machine Learning Model Training
* Desktop GUI Application using Tkinter

The main objective of this project is to predict ride fares based on ride details such as distance, ride timing, wait time, and vehicle type.

# Project Workflow

## Step 1 — Data Cleaning & EDA

File: `Step1_eda.py`

### Tasks Performed

* Loaded raw ride booking dataset
* Performed data walkthrough and inspection
* Handled missing values using business logic
* Created unified cancellation reason column
* Removed unnecessary columns
* Converted data types for optimization
* Created KPIs for ride analysis
* Exported cleaned dataset to MySQL for dashboarding

### Key Business KPIs

* Total Rides
* Completed Rides
* Cancelled Rides
* Driver Not Found Rate
* Incomplete Ride Rate
* Cancellation Rate
* Customer vs Driver Cancellation Analysis

### Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* MySQL
* Matplotlib
* Seaborn

# Step 2 — Power BI Dashboard

File: `Step2_dashboard.pbix`

### Dashboard Features

* Ride performance overview
* Booking status analysis
* Cancellation insights
* Revenue analysis
* Vehicle type analysis
* Payment method analysis
* KPI cards and trend visuals

### Dashboard Purpose

The dashboard helps analyze ride operations and business performance using interactive visualizations.

### Technologies Used

* Power BI
* MySQL

# Step 3 — Feature Engineering

File: `Step3_featureengineering.py`

### Tasks Performed

* Imported cleaned data from MySQL
* Filtered completed rides only
* Extracted hour feature from ride time
* Performed correlation and distribution analysis
* Applied one-hot encoding on vehicle types
* Selected important ML features

### Features Used for Prediction

* Vehicle Type
* Avg VTAT
* Avg CTAT
* Ride Distance
* Hour of Day

### Target Variable

* Booking Value

### Technologies Used

* Pandas
* NumPy
* Seaborn
* Matplotlib

# Step 4 — Machine Learning Model Training

File: `Step4_model.py`

### ML Workflow

* Train-Test Split
* Feature Scaling using StandardScaler
* Multiple Model Evaluation
* Error Metrics Calculation
* Final Model Saving using Joblib

### Models Tested

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* KNN Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

### Evaluation Metrics

* R2 Score
* MAE
* MSE
* RMSE

### Final Deployment Model

Linear Regression was selected for deployment because it produced more stable predictions for unseen and out-of-range ride distances.

### Technologies Used

* Scikit-learn
* XGBoost
* Joblib
* NumPy

# Step 5 — GUI Application

File: `Step5_gui.py`

A desktop application was built using Tkinter to allow users to predict Uber ride prices interactively.

### GUI Features

* User-friendly interface
* Vehicle type selection
* Ride details input
* Real-time fare prediction
* Input validation
* Interactive button hover effects
* Image-based UI design

### Prediction Inputs

* Ride Distance
* Hour of Day
* Avg VTAT
* Avg CTAT
* Vehicle Type

### Output

* Estimated Ride Fare

### Technologies Used

* Tkinter
* ttk Combobox
* Pillow
* Joblib
* Pandas

# Project Architecture

Raw Dataset → Data Cleaning & EDA → MySQL Database → Power BI Dashboard → Feature Engineering → Machine Learning Model → Tkinter GUI Application

# Tech Stack

| Category         | Technologies                  |
| ---------------- | ----------------------------- |
| Programming      | Python                        |
| Data Analysis    | Pandas, NumPy                 |
| Visualization    | Matplotlib, Seaborn, Power BI |
| Database         | MySQL                         |
| Machine Learning | Scikit-learn, XGBoost         |
| Deployment       | Tkinter GUI                   |
| Model Saving     | Joblib                        |

# Machine Learning Insights

* Ride distance showed strong correlation with fare amount.
* Vehicle type significantly impacts ride pricing.
* Peak hour timing affects estimated fare values.
* Tree-based models achieved higher R2 scores.
* Linear Regression provided more stable extrapolation for long-distance predictions.

# Screenshots

## Power BI Dashboard

<img width="887" height="495" alt="dashboard_snapshot_1" src="https://github.com/user-attachments/assets/61380cfd-7cfa-4cf8-b806-15331bd6b054" />

<img width="892" height="496" alt="dashboard_snapshot_2" src="https://github.com/user-attachments/assets/f8171b5c-736c-405c-80c8-b3872deed026" />

## GUI Application

<img width="895" height="695" alt="gui_snapshot" src="https://github.com/user-attachments/assets/a31903d0-aba0-44d0-9da7-1c7a243d7a74" />


# Project Highlights

* End-to-end analytics workflow
* Business-oriented data cleaning
* Power BI dashboard integration
* Multiple ML model comparison
* Desktop application deployment
* Real-world ride analytics use case

# Author

Nakul Singh

Data Analytics & Machine Learning Project
