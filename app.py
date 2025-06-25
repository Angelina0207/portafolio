
import streamlit as st

# -------------------- CONFIGURACIÓN GENERAL --------------------
st.set_page_config(page_title="Portafolio de Yeli", page_icon="🌸", layout="centered")

# -------------------- FOTO PRINCIPAL --------------------
st.markdown("""<a href="https://www.instagram.com/wwkangie"><img src="https://i.imgur.com/KMIU5Oc.png" width="200" alt="Yeli Profile" title="Yeli IG Profile"></a>""")

# -------------------- INTRODUCCIÓN --------------------
st.title("Hola, soy Yeli 💜")
st.subheader("Comunicadora curiosa, creativa y sensible a lo social.")

st.markdown("""
Soy **Angelina Alessandra Contreras Bravo**, aunque todos me dicen **Yeli**.  
Me apasiona explorar historias entre el arte, la cultura y lo digital.  
Actualmente vivo en **Lima, Perú** y estudio Comunicación en la PUCP.  
""")

st.markdown("""
¡Hola! Soy Yeli, una comunicadora de Lima, Perú 🇵🇪 con interés en los discursos sociales, la cultura visual y los temas de género.  
Me gusta trabajar con ideas que conecten emociones y pensamiento crítico, explorar lo narrativo desde lo cotidiano,  
y comunicar de forma cercana y con sentido. En redes, juego, cuestiono y también comparto 💭✨
""")

# -------------------- REDES Y CONTACTO --------------------
st.markdown("### 📬 Redes y contacto")
st.markdown("""
- 📸 Instagram: [@wwkangie](https://www.instagram.com/wwkangie)
- 🎓 Código PUCP: **20231270**
- 📧 Correo: a20231270@pucp.edu.pe
""")

# -------------------- PROYECTOS --------------------
st.markdown("### ✨ Proyectos personales")

st.markdown("#### 💃 Danzas tradicionales")
st.markdown("Me encanta bailar danzas tradicionales y he participado en concursos culturales.")
st.image("https://imgur.com/WYye5NX.png", width=400)

st.markdown("#### 🎥 Videos con conciencia social")
st.markdown("Disfruto creando videos que invitan a reflexionar sobre temas sociales actuales.")
st.image("https://imgur.com/RYjx3HA.png", width=400)

# -------------------- BLOG O PUBLICACIONES --------------------
st.markdown("### 🖊️ Publicaciones y reflexiones")
st.components.v1.html("""<div style="overflow-y: scroll; height:500px; background-color:white;"> <div id="retainable-rss-embed" 
        data-rss="https://medium.com/feed/@yeli-blog"
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Leer más" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> 
        <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>""", height=550)

# -------------------- ARCHIVO BIO --------------------
st.markdown("### 📚 Archivo BIO profesional")
with st.expander("📖 Ver mi biografía completa"):
    st.markdown("""[BIO COMPLETO AQUÍ - OMITIDO PARA BREVEDAD]""")

# -------------------- CIERRE --------------------
st.markdown("""
---
Gracias por visitar mi portafolio 🌷  
Estoy construyendo, explorando y aprendiendo constantemente.  
""")
