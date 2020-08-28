# Cardiovascular Disease Checker Project
"Cardiovascular disease (CVD) is a class of disease that involves the heart or blood vessels." "It is the leading cause of death in all areas of the world expect Africa. Together CVD resulted in 17.9 million deaths in 2015, up from 12.3 million in 1990", but yet it is estimated that up to 90% of CVD may be preventable."

Knowing this our group became interested in predicting whether a person is at risk of cardiovascular disease based of individual demographic and health status data (age, height, weight, systolic blood pressure, diastolic blood pressure, cholesterol levels, glucose levels, etc). 

We want to present this through a web application where users interact with the app by inputing their personal data, and the app responds with the probability of having cardiovascular disease. If time permits, we want to reccommend users course of action such as healthy eating, exercise, limiting alcohol intake based off of the prediction of probability of getting cardiovascular disease.

**Disclaimer**: This is not an official recommendation of what patients should do. Please call a medical professional if you are at risk of cardiovascular disease.

# Data
[Kaggle's Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset/notebooks)

"There are 3 types of input features:

Objective: factual information;
Examination: results of medical examination;
Subjective: information given by the patient.

Features:
| Features                  |  Unit                 | Type of Feature        | Type           |
| :-------------------------| :-------------------: | :--------------------: |--------------: |
| ID                        |                       | Identification feature | Integer        |
| Age                       |    days               | Objective feature      | Integer        |
| Height                    |    cm                 | Objective feature      | Integer        |
| Weight                    |    kg                 | Objective feature      | Float          |
| Gender                    | 1 - women, 2 - men    | Objective feature      |  Categorical   |
| Systolic blood pressure   |    ap_hi              | Examination Feature    |  Integer       |
| Diastolic blood pressure  |    ap_lo              | Examination Feature    |  Integer       |
| Cholesterol               | 1 - normal, 2 - above normal, 3 - well above normal | Examination Feature    | Categorical |
| Glucose                   | 1 - normal, 2 - above normal, 3 - well above normal | Examination Feature    | Categorical |
| Smoking                   | 0 - does not smoke, 1 - smoke | Subjective Feature     | Binary |
| Alcohol intake            | 0 - drinks alcohol, 1 - drinks | Subjective Feature     | Binary |
| Physical activity         | 0 - does not exercise 1 - exercises| Subjective Feature     | Binary |
| Presence or absence of cardiovascular disease   | 0 - healthy, 1 - sick | Target Variable | Binary \|

There are 70,000 records of patients data."

# Question 
What health factors are correlated with having cardiovascular disease?

Which machine learning model provides the most accurate prediction for whether a patient has cardiovasular disease?

# Technology
[Technology Used](https://github.com/adamskel78/SHAX_group_project/blob/shannon/technology.md)

# Communication Protocol
- Medium of communication for updates: Slack
- Video calls for group meetings to discuss roles/responsiblities, timelines, discuss conflicts: Zoom or Google Hangout
- Meeting Days: Tuesday, Thursday, and Saturday or Sunday
- Attending office hours to get help from TAs.

# Feature Engineering / Feature Selection
There are 11 features (age, height, weight, gender, systolic blood pressure, cholesterol, glucose, smoking, alcohol intake, physical activity). 

Some of which aren't correlated to the target variable, presence or absence of cardiovascular disease, thus we used the correlation matrix to determine which features do correlate to our target variable.

[Correlation Heat Map]()
The last column on both axes is our target variable, cardio. Looking at those columns, we see that age (r = 0.24), weight (r = 0.18), ap_hi (0.054), ap_lo (0.066), cholesterol (r = 0.22) are weakly correlated with carido. Thus, we will choose these features in our machine learning models.

# Machine Learning Models
We performed the following machine learning models

# Group Members
Xiao Meng
Adam Skelton 
Steve Manz
Shannon Dang

# Presentation: Sept 10 at 7pm