import streamlit as st
import plotly.express as px
import pandas as pd
import os
path3=os.getcwd() + "\data\stations.txt"
ds=pd.read_csv(path3,skiprows=17)
ds=ds[['STAID','STANAME                                 ']]
ds=ds.head(10)

def get_filename(place):
    file=str(ds[ds['STANAME                                 ']==place]['STAID'].squeeze())
    return file


st.title("Weather forecast for the next days")
#place=st.text_input("Place: ")
place=st.selectbox("Select station to view ",ds['STANAME                                 '])
file=get_filename(place)

days=st.slider("Forecasted Days",min_value=1,max_value=100,help=" Select the number of forecasted days")
option=st.selectbox("Select data to view ",("temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

path = os.getcwd() + "\data\TG_STAID" + str(file).zfill(6) + ".txt"
#path=os.getcwd()+"\data\TG_STAID000001.txt"
#print(path)
df=pd.read_csv(path,skiprows=20,parse_dates=["    DATE"])
df1=df[(df[' Q_TG'] ==0 ) & (df['   TG'] !=0)] #valid data only
#print(df1.head(100))



#dates=["2023-19-04","2023-20-04","2023-21-04"]
#temp=[10,11,15]

def get_temp(days):
    df2=df1.head(days)
    dates=df2["    DATE"]
    temp=df2['   TG']
    return dates,temp

d,t=get_temp(days)

st.subheader(f"place : {place } file: {file} days : {days}")

figure=px.line(x=d,y=t,labels={"x":"Date","y":"temperature(c)"})
st.plotly_chart(figure)



#run the following commands if signed error , then run streamlit command
#Get-ExecutionPolicy
#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
# streamlit run C:\Users\AjayThota\PycharmProjects\WeatherAPP\main.py
