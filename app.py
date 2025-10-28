import base64
import os
import streamlit as st

IMG_FOLDER = 'images/'

# st.set_page_config(layout="wide")
st.write("# PomoTEST")
st.write("### Dai un valore alla percentuale di pomodoro rosso nell'immagine.")
# DATA
slider_rosso_default = 50
slider_rosso_place_holder = st.empty()
conferma_place_holder = st.empty()
image_index = st.session_state.get("image_index", 0)
images = os.listdir(IMG_FOLDER)
# UI
conferma = st.session_state["conferma"] if "conferma" in st.session_state else None
prossima = st.session_state["prossima"] if "prossima" in st.session_state else None
slider_rosso = st.session_state["slider_rosso"] if "slider_rosso" in st.session_state else None

if conferma != None and conferma:
    st.html(f"Hai indicato un valore di <strong>{slider_rosso}%</strong> di pomodoro rosso nell'immagine {image_index+1}.")
    slider_rosso_place_holder.empty()
    conferma_place_holder.empty()
    prossima = st.button("Prossima immagine ->", key="prossima")

elif prossima != None and prossima:
    if (image_index >= len(images)-1):
        st.write("Non ci sono più immagini da valutare. Grazie per il tuo contributo!")
        slider_rosso_place_holder.empty()
        conferma_place_holder.empty()
        st.stop()
    else:
        image_index += 1
        st.session_state["image_index"] = image_index
        slider_rosso = slider_rosso_place_holder.slider(f'PERCENTUALE di bacca rossa immagine {image_index+1}', 0, 100, slider_rosso_default, step=1, format="%d%%", key="slider_rosso")
        conferma = conferma_place_holder.button("Conferma", key="conferma")

else:
    st.session_state["image_index"] = image_index
    slider_rosso = slider_rosso_place_holder.slider(f'PERCENTUALE di bacca rossa immagine {image_index+1}', 0, 100, slider_rosso_default, step=1, format="%d%%", key="slider_rosso")
    conferma = conferma_place_holder.button("Conferma", key="conferma")

# with open('images/PXL_20250630_094604177.jpg', "rb") as f:
#     data = f.read()
#     encoded = base64.b64encode(data)
# data = "data:image/png;base64," + encoded.decode("utf-8")

st.image(IMG_FOLDER + images[image_index])