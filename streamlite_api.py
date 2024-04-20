import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Hello Wilders, welcome to Pattate land where every chips are possible !')
st.write("let's enjoy marvelous smash potatoes and wonderous oil with some little chips topped with chemicals, only 5$")

st.write("un datframe a visé des vieux de 99 ans dont la meteo est devenue la trend en ce moment")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

st.write("un zolie graphique inutile sur le rapport entre l'huile et l'axe de rotation du soleil")

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

st.write("de quoi enrichir les discussions de nos ainés durant les parties de bridge avec leur pilluliers")

st.plotly_chart(px.scatter(df_weather, x="DATE", y="MAX_TEMPERATURE_C"))