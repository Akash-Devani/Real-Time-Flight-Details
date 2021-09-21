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
    text=st.sidebar.selectbox("select",["Anaa","Arrabury","El Arish International Airport","Les Salines","Apalachicola Regional","Arapoti","Aachen/Merzbruck","Arraias","Aranuka","Aalborg","Mala Mala","Al Ain","Anapa","Aarhus Airport","Altay","Araxa","Al Ghaydah","Quetzaltenango","Abakan","Asaba International","Los Llanos","Abadan","Lehigh Valley International","Alpha","Municipal","Felix Houphouet Boigny","Kabri Dar","Ambler","Bamaga Injinoo","Aboisso","Albuquerque International","Municipal","Abu Simbel","Al-Aqiq","Atambua","Nnamdi Azikiwe International Airport","Albury","Dougherty County","Dyce","General Juan N. Alvarez International","Antrim County","Kotoka","Acandi","Lanzarote","Altenrhein","The Blaye","Anuradhapura","Nantucket Memorial","Ciudad Acuña International Airport","Sahand","Araracuara","Achinsk","Municipal","Arcata","Atlantic City International","Zabol Airport","Adana","Adnan Menderes Airport","Bole International","Aden International Airport","Adiyaman","Lenawee County","Aldan","Arandis","Marka International Airport","Adak Island Ns","Adelaide International Airport","Ardmore Municipal Airport","Andamooka","Kodiak Airport","Andrews","Addison Airport","Ada Municipal","Ardabil","Leuchars","Alldays","San Andres Island","Abemama Atoll","Aek Godang","Abéché","Albert Lea","Aioun El Atrouss","Aeroparque Jorge Newbery","Sochi/Adler International Airport","Vigra","Allakaket","Abu Musa","Alexandria International","Akureyri","San Rafael","Port Alfred","USAF Academy Airstrip","Amalfi","Alta Floresta","Municipal","Municipal","Zarafshan","Afutara Aerodrome","Fort Worth Alliance","Afyon"
])
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
    text=st.sidebar.selectbox("select",["American Airlines","Delta Air Lines","United Airlines","Southwest Airlines Co.","China Southern Airlines","China Eastern","SkyWest Airlines","Air China Limited","Federal Express","Ryanair Ltd.","Expressjet","THY - Turkish Airlines","Lufthansa Cargo","British Airways","Emirates","UPS Airlines","Easyjet Airline Company Limited","Air France","JetBlue","All Nippon Airways","Qatar Airways","Envoy Air Inc.","Aeroflot","Shenzhen Airlines","Air Canada","TAM Linhas Aereas","Japan Airlines","Korean Air","Alaska Airlines","Hainan Airlines","SAS","Garuda","Cathay Pacific","Republic Airlines","Saudi Arabian Airlines","Azul Brazilian Airlines","Xiamen Airlines","VRG Linhas Aereas S.A. - Grupo GOL","Jazz Aviation LP","Etihad Airways","Lan Airlines","Endeavor Air","Mesa Airlines, Inc.","Qantas","Lion Airlines","WestJet","KLM","SIA Cargo","PSA Airlines","Air India","Sichuan Airlines","Interglobe Aviation Ltd. dba Indigo","Vueling","Alitalia","AVIANCA","Virgin Australia","Shuttle America","Shandong Airlines","Jet Airways","Tianjin Airlines","Vietnam Airlines","COPA Airlines","Shanghai Airlines","Air Berlin","Austrian","Spirit Airlines","Asiana","China Airlines","Allegiant Air LLC","Malaysia Airlines","AirAsia Berhad dba AirAsia","Thai Airways International","IBERIA","flybe","Ethiopian Airlines","Jetstar Airways Pty Limited","Wizz Air Hungary Ltd.","Air Wisconsin Airlines Corporation (AWAC)","SWISS","Trans States Airlines, LLC","EVA Air","S7 Airlines","Aeromexico","Interjet","Aerolitoral S.A. de C.V.","Capital Airlines","Pegasus Airlines","UTair","TUI Airways Limited","Compass Airlines LLC","TAP Portugal","Virgin America","Volaris","Germanwings GmbH","Jet2.com Limited","Philippine Airlines","Spring Airlines Limited Corporation","Frontier Airlines, Inc.","Cebu Pacific Air","Norwegian Air Shuttle A.S.",
])
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
    text=st.sidebar.selectbox("select",["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99",
])
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
    text=st.sidebar.selectbox("select",["Anaa","Arrabury","El Arish","Annaba","Apalachicola","Arapoti","Aachen","Arraias","Awaradam","Aranuka","Aalborg","Mala Mala","Al Ain","Anaco","Anapa","Aarhus","Apalapsili","Altay","Asau","Surallah","Abbottabad","Araxa","Al Ghaydah","Quetzaltenango","Abakan","Asaba","Albacete","Abadan","Allentown","Abaiang","Abingdon","Alpha","Abilene","Abidjan","Kabri Dar","Ambler","Bamaga","Albina","Aboisso","Atkamba","Albuquerque","Aberdeen","Abu Simbel","Al-Baha","Atambua","Abuja","Abau","Albury","Albany","Aberdeen","Acapulco","Bellaire","Accra","Acandi","Arrecife","Altenrhein","Alderney","Anuradhapura","Nantucket","Aguaclara","Arica","Acuna","Sahand","Araracuara","Achinsk","Waco","Achutupo","Arcata","Xingyi","Zabol","Adana","Andakombe","Addis Ababa","Aden","Adiyaman","Adrian","Aldan","Arandis","Adak Island","Adelaide","Ardmore","Andes","Andamooka","Ampara","Kodiak","Andrews","Ada","Ardabil","Camp Springs","St Andrews","Alldays","San Andres Island","Abemama Atoll","Baise","Aleneva","Adareil","Aek Godang","Abeche","Algeciras","Aseki",
])
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
    text=st.sidebar.selectbox("select",["Andorra","United Arab Emirates","Afghanistan","Antigua and Barbuda","Anguilla","Albania","Armenia","Netherlands Antilles","Angola","Antarctica","Argentina","American Samoa","Austria","Australia","Aruba","Aland Islands","Azerbaijan","Bosnia and Herzegovina","Barbados","Bangladesh","Belgium","Burkina Faso","Bulgaria","Bahrain","Burundi","Benin","Saint Barthélemy","Bermuda","Brunei","Bolivia","Bonaire, Saint Eustatius and Saba ","Brazil","Bahamas","Bhutan","Bouvet Island","Botswana","Belarus","Belize","Canada","Cocos Islands","Democratic Republic of the Congo","Central African Republic","Republic of the Congo","Switzerland","Ivory Coast","Cook Islands","Chile","Cameroon","China","Colombia","Costa Rica","Serbia and Montenegro","Cuba","Cape Verde","Curaçao","Christmas Island","Cyprus","Czech Republic","Germany","Djibouti","Denmark","Dominica","Dominican Republic","Algeria","Ecuador","Estonia","Egypt","Western Sahara","Eritrea","Spain","Ethiopia","Finland","Fiji","Falkland Islands","Micronesia","Faroe Islands","France","Gabon","United Kingdom","Grenada","Georgia","French Guiana","Guernsey","Ghana","Gibraltar","Greenland","Gambia","Guinea","Guadeloupe","Equatorial Guinea","Greece","South Georgia and the South Sandwich Islands","Guatemala","Guam","Guinea-Bissau","Guyana","Hong Kong","Heard Island and McDonald Islands","Honduras","Croatia",
])
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