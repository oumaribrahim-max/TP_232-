import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="TP232 Dashboard", layout="wide")

st.title("📊 TP232 - Collecte et Analyse des Données")

st.sidebar.header("📥 Entrer les données")

nom = st.sidebar.text_input("Nom")
poids = st.sidebar.number_input("Poids (kg)", min_value=1.0)
taille = st.sidebar.number_input("Taille (m)", min_value=0.5)

if st.sidebar.button("Ajouter"):
    if "data" not in st.session_state:
        st.session_state.data = []

    imc = poids / (taille ** 2)

    st.session_state.data.append({
        "Nom": nom,
        "Poids": poids,
        "Taille": taille,
        "IMC": round(imc, 2)
    })

if "data" in st.session_state:
    df = pd.DataFrame(st.session_state.data)

    st.subheader("📋 Données collectées")
    st.dataframe(df)

    st.subheader("📈 Graphique IMC")
    fig = px.bar(df, x="Nom", y="IMC", color="Nom")
    st.plotly_chart(fig)

    st.success("Données enregistrées ✔")
