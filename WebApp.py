#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import pickle
##pickle.dump(log_model,open('log_model.pkl','wb'))
#pickle.dump(dec_model,open('dec_model.pkl','wb'))


log_model = pickle.load(open('log_model.pkl','rb'))
dec_model = pickle.load(open('dec_model.pkl','rb'))

def classify(num):
    if num<0.5:
        return'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'virginica'

def main():
    st.title('Classify Species')
    html_temp = """
    <div style = "background-color:grey ;padding:10px">
    <h2 style = "color:white;text-align:center;"> Iris Classification</h2>
    </div>
    """
#Interface
st.markdown('## Iris Species Prediction')
sidebar = st.sidebar
activities = ['Logistic Regression','Decision Tree']
option= sidebar.selectbox("Which Model you want to use",activities)
st.subheader(option)
st.spinner("WELCOME")
sepal_length = st.slider('Select Sepal length (cm)',0.0,10.0)
sepal_width = st.slider('Select Sepal width (cm)',0.0,10.0)
petal_length = st.slider('Select Petal length (cm)',0.0,10.0)
petal_width = st.slider('Select Petal width (cm)',0.0,10.0)
inputs = [[sepal_length,sepal_width,petal_length,petal_width]]

#Predict button
if st.button('Classify Iris Species'):
    if option == 'Linear Regression':
        st.success(classify((log_model.predict(inputs))))
    else:
        st.success(classify((dec_model.predict(inputs))))

if __name__ == '__main__':
    main()




# In[ ]:




