import streamlit as st
import pandas as pd
import requests
import json
from PIL import Image

params = {'access_key': 'a1f76523a100480d892ae4d3bf75ebad'}

st.header("Flight Tracking")
img=Image.open('E://streamlit//flight1.jpg')
st.image(img,width=600)



select=st.sidebar.selectbox("select",["airport","airlines","flight","cities","country"])
if(select=="airport"):
    text=st.sidebar.text_input("Airport name")
    res=st.sidebar.button("OK")
    if(res==True and len(text)!=0):
        api_result = requests.get('http://api.aviationstack.com/v1/airports', params)
        dict_train=api_result.json()
        fram=pd.DataFrame(dict_train['data'])

        store=fram.loc[fram['airport_name'] == text.title()]
        st.write("airport_id =",store["airport_id"].to_string().split()[1])
        st.write("gmt =",store["gmt"].to_string().split()[1])
        st.write("iata_code =",store["iata_code"].to_string().split()[1])
        st.write("airport_name =",store["airport_name"].to_string().split()[1])
        st.write("country_name =",store["country_name"].to_string().split()[1])
        st.write("timezone =",store["timezone"].to_string().split()[1])

        st.sidebar.success("Success")

    if(res==True and len(text)==0):
        st.sidebar.error("fill up")

if(select=="airlines"):
    text=st.sidebar.text_input("Airlines name")
    res=st.sidebar.button("OK")
    if(res==True and len(text)!=0):
        api_result = requests.get('http://api.aviationstack.com/v1/airlines', params)
        dict_train=api_result.json()
        fram=pd.DataFrame(dict_train['data'])

        store=fram.loc[fram['airline_name'] == text.title()]
        st.write("airline_id =",store["airline_id"].to_string().split()[1])
        st.write("callsign =",store["callsign"].to_string().split()[1])
        st.write("country_iso2 =",store["country_iso2"].to_string().split()[1])
        st.write("date_founded =",store["date_founded"].to_string().split()[1])
        st.write("airline_name =",store["airline_name"].to_string().split()[1])
        st.write("country_name =",store["country_name"].to_string().split()[1])
        st.write("fleet_size =",store["fleet_size"].to_string().split()[1])
        st.write("status =",store["status"].to_string().split()[1])

        st.sidebar.success("Success")


    if(res==True and len(text)==0):
        st.sidebar.error("fill up")  

if(select=="flight"):
    text=st.sidebar.text_input("airplane_id")
    res=st.sidebar.button("OK")
    if(res==True and len(text)!=0):
        api_result = requests.get('http://api.aviationstack.com/v1/airplanes', params)
        dict_train=api_result.json()
        fram=pd.DataFrame(dict_train['data'])

        store=fram.loc[fram['airplane_id'] == text.title()]
        st.write("engines_count =",store["engines_count"].to_string().split()[1])
        st.write("engines_type =",store["engines_type"].to_string().split()[1])
        st.write("plane_age =",store["plane_age"].to_string().split()[1])
        st.write("model_name =",store["model_name"].to_string().split()[1])
        st.write("plane_owner =",store["plane_owner"].to_string().split()[1])
        st.write("plane_status =",store["plane_status"].to_string().split()[1])
        st.write("production_line =",store["production_line"].to_string().split()[1])

        st.sidebar.success("Success")


    if(res==True and len(text)==0):
        st.sidebar.error("fill up") 

if(select=="cities"):
    text=st.sidebar.text_input("city_name")
    res=st.sidebar.button("OK")
    if(res==True and len(text)!=0):
        api_result = requests.get('http://api.aviationstack.com/v1/cities', params)
        dict_train=api_result.json()
        fram=pd.DataFrame(dict_train['data'])

        store=fram.loc[fram['city_name'] == text.title()]
        st.write("id =",store["id"].to_string().split()[1])
        st.write("gmt =",store["gmt"].to_string().split()[1])
        st.write("iata_code =",store["iata_code"].to_string().split()[1])
        st.write("latitude =",store["latitude"].to_string().split()[1])
        st.write("longitude =",store["longitude"].to_string().split()[1])
        st.write("city_name =",store["city_name"].to_string().split()[1])

        st.sidebar.success("Success")


    if(res==True and len(text)==0):
        st.sidebar.error("fill up") 

if(select=="country"):
    text=st.sidebar.text_input("country_name")
    res=st.sidebar.button("OK")
    if(res==True and len(text)!=0):
        api_result = requests.get('http://api.aviationstack.com/v1/countries', params)
        dict_train=api_result.json()
        fram=pd.DataFrame(dict_train['data'])

        store=fram.loc[fram['country_name'] == text.title()]
        st.write("country_id =",store["country_id"].to_string().split()[1])
        st.write("capital =",store["capital"].to_string().split()[1])
        st.write("country_name =",store["country_name"].to_string().split()[1])
        st.write("currency_name =",store["currency_name"].to_string().split()[1])
        st.write("phone_prefix =",store["phone_prefix"].to_string().split()[1])
        st.write("population =",store["population"].to_string().split()[1])

        st.sidebar.success("Success")


    if(res==True and len(text)==0):
        st.sidebar.error("fill up") 