# Cardiovascular Disease Checker Project
Cardiovascular disease (CVD) is a class of disease that involves the heart or blood vessels. "It is the leading cause of death in all areas of the world expect Africa. "An estimated 17.9 million people died from CVD in 2016, representing 31% of all global deaths[1], but yet it is estimated that up to 90% of some CVD may be preventable[2]."

Knowing this our group became interested in predicting whether a person is at risk of cardiovascular disease based of individual demographic and health status data (age, height, weight, systolic blood pressure, diastolic blood pressure, cholesterol levels, glucose levels, etc). 

We want to present this through a web application where users interact with the app by inputting their personal data, and the app responds with the probability of having cardiovascular disease. If time permits, we want to recommend users course of action such as healthy eating, exercise, limiting alcohol intake based off of the prediction of probability of getting cardiovascular disease.

**Disclaimer**: This is not an official recommendation of what patients should do. Please call a medical professional if you are at risk of cardiovascular disease.

# Technology
[Technology Used](https://github.com/adamskel78/SHAX_group_project/blob/shannon/technology.md)

# Communication Protocol
- Medium of communication for updates: Slack
- Video calls for group meetings to discuss roles/responsiblities, timelines, discuss conflicts: Zoom or Google Hangout
- Meeting Days: Tuesday, Thursday, and Saturday or Sunday
- Attending office hours to get help from TAs.

# Question 
- Can random forest model predict presence of cardiovascular disease with moderate accuracy?
- What health factors are correlated with having cardiovascular disease?

# Data
[Kaggle's Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset/notebooks)

There are 70,000 patients with 11 features (ID excluded), and one target variable.

Features:
| Features                |   Type of Feature        |   Type    | Unit  |
| :----------------| :----------------------: | :-------: |:----- |
| ID                        | Identification feature | Integer   |       |
| Age                       | Objective feature      | Integer   |  days |
| Height                    | Objective feature      | Integer   |  cm   |
| Weight                    | Objective feature      | Float     |  kg   |
| Gender                    | Objective feature      | Categorical|<ul><li>1 - women</li><li>2 - men</ul></li> |
| Systolic blood pressure   | Examination Feature    | Integer   | ap_hi |
| Diastolic blood pressure  | Examination Feature    | Integer   | ap_lo |
| Cholesterol               | Examination Feature    | Categorical |<ul><li>1 - normal</li><li>2 - above normal</li><li>3 - well above normal</li></ul> |
| Glucose                   | Examination Feature     | Categorical |<ul><li>1 - normal</li><li>2 - above normal</li><li>3 - well above normal</ul></li> |
| Smoking                   | Subjective Feature     | Binary |<ul><li>0 - does not smoke</li><li>1 - smokes</li></ul>|
| Alcohol intake            | Subjective Feature     | Binary |<ul><li> 0 - does not drink alcohol</li><li>1 - drinks</li></ul>| 
| Physical activity         | Subjective Feature     | Binary |<ul><li>0 - does not exercise</li><li>1 - exercises</li></ul>|
| Presence or absence of cardiovascular disease | Target Variable | Binary |<ul><li>0 - healthy</li><li>1 - sick</li></ul>

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
| Machine Learning Model| Accuracy  | What it is     | Benefits |Shortcomings |
| :---------------------| ----------| ---------------|----------| :---------- |
| Random Forest         |   73%    |Bagging algorithm that builds multiple decision trees and merges them together to get a more accurate and stable predict using bagging (builds many independent predictors and combines them using averaging techinque).| <ul><li>Overcome overfitting by averaging.</li><li>Less variance, high accuracy even with missing data, scaling unnessecary</li></ul>|<ul><li>Computationally expensive<li><li>Less intutive with large datasets</li><li>Features need to have some predictive power else model won't work</li></ul>|
| Logistic Regression   |   69.8%  |Classification algorithm that classifies binary outcomes by using a sigmoid function to map the predicted values to probabilities.|<ul><li>Simple to implement</li><li>Effective<li>Feature scaling unnessecary</li></ul>|<ul><li>Poor performance with irrelevant and high correlate features</li><li>High reliance on proper presentation of data</li></ul>|
| Gradient Boosting Classifer|Learning rate: 5%, 73%|Boosting algorithm in which the predictors are made sequentially.|<ul><li>Good accuracy score/<li>Data pre-processing not needed</li><li>Handles missing data</li></ul>|<ul><li>Overfitting</li><li>Computationally expensive</li><li>Less interpretable</li></ul>]   
| K-Nearest Neighbor    |    71%   |Classification algorithm that assumes that similar points lie close in proximity and groups them according to distance from one another.|<ul><li>Simpe to understand and implement</li><li>Constantly evolving when new data is inputed</li></ul>|<ul><li>Computationally expensive</li><li>Scaling is required</li><li>Sensitive to outliers and missing values</li><li>Does not work well with imbalance data</li></ul>
[3]

# References
- [1] Center for Disease Control and Prevention. 2020. Heart Disease Facts | Cdc.Gov. [online] Available at: <https://www.cdc.gov/heartdisease/facts.htm> [Accessed 29 Aug 2020].
- [2] McGillJr, Henry C., et al. “Preventing Heart Disease in the 21st Century.” Circulation, 4 Mar. 2008, www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.107.717033.
- [3][Pros and cons of various Machine Learning algorithms bt Shailaja Gupta](https://towardsdatascience.com/pros-and-cons-of-various-classification-ml-algorithms-3b5bfb3c87d6_)

# Group Members
- Xiao Meng
- Adam Skelton 
- Steve Manz
- Shannon Dang

# Presentation: Sept 10 at 7pm