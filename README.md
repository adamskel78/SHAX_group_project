# Cardiovascular Disease Checker Project
"Cardiovascular disease (CVD) is a class of disease that involves the heart or blood vessels." "It is the leading cause of death in all areas of the world expect Africa. Together CVD resulted in 17.9 million deaths in 2015, up from 12.3 million in 1990", but yet it is estimated that up to 90% of CVD may be preventable."

Knowing this our group became interested in predicting whether a person is at risk of cardiovascular disease based of individual demographic and health status data (age, height, weight, systolic blood pressure, diastolic blood pressure, cholesterol levels, glucose levels, etc). We want to present this through a web application where users interact with the app by inputing their personal data, and the app responds with the probability of having cardiovascular disease. If time permits, we want to reccommend users course of action such as healthy eating, exercise, limiting alcohol intake based off of the prediction of probability of getting cardiovascular disease.

**Disclaimer**: This is not an official recommendation of what patients should do. Please call a medical professional if you are at risk of cardiovascular disease.

## Data
[Kaggle's Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset/notebooks)

"There are 3 types of input features:

Objective: factual information;
Examination: results of medical examination;
Subjective: information given by the patient.

Features:
- Age (Objective Feature, age, int (days))
- Height (Objective Feature, height int (cm))
- Weight (Objective Feature, weight, float (kg)) 
- Gender (Objective Feature, gender, categorical code)
- Systolic blood pressure (Examination Feature, ap_hi int)
- Diastolic blood pressure (Examination Feature, ap_lo int)
- Cholesterol (Examination Feature, cholesterol, 1: normal, 2: above normal, 3: well above normal)
- Glucose (Examination Feature, gluc, 1: normal, 2: above normal, 3: well above normal)
- Smoking (Subjective Feature, smoke, binary)
- Alcohol intake (Subjective Feature, alco, binary)
- Physical activity (Subjective Feature, active, binary)
- Presence or absence of cardiovascular disease (Target Variable, cardio, binary)

There are 70,000 records of patients data."

## Questions Hope to Answer with this data
We want to answer what health factors are correlated with Cardiovascular Disease and make predition of the probability of getting Cardiovascular Disease given new inputs.

## EDA
We conducted exploratory data analysis (EDA) to this dataset to analyze main characteristics and provide information for the formal modeling task.

To do..
- Need some charts here.


## Technology
[Technology Used](https://github.com/adamskel78/SHAX_group_project/blob/shannon/technology.md)

### Model Selection

We performed the following machine learning models:

- Logistic Model
    - Decision Tree Model
    - Random Forest Model
    - Gradient Boosting Model

We choose Random Forest Model as our predicting model based on the comparisons of model training and validating accuracy.

### Tools
- Postgres for creating a database
- pgAdmin4 for working with the data imported
- QuickDBD for Entity Relationship Diagrams(ERD)
- JavaScript library: D3.js
- VS Code
- Google Chrome
- Plotly.js
- Python Libraries: 
    - numpy
    - pandas
    - sklearn
    - matplotlib
    - seaborn

### Resources
- HTML Styles
    - Bootstrap stylesheet
        - Bootstrap Jumbotron component
- Images

## Results

We tuned the parameters of Random Forest Model and get training accuracy 0.73 and validationg accuracy 0.729. 

## Communication Protocol
- Medium of communication for updates: Slack
- Video calls for group meetings to discuss roles/responsiblities, timelines, discuss conflicts: Zoom or Google Hangout
- Meeting Days: Tuesday, Thursday, and Saturday or Sunday
- Attending office hours to get help from instructor and TAs.

## Group Members:
- Adam Skelton
- Xiao Meng
- Shannon Dang
- Steve Manz
