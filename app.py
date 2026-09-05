import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('churn_predict_model.pkl','rb'))
st.title('Customer Churn Predictor')

Days_since_last_purchase = st.number_input('last_purchase_since_days')
satisfaction_score = st.selectbox('satisfaction_score',[1,2,3,4,5])
complaint_count = st.number_input('complaint_count')
return_count = st.number_input('return_count')
purchase_frequency = st.selectbox('purchase_frequency',['Rarely','Daily','Quarterly','Monthly','Weekly'])
employment_type = st.selectbox('employment_type',['Self-Employed','Employed','Unemployed','Retired','Student'])
shopping_channel = st.selectbox('shopping_channel',['Online','Mobile App','In-Store','Marketplace'])

purchase_frequency_map = {'Daily': 0, 'Monthly':1, 'Quarterly':2, 'Rarely':3, 'Weekly':4}
employment_type_map = {'Employed': 0, 'Retired':1, 'Self-Employed':2, 'Student':3, 'Unemployed':4}
shopping_channel_map = {'In-Store': 0, 'Marketplace':1, 'Mobile App':2, 'Online':3}

purchase_frequency_value = purchase_frequency_map[purchase_frequency]
employment_type_value = employment_type_map[employment_type]
shopping_channel_value = shopping_channel_map[shopping_channel]

churn_map = {
    0:'No',
    1:'Yes'
}

if st.button('predict_churn'):
    input_data=np.array([[Days_since_last_purchase,satisfaction_score,complaint_count,return_count,purchase_frequency_value,employment_type_value,shopping_channel_value]])
    prediction = model.predict(input_data)
    predict=churn_map[prediction[0]]
    st.success(predict)