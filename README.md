# Solar-Power-Prediction-Model

# Solar Power Generation Predictor ☀️

## Overview
This repository contains a machine learning pipeline designed to predict solar power output based on environmental and weather conditions (such as temperature, humidity, and cloud cover). Developed as a 3rd-semester BCA Artificial Intelligence and Data Analytics (AIDA) mini-project, the system evaluates and compares two powerful ensemble learning algorithms to determine the most accurate forecasting model.

## Models Deployed
Built using Python and `scikit-learn`, this project implements:
1. **Random Forest Regressor**: A bagging ensemble method that builds multiple decision trees and averages their predictions to improve accuracy and control overfitting.
2. **Gradient Boosting Decision Tree (GBDT)**: A boosting ensemble method that builds trees sequentially, where each new tree specifically targets and corrects the residual errors of the previous ones.

## Tech Stack
* **Language**: Python 3.x
* **Machine Learning**: `scikit-learn`
* **Data Manipulation**: `pandas`, `numpy`
* **Evaluation Metrics**: R² Score
