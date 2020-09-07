# Cardiovascular Disease Checker Project
Cardiovascular disease (CVD) is a class of disease that involves the heart or blood vessels. "It is the leading cause of death in all areas of the world expect Africa. "An estimated 17.9 million people died from CVD in 2016, representing 31% of all global deaths[1], but yet it is estimated that up to 90% of some CVD may be preventable[2]."

Knowing this our group became interested in predicting whether a person is at risk of cardiovascular disease based of individual demographic and health status data (age, height, weight, systolic blood pressure, diastolic blood pressure, cholesterol levels, glucose levels, etc). 

We want to present this through a web application where users interact with the app by inputting their personal data, and the app responds with the probability of having cardiovascular disease. If time permits, we want to recommend users course of action such as healthy eating, exercise, limiting alcohol intake based off of the prediction of probability of getting cardiovascular disease.

**Disclaimer**: This is not an official recommendation of what patients should do. Please call a medical professional if you are at risk of cardiovascular disease.

# Presentation
[Presentation](https://drive.google.com/file/d/1I0HCk8ESBiMLfeqSvpk2WW1apKL-Ufx2/view?usp=sharing)

# Web Application
[Web](https://cvdchecker.herokuapp.com/)
[Video](https://www.loom.com/share/76c3b51424e74aac95af93201fbae67d)

# Technology
[Technology Used](https://github.com/adamskel78/SHAX_group_project/blob/shannon/technology.md)

# Communication Protocol
- Medium of communication for updates: Slack
- Video calls for group meetings to discuss roles/responsiblities, timelines, discuss conflicts: Zoom or Google Hangout
- Meeting Days: Tuesday, Thursday, and Saturday or Sunday
- Attending office hours to get help from TAs.

# Outline
- Question
- Description of data
- Pre-process the data
- Exploration of the data
- Feature Engineering
- Create machine learning algorithm
- Create web app to display an interactive predictor of cardiovascular disease

# Question 
- What health factors are correlated with Cardiovascular Disease?
- How to help people prevent Cardiovascular Disease?

# Data
[Kaggle's Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset/notebooks)

There are 70,000 patients with 11 features (ID excluded), and one target variable.

Features:
| Features                |   Type of Feature      |   Type     | Unit  |
| :-----------------------| :--------------------  | :--------  |:----  |
| ID                      | Identification feature | Integer    |       |
| Age                     | Objective feature      | Integer    |  days |
| Height                  | Objective feature      | Integer    |  cm   |
| Weight                  | Objective feature      | Float      |  kg   |
| Gender                  | Objective feature      | Categorical|<ul><li>1 - Female</li><li>2 - Male</ul></li> |
| Systolic Blood Pressure | Examination Feature    | Integer    | ap_hi |
| Diastolic Blood Pressure| Examination Feature    | Integer    | ap_lo |
| Cholesterol             | Examination Feature    | Categorical|<ul><li>1 - Normal</li><li>2 - Above normal</li><li>3 - Well Above Normal</li></ul> |
| Glucose                 | Examination Feature     | Categorical |<ul><li>1 - Normal</li><li>2 - Above Normal</li><li>3 - Well Above Normal</ul></li> |
| Smoking                 | Subjective Feature     | Binary |<ul><li>0 - Does Not smoke</li><li>1 - Smokes</li></ul>|
| Alcohol intake          | Subjective Feature     | Binary |<ul><li> 0 - Does Not Drink Alcohol</li><li>1 - Drinks</li></ul>| 
| Physical activity       | Subjective Feature     | Binary |<ul><li>0 - Does Not Exercise</li><li>1 - Exercises</li></ul>|
| Presence or Absence of Cardiovascular Disease| Target Variable | Binary |<ul><li>0 - Absence of Cardiovascular Disease</li><li>1 - Presence of Cardiovascular Disease</li></ul>

# Data Pre-Processing
There weren't any null values, but there were 24 duplicate values, so we removed those and ended with 11 features and 69,976 patients.

We split our training and testing sets into 25 and 75 respectively and scaled the X_train and X_test due to is abnormal shape seen below.
![Hist_Features](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/His_features.png)

# Feature Engineering / Feature Selection
We used two methods to determine which features to include in our machine learning model: correlation matrix and recursive feature elimination.

## Correlation Matrix
![Correlation Heat Map](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Corr_Matrix_Heat_Map.png)

The last column on both axes is our target variable, cardio. Age (r = 0.24), weight (r = 0.18), ap_hi (0.054), ap_lo (0.066), cholesterol (r = 0.22), and glucose (r = 0.089) are weakly correlated with cardio. Thus, we will consider these features for our machine learning models.

## Recursive Feature Elimination (RFE)
"Recursive feature elimination (RFE) is a feature selection method that fits a model and removes the weakest feature (or features) until the specified number of features is reached." In this case, we are choose six feature. "Features are ranked by the model’s coef_ or feature_importances_ attributes, and by recursively eliminating a small number of features per loop, RFE attempts to eliminate dependencies and collinearity that may exist in the model (Yellowbrick)." 


In RFE, we used it on RandonForestClassifier(), you can see from our Cardiovascular_Disease.ipynb file, there were five features ranked 1 while one ranked 2. Although RFE, suggests the optimal number of features to be 5, we picked 6 because we felt cholestrol, ranked second, was also an important indicator of cardiovascular disease. We decided to go with these six features: age, height, weight, ap_hi, ap_lo, cholesterol.

# Exploratory Data Analysis (EDA)
![Corr_Matrix_Select](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Corr_Matrix_Selected.png)

![Cardio Across Ages](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Card_Across_Ages.png)


# Machine Learning Models
We performed the following machine learning models:
| Machine Learning Model   | Accuracy                        | Benefits                                                                   | limitations                                                     |
| :------------------------| --------------------------------| ---------------------------------------------------------------------------| :---------------------------------------------------------------|
| Logistic Regression      | 71.9%                           | Easy to implement. Tuning of hyperparameters not needed.                   | Lack flexibility. Might suffer from model mis-specification.    |
| Decision Tree            | Training:73.3%; Testing: 72.9%  | Easy to interpret.                                                         | Prone to overfitting.                                           |
| Random Forest            | Training:73.1%; Testing: 73.2%  | Reduce the risk of overfitting and hgher accuracy than Decision Tree model.| Computation relatively expensive.                               |
| Gradient Boosting Tree   | Training:73.6%; Testing: 73.4%  | Good model performence. Less prone to overfitting.                         | Hard to tune as there are too many hyperparameters              |
| KNN                      | Training:69.8%; Testing: 68.4%  | Easy to implement. No assumption about data.                               | Curse of dimensionality                                         |
| SVM                      | Training:71.6%; Testing: 71.5%  | Computation faster.                                                        | Poor performence.                                              |


# Database
![ERD](https://github.com/adamskel78/SHAX_group_project/blob/shannon/ERD_SHAX_Project.png)

# References
- [1] Center for Disease Control and Prevention. 2020. Heart Disease Facts | Cdc.Gov. [online] Available at: <https://www.cdc.gov/heartdisease/facts.htm> [Accessed 29 Aug 2020].
- [2] McGillJr, Henry C., et al. “Preventing Heart Disease in the 21st Century.” Circulation, 4 Mar. 2008, www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.107.717033.
- [3][Shailaja Gupta, "Pros and cons of various Machine Learning algorithms" ](https://towardsdatascience.com/pros-and-cons-of-various-classification-ml-algorithms-3b5bfb3c87d6_)

# Group Members
- Xiao Meng
- Adam Skelton 
- Steve Manz
- Shannon Dang

# Presentation: Sept 10 at 7pm

