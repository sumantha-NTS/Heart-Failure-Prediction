import pandas as pd
import pickle
import streamlit as st

pickle_in = open('Classifier.pkl','rb')
model = pickle.load(pickle_in)
#a=[[75,0,582,0,20,1,265000,1.9,130,1,0,4]]

b1, titl, b2 = st.beta_columns([1,5,1])
titl.title('Heart Failure Prediction')

if st.sidebar.checkbox('Parameter Details'):
    st.sidebar.markdown('**Age : ** Age of the Person ')
    st.sidebar.markdown('**Aneamia : ** Decrease of red blood cells or hemoglobin')
    st.sidebar.markdown('**Creatinine Phosphokinase : ** Level of the CPK enzyme in the blood (mcg/L) Normal Range : 10 to 120 micrograms per liter (mcg/L)')
    st.sidebar.markdown('**Diabetes : ** If a person has diabetes')
    st.sidebar.markdown('**Ejection Fraction : ** Percentage of blood leaving the heart at each contraction (%)')
    st.sidebar.markdown('**Platelets : ** Platelets in the blood (kiloplatelets/mL) Normal Range : 150,000 to 450,000 platelets per microliter of blood ')
    st.sidebar.markdown('**High Blood Pressure : ** If the patient has hypertension')
    st.sidebar.markdown('**Serum Creatinine : ** Level of serum creatinine in the blood (mg/dL) Normal Range : 0.84 to 1.21 milligrams per deciliter')
    st.sidebar.markdown('**Serum Sodium : ** Level of serum sodium in the blood (mEq/L) Normal Range : 135 and 145 milliequivalents per liter')
    st.sidebar.markdown('**Time : ** Follow-up period (days)')


st.header('Patient Details')
age = st.number_input('Age',value=25)

gender, smoke = st.beta_columns(2)
gender.selectbox('Gender',('Male','Female'))
smoke.selectbox('Do you Smoke?',('Yes','No'))

anaemia, hbp, diabetes = st.beta_columns(3)
anaemia.selectbox('Do you have Anaemia?',('Yes','No'))
hbp.selectbox('Do you have High Blood Pessure?',('Yes','No'))
diabetes.selectbox('Do you have Diabetes?',('Yes','No'))

eject = st.number_input('Ejection Fraction (%)',value=10)
cp = st.number_input('Creatinine Phosphokinase (mcg/L)',value=10)
platelets = st.number_input('Platelets Count (kiloplatelets/mL)',value=150000.00)

serum_cre = st.text_input('Serum Creatinine value (mg/dL)',value=0.84)
serum_sod = st.number_input('Serum Sodium value (mEq/L)',value=135)
time = st.number_input('Days of follow-up with doctor',value=1)

#def preprocessing():
    #for Anaemia
if(anaemia == 'Yes'):
    ana = 1
else:
    ana = 0
    
if(diabetes == 'Yes'):
    dia = 1
else:
    dia = 0   
    
if(hbp == 'Yes'):
    hb = 1
else:
    hb = 0    
   
if(gender == 'Male'):
    gen = 1
else:
    gen = 0
    
if(smoke == 'Yes'):
    smok = 1
else:
    smok = 0


data = [[age,ana,cp,dia,eject,hb,platelets,serum_cre,serum_sod,gen,smok,time]]
    
    
if st.button('Predict'):

    data1 = pd.DataFrame(data)
    pred = model.predict(data)

   
    if(pred == 1):
        st.success('There is a high probability of Heart Fail')
    else:
        st.success('Your Heart is safe')

if st.button('About'):
    st.write('Created by Sumantha.NTS dated 07/01/2021')
    

