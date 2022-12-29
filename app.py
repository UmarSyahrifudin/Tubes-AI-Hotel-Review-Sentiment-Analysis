import numpy as np
import streamlit as st
import pickle

with open("model_pkl", 'rb') as file:
    model = pickle.load(file)


input_review = st.text_area(label="Masukkan Review (Dalam bahasa Inggris):",
                            placeholder="Review")
analisis_button = st.button(label="Analyze")



hasil_analisis = predictions(input_review)
st.write("Hasil Analisis : " + hasil_analisis)
