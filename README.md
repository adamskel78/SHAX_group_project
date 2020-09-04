# Cardiovascular Disease Checker Project
Cardiovascular disease (CVD) is a class of disease that involves the heart or blood vessels. "It is the leading cause of death in all areas of the world expect Africa. "An estimated 17.9 million people died from CVD in 2016, representing 31% of all global deaths[1], but yet it is estimated that up to 90% of some CVD may be preventable[2]."

Knowing this our group became interested in predicting whether a person is at risk of cardiovascular disease based of individual demographic and health status data (age, height, weight, systolic blood pressure, diastolic blood pressure, cholesterol levels, glucose levels, etc). 

We want to present this through a web application where users interact with the app by inputting their personal data, and the app responds with the probability of having cardiovascular disease. If time permits, we want to recommend users course of action such as healthy eating, exercise, limiting alcohol intake based off of the prediction of probability of getting cardiovascular disease.

**Disclaimer**: This is not an official recommendation of what patients should do. Please call a medical professional if you are at risk of cardiovascular disease.

# Presentation
[Presentation](https://drive.google.com/file/d/1I0HCk8ESBiMLfeqSvpk2WW1apKL-Ufx2/view?usp=sharing)
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

- What machine learning model has the highest accuracy of predicting presence of cardiovascular disease, and can it predict presence of cardiovascular disease with moderate accuracy?

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
| Gender                    | Objective feature      | Categorical|<ul><li>1 - Female</li><li>2 - Male</ul></li> |
| Systolic Blood Pressure   | Examination Feature    | Integer   | ap_hi |
| Diastolic Blood Pressure  | Examination Feature    | Integer   | ap_lo |
| Cholesterol               | Examination Feature    | Categorical |<ul><li>1 - Normal</li><li>2 - Above normal</li><li>3 - Well Above Normal</li></ul> |
| Glucose                   | Examination Feature     | Categorical |<ul><li>1 - Normal</li><li>2 - Above Normal</li><li>3 - Well Above Normal</ul></li> |
| Smoking                   | Subjective Feature     | Binary |<ul><li>0 - Does Not smoke</li><li>1 - Smokes</li></ul>|
| Alcohol intake            | Subjective Feature     | Binary |<ul><li> 0 - Does Not Drink Alcohol</li><li>1 - Drinks</li></ul>| 
| Physical activity         | Subjective Feature     | Binary |<ul><li>0 - Does Not Exercise</li><li>1 - Exercises</li></ul>|
| Presence or Absence of Cardiovascular Disease | Target Variable | Binary |<ul><li>0 - Absence of Cardiovascular Disease</li><li>1 - Presence of Cardiovascular Disease</li></ul>

# Data Pre-Processing
There weren't any null values, but there were 24 duplicate values, so we removed those. In the end we have 11 features and 69,976 patients.

We split our training and testing sets into 25 and 75 respectively. Also, when you look at the histograms, there is scaling needed because our data isn't normalized, so we scaled our X_train and X_test.

![Hist_Features](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/His_feature.png)

# Feature Engineering / Feature Selection
There are 11 features (age, height, weight, gender, systolic blood pressure, diastolic blood pressure, cholesterol, glucose, smoking, alcohol intake, physical activity). 


Some of which aren't correlated to the target variable, presence or absence of cardiovascular disease, thus we used two methods to determine which feature to include in our machine learning model: correlation matrix and recursive feature elimination.

## Correlation Matrix
![Correlation Heat Map](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Corr_Matrix_Heat_Map.png)

The last column on both axes is our target variable, cardio. Looking at those columns, we see that age (r = 0.24), weight (r = 0.18), ap_hi (0.054), ap_lo (0.066), cholesterol (r = 0.22), and glucose (r = 0.089) are weakly correlated with carido. Thus, we will consider these features for our machine learning models.

## Recursive Feature Elimination (RFE)
"Recursive feature elimination (RFE) is a feature selection method that fits a model and removes the weakest feature (or features) until the specified number of features is reached." In this case, we are choose six feature. "Features are ranked by the model’s coef_ or feature_importances_ attributes, and by recursively eliminating a small number of features per loop, RFE attempts to eliminate dependencies and collinearity that may exist in the model (Yellowbrick)." 


In RFE, we used it on RandonForestClassifier(), you can see from our Cardiovascular_Disease.ipynb file, there were five features ranked 1 while one ranked 2. Although RFE, suggests the optimal number of features to be 5, we picked 6 because we felt cholestrol, ranked second, was also an important indicator of cardiovascular disease. We decided to go with these six features: age, height, weight, ap_hi, ap_lo, cholesterol.

# Exploratory Data Analysis (EDA)
![Corr_Matrix_Select](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Corr_Matrix_Selected.png)
- This correlation matrix shows our selected features. I'll be doing EDA on those features.

![Sex](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Count_Sex_CVD.png)

- Our data shows more female data than males. This means that our data is skewed towards data from females.

![Cardio Across Ages](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Card_Across_Ages.png)
- Looking at this bar graph, we see that the orange bar indicating presence of CVD starts surpassing the blue bar indicating absence of CVD at age 53, but at age 54 the blue bar surpasses the orange bar. It isn't until age 55 that the orange bar surpasses the blue bar consistently. This indicates that people older than 55 are more at risk of having CVD.

![BMI_Cardio](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/BMI_Cardio.png)
- Patients with abnormal BMI are more at risk of cardiovascular disease than patients with normal or underweight BMI. We can see this by looking at the abnormal category where patients with cardiovascular disease surpasses patients withour cardiovascular disease.

![Blood_Cardio](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Blood_Cardio.png)
- Patients who develop hypertension are more at risk of cardiovascular disease. We can see this by looking at Hypertension (Stage 1) where there is an increasing number of patients who do have cardiovascular disease are in this category and it is farther confirmed when looking at Hypertension (Stage 2) where patients with cardiovascular disease excesses patients withour cardiovascular disease.

![Choles_Cardio](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Choles_Cardio.png)
- Both "Above Normal" and "Well Above Normal" cholesterol levels have more patients who have cardiovascular disease than don't have cardiovascular disease meaning that people with above normal or well above normal cholesterol levels are more at risk of cardiovascular disease.

# Machine Learning Models
We performed the following machine learning models[3]:
| Machine Learning Model| Accuracy  | What it is     | Benefits |Shortcomings |
| :---------------------| ----------| ---------------|----------| :---------- |
| Logistic Regression   |Testing: 71.9%|Classification algorithm that classifies binary outcomes by using a sigmoid function to map the predicted values to probabilities.|<ul><li>Simple to implement</li><li>Effective<li>Feature scaling unnessecary</li></ul>|<ul><li>Poor performance with irrelevant and high correlate features</li><li>High reliance on proper presentation of data</li></ul>|
| K-Nearest Neighbor     |<ul><li>Training: 69.8%</li><li>Testing: 68.4%</li></ul>|Classification algorithm that assumes that similar points lie close in proximity and groups them according to distance from one another.|<ul><li>Simpe to understand and implement</li><li>Constantly evolving when new data is inputed</li></ul>|<ul><li>Computationally expensive</li><li>Scaling is required</li><li>Sensitive to outliers and missing values</li><li>Does not work well with imbalance data</li></ul>
|Decision Tree|<ul><li>Training: 73.3%</li><li>Testing: 72.9%</li></ul>|Supervised algorithm with tree-like structures with its root nod on top; it's mostly used for classification.|<ul><li>Normalization or scaling of data not needed.</li><li>Handling missing values</li><li>Automatic Feature selection : Irrelevant features won’t affect decision trees</li></ul>|<ul><li>Prone to overfitting.</li><li>Sensitive to data. If data changes slightly, the outcomes can change to a very large extent.</li><li>Sensitive to outliers and missing values</li><li>Computationally Expensive</li></ul>|
| Random Forest         | <ul><li>Training: 73%</li><li>Testing: 72.9%</li></ul>|Bagging algorithm that builds multiple decision trees and merges them together to get a more accurate and stable predict using bagging (builds many independent predictors and combines them using averaging techinque).| <ul><li>Overcome overfitting by averaging.</li><li>Less variance, high accuracy even with missing data, scaling unnessecary</li></ul>|<ul><li>Computationally expensive<li><li>Less intutive with large datasets</li><li>Features need to have some predictive power else model won't work</li></ul>|
| Gradient Boosting Classifer|<ul><li>Training: 73.5%</li><li>Testing: 73.4%</li></ul>|Boosting algorithm in which the predictors are made sequentially.|<ul><li>Good accuracy score/<li>Data pre-processing not needed</li><li>Handles missing data</li></ul>|<ul><li>Overfitting</li><li>Computationally expensive</li><li>Less interpretable</li></ul>|


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

