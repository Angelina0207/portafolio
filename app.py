import streamlit as st

# ---------------------- DATOS PERSONALES ---------------------
info = {
    "Pronoun": "ella", 
    "Name": "Paula",
    "Full_Name": "Paula Chirinos",
    "Intro": "Publicista en formación, apasionada por el cine y la fotografía",
    "About": "¡Hola! Soy Paula, estudiante de quinto ciclo de Publicidad en la PUCP. Me encantan las artes y poder orientar aspectos empresariales del Marketing hacia lo creativo. He participado en voluntariados de cine y trabajado en atención al cliente, aplicando estrategias comunicativas. Conoce mis experiencias fotográficas en Instagram: [paula_jchirinos](https://www.instagram.com/paula_jchirinos?igsh=MXZvbXRiMzMwcDZ1MA%3D%3D&utm_source=qr)",
    "City": "Lima, Perú",
    "Photo": "https://i.imgur.com/4NZ6uLY.jpg",  # Usa un enlace directo accesible (no drive)
    "Email": "a20230941@pucp.edu.pe"
}

endorsements = {
    "img1": "https://i.imgur.com/yds3ZeZ.jpeg",
    "img2": "https://i.imgur.com/J70h2sZ.jpeg",
    "img3": "https://i.imgur.com/F1gVb1E.jpeg"
}

# ---------------------- DISEÑO EN STREAMLIT ---------------------

st.set_page_config(page_title="Portafolio Paula Chirinos", layout="wide")

# Presentación
col1, col2 = st.columns([1, 2])
with col1:
    st.image(info["Photo"], width=250)
with col2:
    st.title(info["Full_Name"])
    st.subheader(info["Intro"])
    st.markdown(f"📍 {info['City']}")
    st.markdown(f"✉️ {info['Email']}")

# Sección "Sobre mí"
st.markdown("## Sobre mí")
st.write(info["About"])

# Sección de Endosos o Reconocimientos
st.markdown("## Reconocimientos o experiencias visuales")
col1, col2, col3 = st.columns(3)
col1.image(endorsements["img1"], use_column_width=True)
col2.image(endorsements["img2"], use_column_width=True)
col3.image(endorsements["img3"], use_column_width=True)

# Footer
st.markdown("---")
st.markdown("Hecho con ❤️ en Streamlit")


