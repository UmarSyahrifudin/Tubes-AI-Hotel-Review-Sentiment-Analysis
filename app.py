import numpy as np
import streamlit as st
import pickle

with open("model_pkl", 'rb') as file:
    model = pickle.load(file)


input_review = st.text_area(label="Masukkan Review (Dalam bahasa Inggris):",
                            placeholder="Review")
analisis_button = st.button(label="Analyze")


if analisis_button:
    hasil_analisis = model.predict(input_review)
    if hasil_analisis == "Is_Response":
        sentimen = "happy"
    else:
        sentimen = "not happy"
    st.write("Hasil Analisis : " + sentimen)
