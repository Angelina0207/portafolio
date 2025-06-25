import streamlit as st

# ---------------------- DATOS PERSONALES ---------------------
info = {
    "Pronoun": "ella",
    "Name": "Paula",
    "Full_Name": "Paula Chirinos",
    "Intro": "Publicista en formación, apasionada por el cine y la fotografía",
    "About": """¡Hola! Soy Paula, estudiante de quinto ciclo de la carrera de Publicidad en la PUCP. 
Me encantan las artes y poder orientar aspectos empresariales del Marketing hacia lo creativo, 
participando en voluntariados orientados al cine o trabajos de atención al cliente donde aplicar estrategias 
para la transmisión de mensajes inspiradores.

Vinculado a la transmisión, conoce un poco de mis experiencias fotográficas en Instagram: 
[paula_jchirinos](https://www.instagram.com/paula_jchirinos?igsh=MXZvbXRiMzMwcDZ1MA&utm_source=qr)""",
    "City": "Lima, Perú",
    "Photo": "https://i.imgur.com/27mdmhl.jpeg",  # Usa un link directo (evita Google Drive)
    "Email": "a20230941@pucp.edu.pe",
    "Phone": "999003581"
}

endorsements = {
    "img1": "https://i.imgur.com/yds3ZeZ.jpeg",
    "img2": "https://i.imgur.com/J70h2sZ.jpeg",
    "img3": "https://i.imgur.com/F1gVb1E.jpeg"
}

# ---------------------- DISEÑO DEL PORTAFOLIO ---------------------
st.set_page_config(page_title="Portafolio Paula Chirinos", layout="wide")

# --- Encabezado con imagen y nombre ---
col1, col2 = st.columns([1, 2])
with col1:
    st.image(info["Photo"], width=250)
with col2:
    st.title(info["Full_Name"])
    st.subheader(info["Intro"])
    st.markdown(f"📍 {info['City']}")
    st.markdown(f"✉️ {info['Email']}")
    st.markdown(f"📞 {info['Phone']}")

# --- Sección: Sobre mí ---
st.markdown("## Sobre mí")
st.markdown(info["About"])

st.markdown("## Sobre Paula")
st.write("""Paula es una estudiante apasionada de Publicidad en la PUCP, con experiencia en la organización de festivales de cine, atención al cliente y ponencias institucionales representando a su universidad frente a colegios y familias de todo el Perú. 
Le encanta capturar el mundo a través de su lente, y combina su sensibilidad visual con habilidades estratégicas de comunicación. 
Curiosa, comprometida y creativa, busca generar conexiones significativas entre las personas y las marcas a través de ideas que inspiran.""")

# --- Experiencia Laboral ---
st.markdown("## Experiencia Laboral")
st.write("- **Atención al cliente en fast food** (2024-2025)")
st.write("- **Apoyo administrativo - Oficina de Admisión PUCP** (2025–actualidad)")

# --- Objetivo Profesional ---
st.markdown("## Objetivo Profesional")
st.write("Desarrollarse como estratega creativa en la industria publicitaria, integrando su pensamiento analítico, sensibilidad cultural y gusto por la narrativa visual para crear campañas relevantes y auténticas.")

# --- Habilidades ---
st.markdown("## Habilidades")
st.write("Canva, Excel, Python, Inglés, Artes visuales")

# --- Certificaciones ---
st.markdown("## Certificaciones")
st.write("- Cambridge B1 Preliminary")
st.write("- Certificado del IB en Artes Visuales (2022)")

# --- Logros ---
st.markdown("## Logros")
st.write("- Parte del equipo del Festival de Cine de Lima de la PUCP con más de 12,000 asistentes")
st.write("- Reconocida por brindar una atención al cliente empática y eficiente")
st.write("- Exposición de obras en el curso de Artes Visuales del Programa IB")

# --- Galería de Imágenes ---
st.markdown("## Galería de experiencias")
col1, col2, col3 = st.columns(3)
with col1:
    st.image(endorsements["img1"], use_container_width=True)
with col2:
    st.image(endorsements["img2"], use_container_width=True)
with col3:
    st.image(endorsements["img3"], use_container_width=True)

# --- Fortalezas ---
st.markdown("## Fortalezas y Ventajas")
st.write("Empática, observadora y versátil, Paula se adapta con facilidad a contextos dinámicos. Su curiosidad constante y dedicación le permiten aportar una mirada fresca y comprometida a los proyectos.")

# --- Debilidades ---
st.markdown("## Desafíos")
st.write("Su nivel de detalle puede ralentizar algunos procesos, pero garantiza resultados cuidados y coherentes con los objetivos del proyecto.")

# --- Intereses ---
st.markdown("## Intereses y Pasatiempos")
st.write("Apasionada por la fotografía, Paula disfruta documentar escenas cotidianas, explorar rincones urbanos, ver cine independiente y compartir conversaciones largas con café de por medio. También le interesa contar historias visuales en redes sociales.")

# --- Portafolio ---
st.markdown("## Portafolio")
st.write("Actualmente se encuentra desarrollando un portafolio digital que reúna sus trabajos en fotografía, producción de eventos y conceptos creativos. Su objetivo es mostrar su enfoque multidisciplinario y su estilo personal.")

# --- Disponibilidad ---
st.markdown("## Disponibilidad")
st.write("Abierta a prácticas, proyectos freelance o roles de asistencia en publicidad, eventos y creación de contenido.")

# --- Referencias ---
st.markdown("## Referencias")
st.write("Disponibles a solicitud.")

# Footer
st.markdown("---")
st.markdown("Creado por Paula Chirinos usando Streamlit.")


