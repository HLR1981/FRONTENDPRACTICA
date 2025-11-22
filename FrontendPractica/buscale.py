# ============================================
#     PRESENTACIÓN DEL PROYECTO
# ============================================
# Nombre del estudiante: Hilario Jimenez Victoriano
# Matrícula: 22760839
# Profesor: Guillermo Alejandro Chávez Sánchez
# Materia: Programación Lógica
# Fecha: Noviembre 2025
# Proyecto: Analizador de conceptos de computación con Streamlit
# ============================================

import streamlit as st
import pandas as pd
import altair as alt
import re

# --- Configuración de la página ---
st.set_page_config(
    page_title="Computación 💻",
    layout="centered",
    page_icon="💡"
)

st.title("💻 Conceptos Clave de la Computación")

# --- Datos ---
data = {
    "Palabra": [
        "Programación", "Algoritmo", "IA", "BD",
        "Redes", "Ciberseguridad", "Hardware", "Software", "Nube",
        "ML", "Blockchain", "SO", "Big Data",
        "RV", "CC"
    ],
    "Importancia": [95, 90, 98, 88, 85, 92, 80, 84, 89, 97, 91, 83, 86, 82, 99],
    "Descripción": [
        "Proceso de crear programas mediante lenguajes de programación.",
        "Conjunto de pasos lógicos para resolver un problema.",
        "Campo que busca que las máquinas imiten la inteligencia humana.",
        "Colección estructurada de información que puede consultarse fácilmente.",
        "Conjunto de dispositivos conectados para compartir recursos y datos.",
        "Protege sistemas y datos contra accesos o ataques no autorizados.",
        "Parte física de una computadora: CPU, RAM, discos, etc.",
        "Parte lógica de una computadora: programas y aplicaciones.",
        "Uso de servidores remotos para almacenar y procesar datos en línea.",
        "Subcampo de la IA que permite a las máquinas aprender de datos.",
        "Tecnología que garantiza transacciones seguras y descentralizadas.",
        "Programa que gestiona los recursos y procesos de una computadora.",
        "Análisis de grandes volúmenes de datos para obtener información útil.",
        "Tecnología que crea entornos digitales inmersivos.",
        "Rama avanzada que usa principios cuánticos para procesar información."
    ],
    "Imagen": [
        "https://cdn-icons-png.flaticon.com/512/2721/2721270.png",
        "https://cdn-icons-png.flaticon.com/512/2206/2206368.png",
        "https://cdn-icons-png.flaticon.com/512/4712/4712107.png",
        "https://cdn-icons-png.flaticon.com/512/1055/1055646.png",
        "https://cdn-icons-png.flaticon.com/512/3208/3208676.png",
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "https://cdn-icons-png.flaticon.com/512/2103/2103832.png",
        "https://cdn-icons-png.flaticon.com/512/3662/3662857.png",
        "https://cdn-icons-png.flaticon.com/512/1048/1048953.png",
        "https://cdn-icons-png.flaticon.com/512/4712/4712108.png",
        "https://cdn-icons-png.flaticon.com/512/2910/2910768.png",
        "https://cdn-icons-png.flaticon.com/512/2306/2306154.png",
        "https://cdn-icons-png.flaticon.com/512/3514/3514341.png",
        "https://cdn-icons-png.flaticon.com/512/4261/4261174.png",
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"
    ]
}

df = pd.DataFrame(data)

# --- Buscador ---
st.subheader("🔍 Buscador de conceptos")

busqueda = st.text_input("Escribe una palabra o parte de ella para buscar:", "")

if busqueda:
    resultados = df[df["Palabra"].str.contains(busqueda, case=False, na=False)]

    if not resultados.empty:
        st.success(f"Se encontraron {len(resultados)} coincidencias:")

        for _, row in resultados.iterrows():
            st.markdown(f"### {row['Palabra']}")
            st.image(row["Imagen"], width=200)
            st.write(row["Descripción"])
            st.progress(row["Importancia"] / 100)

        st.subheader("📊 Nivel de importancia del concepto buscado")

        chart = (
            alt.Chart(resultados)
            .mark_bar(color="#4b9cd3")
            .encode(
                x=alt.X("Importancia:Q", title="Nivel de Importancia"),
                y=alt.Y("Palabra:N", sort="-x", title="Concepto"),
                tooltip=["Palabra", "Descripción", "Importancia"]
            )
            .properties(width=600, height=300)
        )

        st.altair_chart(chart, use_container_width=True)

    else:
        st.warning("No se encontraron coincidencias.")
else:
    st.info("Escribe algo para comenzar la búsqueda. 👆")

# --- Análisis de texto ---
st.markdown("---")
st.subheader("🧠 Análisis de texto")

texto_usuario = st.text_area("Escribe o pega un texto:", height=200)

if st.button("Analizar texto"):
    if texto_usuario.strip():
        texto_limpio = texto_usuario.lower()
        coincidencias = []

        for palabra in df["Palabra"]:
            palabra_simple = re.sub(r"[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ ]", "", palabra).lower()
            if re.search(r"\b" + palabra_simple + r"\b", texto_limpio):
                coincidencias.append(palabra)

        if coincidencias:
            st.success(f"Se encontraron {len(coincidencias)} conceptos.")
            st.write(", ".join(coincidencias))

            coincidencias_df = df[df["Palabra"].isin(coincidencias)]

            chart = (
                alt.Chart(coincidencias_df)
                .mark_bar(color="#3FB5A3")
                .encode(
                    x=alt.X("Importancia:Q"),
                    y=alt.Y("Palabra:N", sort="-x"),
                    tooltip=["Palabra", "Importancia"]
                )
                .properties(width=600, height=300)
            )

            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("No se encontraron conceptos en el texto.")
    else:
        st.warning("Escribe un texto para analizar.")

st.markdown("---")
st.caption("Aplicación desarrollada en Streamlit — Tema: Computación 💻")


