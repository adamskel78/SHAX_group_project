# Data Pre-Processing

## Data source

[Kaggle's Cardiovascular Disease Dataset](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset/notebooks)

There are 70,000 patients with 11 features (ID excluded), and one target variable.

Features:
|       Features            |   Type of Feature      |   Type    | Unit  | Mean | Std |
| :-------------------------| --------------------   | ----------|-----  |------|----|
| ID                        | Identification feature | Integer   |       |      |    |
| Age                       | Objective feature      | Integer   |  days | 53  | 6.8 |
| Height                    | Objective feature      | Integer   |  cm   | 164  | 8.2 |
| Weight                    | Objective feature      | Float     |  kg   | 74   | 14.4 |
| Gender                    | Objective feature      | Categorical|1 - Female, 2 - Male| 1.35 | 0.48 |
| Systolic Blood Pressure   | Examination Feature    | Integer   | ap_hi | 128.8 | 154 | 
| Diastolic Blood Pressure  | Examination Feature    | Integer   | ap_lo | 96.6 | 188.5 |
| Cholesterol               | Examination Feature    | Categorical |1 - Normal, 2 - Above normal, 3 - Well Above Normal| 1.37 | 0.68|
| Glucose                   | Examination Feature    | Categorical |1 - Normal, 2 - Above Normal, 3 - Well Above Normal| 1.37 | 0.57 |
| Smoking                   | Subjective Feature     | Binary |0 - Does Not smoke, 1 - Smokes| 0.09 | 0.28 |
| Alcohol intake            | Subjective Feature     | Binary |0 - Does Not Drink Alcohol, 1 - Drinks| 0.05 | 0.23 |
| Physical activity         | Subjective Feature     | Binary |0 - Does Not Exercise, 1 - Exercises| 0.8 | 0.4|
| Presence or Absence of Cardiovascular Disease | Target Variable | Binary |0 - Absence of Cardiovascular Disease, 1 - Presence of Cardiovascular Disease| 0.499 | 0.50 |


## Data Description and Data Cleaning

We summarized variable statistics. There is not zero variance variables.
We use df.isnull to check if there is any null values in this dataset and found there is no null values.
We found there were 24 duplicate values, so we removed all duplicated rows. 
In the end we have 11 features and 69,976 patients records.

We split our training and testing sets into 25 and 75 respectively. 
We also scaled X_train and X_test since the features have huge differences in their scales.
The following chart shows the scales of the features.

![Hist_Features](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/His_feature.png)

## Exploratory Data Analysis (EDA)
We provide visualization and Statistics about each variable.
We visualize the relationship between variables.

1. Age and CVD

![Cardio Across Ages](https://github.com/adamskel78/SHAX_group_project/blob/shannon/Data_Visuals/Card_Across_Ages.png)

- Findings

  - In the bar graph, orange bars indicate presence of CVD and blue bars indicate absence of CVD.
  - We found when age is higher, the percentage of people who have CVD is higher.
  - In this dataset, people older than 55 are more at risk of having CVD.

2.  Cholesterol and CVD

![Cardio and Cholesterol](https://github.com/adamskel78/SHAX_group_project/blob/Xiao_Meng/Data_Visuals/Choles_Cardio.png)

- Findings

  - The higher the cholesterol level, the larger the percentage of people who have CVD.

3. Systolic Blood Pressure (ap_hi)

4. Diastolic Blood Pressure (ap_lo)

## Variable Reduction

### Feature Selection
There are 11 features (age, height, weight, gender, systolic blood pressure, diastolic blood pressure, cholesterol, glucose, smoking, alcohol intake, physical activity). 
From EDA, we found some of the features do not show strong correlations to the target variable, presence or absence of cardiovascular disease.
Thus, we used the information from correlation matrix and Recursive Feature Elimination to determine which features to include in our machine learning model.

#### Correlation Matrix
![Correlation Heat Map]()
The last column on both axes is our target variable, cardio. 
Correlation matrix shows that age (r = 0.24), weight (r = 0.18), ap_hi (0.054), ap_lo (0.066), cholesterol (r = 0.22), and glucose (r = 0.089) are correlated with carido. 
Thus, we considered these features for our machine learning models.

#### Recursive Feature Elimination (RFE)
"Recursive feature elimination (RFE) is a feature selection method that fits a model and removes the weakest feature (or features) until the specified number of features is reached." 
We choose six features out of eleven based on correlation matrix. 
In RFE, we used it on RandonForestClassifier(). RFE suggests inmportant indicators of cardiovascular disease are: age, height, weight, ap_hi, ap_lo and cholesterol. This also matches the findings from correlation matrix.



# Machine Learning Models

We performed six machine learning models: Logistic Regression, Decision Tree, Random Forest, KNN, Gradient Boosting Tree and SVM models.
We orignally trained neural network model and got 0.734 testing accuracy. But for depoy purpose, we do not use this model in our app.
We conducted 10-StratifiedKFold crossvalidation and use neg_log_loss to evaluate model performence.
We tuned parameters for the six models to evaluate them and reduce the risk of overfitting problem.

## Logistic Model
 - We trained Logistic Model using ‘lbfgs’ solver and max_iter equals 200. 
 - Logistic regression model accuracy is 0.719.

## Decision Tree
 - We tuned max_depth and max_features to evaluate Decision Tree model. 
 - max_depth=4 and max_features=5 are chosen.
 - Accuracy (training): 0.733
 - Accuracy (testing): 0.731

## Random Forest
 - We tuned n_estimators and max_depth to evaluate Randon Forest model.
 - n_estimators=200 and max_depth=8 are chosen.
 - Accuracy (training): 0.754
 - Accuracy (testing): 0.733 

## Gradient Boosting Tree
 - We tuned max_depth and learning_rate to evaluate Gradient Boosting Tree.
 - max_depth=5 and learning_rate=0.05 are chosen.
 - Accuracy (training): 0.739
 - Accuracy (validation): 0.734

## KNN
 - We tuned n_neighbors for KNN model.
 - n_neighbors=50 is chosen.
 - Accuracy (training): 0.698
 - Accuracy (testing): 0.684

## SVM
 - We tuned the values of C and gamma for SVM model.
 - Accuracy (training): 0.716
 - Accuracy (testing): 0.715

## Model Evaluation
Among all six models, the tree models' performence are better than other models.
We choose Gradient Boosting Tree which got highest testing accuracy (0.734) among six models. 


- The following table shows model performence and comparisons of limitations and benefits.

| Machine Learning Model   | Accuracy | Benefits | limitations |
| :------------------------| ---------| ---------| :-----------|
| Logistic Regression      | 71.9%    | Easy to implement. Tuning of hyperparameters not needed.| Lack flexibility. Might suffer from model mis-specification.|
| Decision Tree            | Training:73.3%; Testing: 72.9%  | Easy to interpret.| Prone to overfitting. |
| Random Forest            | Training:73.1%; Testing: 73.2%  | Reduce the risk of overfitting and hgher accuracy than Decision Tree model.| Computation relatively expensive.|
| Gradient Boosting Tree   | Training:73.6%; Testing: 73.4%  | Good model performence. Less prone to overfitting.| Hard to tune as there are too many hyperparameters. |
| KNN                      | Training:69.8%; Testing: 68.4%  | Easy to implement. No assumption about data.| Curse of dimensionality  |
| SVM                      | Training:71.6%; Testing: 71.5%  | Computation faster. | Poor performence.|



- The following graphs show the performence of Gradient Boosting Tree model.

![cm](https://github.com/adamskel78/SHAX_group_project/blob/Xiao_Meng/Data_Visuals/confusion_matrix.png)

![learning rate](https://github.com/adamskel78/SHAX_group_project/blob/Xiao_Meng/Data_Visuals/learning_rate_only.png) 

![parameter tune](https://github.com/adamskel78/SHAX_group_project/blob/Xiao_Meng/Data_Visuals/max_depth_vs_learning_rate.png) 

![learning curve](https://github.com/adamskel78/SHAX_group_project/blob/Xiao_Meng/Data_Visuals/learning_curve.png)
