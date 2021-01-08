# Heart-Failure-Prediction

Data is taken from Kaggle : https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide.
Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

## Feature Details : 
Following are the feature used for predicting heart fail
Age : Age of the Person
Aneamia : Decrease of red blood cells or hemoglobin\
Creatinine Phosphokinase : Level of the CPK enzyme in the blood (mcg/L) Normal Range : 10 to 120 micrograms per liter (mcg/L) \
Diabetes : If a person has diabetes \
Ejection Fraction : Percentage of blood leaving the heart at each contraction (%)\
Platelets : Platelets in the blood (kiloplatelets/mL) Normal Range : 150,000 to 450,000 platelets per microliter of blood\
High Blood Pressure : If the patient has hypertension \
Serum Creatinine : Level of serum creatinine in the blood (mg/dL) Normal Range : 0.84 to 1.21 milligrams per deciliter \
Serum Sodium : Level of serum sodium in the blood (mEq/L) Normal Range : 135 and 145 milliequivalents per liter \
Time : Follow-up period (days)

## Algirithm Used for Prediction
Following are the algorithms used for predicting heart fail along with their accuracy
|Sl.No.|       lgorithm      |Accuracy (%)|
|:----:|:-------------------:|:----------:|
|1.    | Logistic Regression | 85%        |
|2.    | SVM   | 73.33        |
|3.    | KNN   | 66.67        |
|4.    | Naive Bayes   | 83.33        |
|5.    | Decision Tree   | 88.33        |
|6.    | Ada Boost   | 88.33        |
|7.    | XG Boost   | 93.33        |
|8.    | Random Forest   | 91.67        |

From the above table, it is evidend that the best classifier for this problem is either **XGBoost or Random Forest**. So for the app building, *Random Forest* is considered for predicting Heart Failure.

## Deployment :
I have used **Streamlit** library and **Heroku** platform to build the app.
App URL : 
