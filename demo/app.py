import streamlit as st
import pandas as pd

st.title('Equipo N&L')
st.text('By:')
st.text('Nestor Sebastian Garzon Contreras')
st.text('Santiago Leonardo Delgado Mejia')

df = pd.read_csv('../data/test_data.csv')

st.dataframe(df)

st.image('../cosas_raras_3.png')
