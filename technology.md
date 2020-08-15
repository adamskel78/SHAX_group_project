# Technologies Used
## Data Cleaning and Analysis
We are using Python to analysis our data. The dataset we found from Kaggle is already cleaned, but if we find that it needs farther cleaning, we will be using Pandas. 

## Database Storage
We are using PostgresSQL to store our data, so far we plan to use only one dataset, so we won't be using PostgresSQL to create relationships between differnt tables.

## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup is to predict the severity of their condition if the someone were to catch COVID. We haven't decided how to split the data yet, but our target group is severity and our dependent variables are COVID symptons: fever, tiredness, dry cough, difficulty in breathing, sore throat, none sympton, pain, nasal congestion, runny nose, diarrhea, none experiencing. We're going to use logistic regression.

## Dashboard
We are planning to display our results through a chatbot where the user inputs their symptoms and the chatbot will respond whether the user will have a mild, moderate, sereve, or no case of COVID if they were to get it.We will have other visualizations of the results of our logistic regression as well.