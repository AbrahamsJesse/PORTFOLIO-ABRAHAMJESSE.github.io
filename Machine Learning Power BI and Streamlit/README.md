
              -* Machine Learning, Power BI, Streamlit*-

# Machine Learning Project: Predicting Victories in League of Legends

## Introduction:
This project utilizes various machine learning models to predict the outcome of ranked games in
League of Legends based on the first 10 minutes of gameplay data. The dataset contains approximately
9,000 ranked games from a high division of League of Legends, with 38 in-game parameters collected 
after 10 minutes of gameplay. The target variable, blueWins, indicates victory (1) or defeat (0) 
for the blue team.

## Project Overview:

1. Data Exploration:

Explored the dataset containing almost 10,000 rows and 40 columns.
Checked data types, unique values, null values, balance of data, and duplicates.
Displayed boxplot and histogram to understand the distribution of features.
Checked values range, variance, and correlation between features and target.

2. Data Cleaning:
No cleaning required as there were no duplicates, unnecessary columns, or null values.
  
3. Model Training and Evaluation:
     
Trained a Random Forest model with an accuracy of 70%.
Pickled the Random Forest model for future use in Streamlit.
Explored other models including Random Forest with robust scaler, Grid Search, Random Search, AdaBoost,
Gradient Boost, Extreme Gradient Boost, Stacking, Support Vector Machine, Cross Validation, and Neural Network.
Evaluated each model's accuracy and performance.

4. Deployment:

Picked the best-performing model and transferred it to a website created with Streamlit.
Incorporated Power BI for simple visualizations of the dataset on the Streamlit website.

Files and Structure:
-  Dataset: high_diamond_ranked_10min.csv
-  Model Pickle: Model.pkl
-  Streamlit Website: app.py
-  Power BI Visualizations: power_bi_visualizations.pbix

## Conclusion:

This machine learning project successfully predicts the outcomes of League of Legends games based 
on early-game data. By exploring various models and techniques, valuable insights were gained into
the predictive capabilities of different algorithms. The deployment of the best-performing model on a
Streamlit website provides an interactive platform for users to explore and utilize the prediction model.
