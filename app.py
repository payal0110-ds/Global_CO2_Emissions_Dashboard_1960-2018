import streamlit as st
import pickle

st.set_page_config(
    page_title="CO₂ Emissions Dashboard",
    layout='wide'
)

st.title='Dashboard: 🌍 CO2 Emissions from 1960 to 2018'

with open('bar_chart.pkl','rb') as file:
    bar_chart=pickle.load(file)
with open('line_chart.pkl','rb') as file:
    line_chart=pickle.load(file)
with open('map_chart.pkl','rb') as file:
    map_chart=pickle.load(file)

st.subheader('📈 CO₂ Emissions Trend')
st.plotly_chart(line_chart,use_container_width=True)

st.divider()

st.subheader('CO₂ Emissions by Country Map')
st.plotly_chart(map_chart,use_container_width=True)

st.divider()

st.subheader('Carbon Emissions Race by Country (Since 1960 to 2018)')
st.plotly_chart(bar_chart,use_container_width=True)

