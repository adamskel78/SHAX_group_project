# Cardiovascular Disease Checker Project
"Cardiovascular disease (CVD) is a class of disease that involves the heart or blood vessels (Wikipedia)." "It is the leading cause of death in all areas of the world expect Africa. Together CVD resulted in 17.9 million deaths in 2015, up from 12.3 million in 1990", but yet it is estimated that up to 90% of CVD may be preventable (Wikipedia)."

Knowing this our group became interested in predicting whether a person is at risk of cardiovascular disease based of individual demographic and health status data (age, height, weight, systolic blood pressure, diastolic blood pressure, cholesterol levels, glucose levels, etc). 

We want to present this through a web application where users interact with the app by inputing their personal data, and the app responds with the probability of having cardiovascular disease. If time permits, we want to reccommend users course of action such as healthy eating, exercise, limiting alcohol intake based off of the prediction of probability of getting cardiovascular disease.

**Disclaimer**: This is not an official recommendation of what patients should do. Please call a medical professional if you are at risk of cardiovascular disease.

# Technology
[Technology Used](https://github.com/adamskel78/SHAX_group_project/blob/shannon/technology.md)

# Communication Protocol
- Medium of communication for updates: Slack
- Video calls for group meetings to discuss roles/responsiblities, timelines, discuss conflicts: Zoom or Google Hangout
- Meeting Days: Tuesday, Thursday, and Saturday or Sunday
- Attending office hours to get help from TAs.

# Question 
- Which machine learning model provides the most accurate prediction for whether a patient has cardiovasular disease?
- What health factors are correlated with having cardiovascular disease?

# Data
[Kaggle's Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset/notebooks)

"There are 3 types of input features:

- Objective: factual information;
- Examination: results of medical examination;
- Subjective: information given by the patient.

Features:
| Features                |   Type of Feature        |   Type    | Unit  |
| :-----------------------| :----------------------: | :-------: |-----: |
| ID                        | Identification feature | Integer   |       |
| Age                       | Objective feature      | Integer   |  days |
| Height                    | Objective feature      | Integer   |  cm   |
| Weight                    | Objective feature      | Float     |  kg   |
| Gender                    | Objective feature      | Categorical|1 - women; 2 - men |
| Systolic blood pressure   | Examination Feature    | Integer   | ap_hi |
| Diastolic blood pressure  | Examination Feature    | Integer   | ap_lo |
| Cholesterol               | Examination Feature    | Categorical | 1 - normal, 2 - above normal, 3 - well above normal |
| Glucose                   | Examination Feature     | Categorical | 1 - normal, 2 - above normal, 3 - well above normal |
| Smoking                   | Subjective Feature     | Binary | 0 - does not smoke, 1 - smoke |
| Alcohol intake            | Subjective Feature     | Binary | 0 - drinks alcohol, 1 - drinks| 
| Physical activity         | Subjective Feature     | Binary | 0 - does not exercise 1 - exercises|
| Presence or absence of cardiovascular disease | Target Variable | Binary | 0 - healthy, 1 - sick \|

There are 70,000 records of patients data."

# Data Pre-Processing
There weren't any null values, so we didn't remove any values. 

We split our training and testing sets into 25 and 75 respectively. Also, when you look at the histograms, there is scaling needed, so we scaled our X_train and X_test.

![Hist_Features](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data%20Visuals/His_feature.png)

# Feature Engineering / Feature Selection
There are 11 features (age, height, weight, gender, systolic blood pressure, diastolic blood pressure, cholesterol, glucose, smoking, alcohol intake, physical activity). 

Some of which aren't correlated to the target variable, presence or absence of cardiovascular disease, thus we used two methods to determine which feature to include in our machine learning model: correlation matrix and recursive feature elimination.

## Correlation Matrix
![Correlation Heat Map](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data%20Visuals/Corr_Matrix_Heat_Map.png)
The last column on both axes is our target variable, cardio. Looking at those columns, we see that age (r = 0.24), weight (r = 0.18), ap_hi (0.054), ap_lo (0.066), cholesterol (r = 0.22), and glucose (r = 0.089) are weakly correlated with carido. Thus, we will consider these features for our machine learning models.

## Recursive Feature Elimination (RFE)
"Recursive feature elimination (RFE) is a feature selection method that fits a model and removes the weakest feature (or features) until the specified number of features is reached." In this case, we are choose six feature. "Features are ranked by the model’s coef_ or feature_importances_ attributes, and by recursively eliminating a small number of features per loop, RFE attempts to eliminate dependencies and collinearity that may exist in the model (Yellowbrick)." 

In RFE, we used it on RandonForestClassifier(), you can see from our Cardiovascular_Disease.ipynb file, there were five features ranked 1 while one ranked 2. We decided to go with those six features: age, height, weight, ap_hi, ap_lo, cholesterol.

# Exploratory Data Analysis (EDA)


# Machine Learning Models
We performed the following machine learning models:
| Machine Learning Model| Accuracy | What it is     | Benefit |Shortcoming |
| :---------------------| ---------| ---------------|----------| ----------: |
| Random Forest         |   73%    |Bagging algorithm that builds multiple decision trees and merges them together to get a more accurate and stable predict using bagging (builds many independent predictors and combines them using averaging techinque).| - Overcome overfitting by averaging. - Less variance, high accuracy even with missing data, scaling unnessecary | - More computational resources, thus more time consuming. - Less intutive with large datasets - Features need to have some predictive power else model won't work|
| Logistic Regression   |   69.8%  |Classification algorithm that classifies binary outcomes by using a sigmoid function to map the predicted values to probabilities.| - Simple to implement - Effective - Feature scaling unnessecary|- Poor performance with irrelevant and high correlate features - High reliance on proper presentation of data  
| Gradient Boosting Classifer|Learning rate: 0.05, 73%|Boosting algorithm in which the predictors are made sequentially.             | Can overfit             |     
| K-Nearest Neighbor    |    71%   |Classification algorithm that assumes that similar points lie close in proximity and groups them according to distance from one another.|- Simpe to understand and implement - Constantly evolving when new data is inputed.| - More computational resources, thus more time consuming. - Scaling is required - Sensitive to outliers and missing values - Does not work well with imbalance data \|   

# Group Members
- Xiao Meng
- Adam Skelton 
- Steve Manz
- Shannon Dang

# Presentation: Sept 10 at 7pm