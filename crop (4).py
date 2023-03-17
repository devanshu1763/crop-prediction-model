#!/usr/bin/env python
# coding: utf-8

# In[14]:





# In[19]:


import streamlit as st
import pandas as pd
import numpy as np
import time
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
d=pd.read_csv("C:\\Desktop\\hack\\CRD.csv")
le_label=LabelEncoder()
d['crop_n']=le_label.fit_transform(d['label'])
inputs=d[['N','P','K','temperature','rainfall']]
km=KMeans(n_clusters=22,random_state=0)
m=km.fit(inputs[['N','P','K','temperature','rainfall']])

df = pd.DataFrame({"N":[], "P":[],"K":[],"temp":[],"rain":[]})

choice=st.sidebar.radio("navigation",['home'],index=0)

st.title("crop prediction   model")
st.markdown("""   ## Enter details""")
nitro =st.text_input("enter nitrogen content")

phos=st.text_input("enter phosphorous")

pota =st.text_input("enter your potasium")

temp=st.text_input("enter temperature")
   
rain=st.text_input("enter rainfall")

arr=[]

if st.button(" Submit"):
   
    df=df.append({"N":nitro,"P":phos,"K":pota,"temp":temp,"rain":rain}, ignore_index=True)
    df.to_excel("C:\\Desktop\\hack\\back.xlsx", index = False)
    st.write("records saved ")
    nitro1=int(nitro) 
    phos1=int(phos)
    pota1=int(pota)
    temp1=int(temp)
    rain1=int(rain)
    arr=m.predict([[nitro1,phos1,pota1,temp1,rain1]])   
    if arr[0] == 0:
        st.write("You can grow kidneybeans, pigeonpeas, blackgram, and mothbean")
    elif arr[0] == 1:
        st.write("You can grow coffee, jute, and papaya")
    elif arr[0] == 2:
        st.write("You can grow grapes")
    elif arr[0] == 3:
        st.write("You can grow maize and papaya")
    elif arr[0] == 4:
        st.write("You can grow papaya, mango, and promogranate")
    elif arr[0] == 5:
        st.write("You can grow rice")
    elif arr[0] == 6:
        st.write("You can grow chickpea and papaya")
    elif arr[0] == 7:
        st.write("You can grow watermelon")
    elif arr[0] == 8:
        st.write("You can grow maize and cotton")
    elif arr[0] == 9:
        st.write("You can grow rice and papaya")
    elif arr[0] == 10:
        st.write("You can grow pigeonpeas and papaya")
    elif arr[0] == 11:
        st.write("You can grow rice, coffee, jute, and papaya")
    elif arr[0] == 12:
        st.write("You can grow banana")
    elif arr[0] == 13:
        st.write("You can grow muskmelon")
    elif arr[0] == 14:
        st.write("You can grow mugbeans and mothbeans")
    elif arr[0] == 15:
        st.write("You can grow coconut")
    elif arr[0] == 16:
        st.write("You can grow apple")
    elif arr[0] == 17:
        st.write("You can grow coconut")
    elif arr[0] == 18:
        st.write("You can grow lentill, mugbeans, and mothbean")
    elif arr[0] == 19:
        st.write("You can grow orange")
    elif arr[0] == 20:
        st.write("You can grow maize, lentill, blackgram, mugbeans, and mothbeans")
    elif arr[0] == 21:
        st.write("You can grow kidneybeans, pigeonpeas, and papaya")
    


# In[ ]:




