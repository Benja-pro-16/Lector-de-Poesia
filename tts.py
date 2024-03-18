import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import sqlite3
from gtts import gTTS

conn = sqlite3.connect('poesias.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS poesias
             (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, texto TEXT)''')
conn.commit()

def agregar_poesia(tit, texto):
    c.execute("INSERT INTO poesias (titulo, texto) VALUES (?, ?)", (tit, texto))
    conn.commit()
    conn.close()
    
def obtener_poesias():
    titulos=[]
    c.execute("SELECT titulo FROM poesias")
    poesias = c.fetchall()
    for poe in poesias:
        titulos.append(poe[0])
    conn.close()
    return titulos

def obtener_texto(tit):
    conn = sqlite3.connect('poesias.db')
    c = conn.cursor()
    c.execute("SELECT texto FROM poesias WHERE titulo= ?", (tit,))
    text = c.fetchone()
    conn.close()
    return text

def formato_poema(txt):
    poema = ""
    for linea in txt:
        linea_con_salto = linea.replace('.', '.\n').replace('.;', '.;\n')
        poema += linea_con_salto.strip() + "\n"
    return poema

def audio(text):
    language = "es"
    speech= gTTS(text=text, lang=language, slow=False, tld="com.mx")
    speech.save("text_to_speech.mp3")
    
st.set_page_config(page_title="Lector de Poemas",page_icon="📝")

st.markdown("<h1 style='text-align:center;'>Lector de Poesía</h1>", unsafe_allow_html=True)
st.image("pluma.jpg")
st.markdown("---")
st.markdown("<h5 style='text-align:center;'>Hola, soy un recitador de poesías. Puedes elegir una poesía que ya conozca o subir tu propia poesía para que la recite.</h5>", unsafe_allow_html=True)

uso = st.radio("¿Quieres escuchar una poesía que ya conozca?", ["Recitame tus poesías", "Subir una poesía"])


if uso == "Recitame tus poesías":
    
    guardadas = st.selectbox("Elegir poesía", options=obtener_poesias())
    
    if guardadas:
        poema = formato_poema(obtener_texto(guardadas))
        on = st.toggle("Ver texto")
        recitar_btn = st.button("Generar Audio", on_click=audio(str(poema)))
        if recitar_btn:
            recitado = st.audio("text_to_speech.mp3")
            if on and recitado:
                largo = len(poema.split("\n")) *25
                st.text_area("Poema:", poema , height=largo)
            
        
else:
    titulo = st.text_input("Ingrese el título")
    if titulo:
        nuevo_texto = st.text_area("Nueva poesía")
        agregar_btn = st.button("Agregar")

        if agregar_btn:
            agregar_poesia(titulo, nuevo_texto)
            st.success("La poesía se agregó correctamente a la lista.")
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
            
    else:
        st.warning("Debe ingresar un título")