import streamlit as st
import os
import subprocess
import ultralytics
ultralytics.checks()
from ultralytics import YOLO
import shutil

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except:
        return

model_path = 'best.pt'
output_dir = 'runs/classify/predict'

st.set_page_config(page_title='Child Classification', layout='centered')
st.title('Null Class Intership Project')
st.title("Child Classification Project")
st.header('Trained & Developed by Sai Kiran Patnana')
delete_folder('runs')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "test_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    detect_command = f"yolo task=detect mode=predict model={model_path} conf=0.5 source='{image_path}' save_txt=true save_conf=true"
    subprocess.run(detect_command, shell=True)
    output_image_path = os.path.join(output_dir, "test_image.jpg")
    if os.path.exists(output_image_path):
        st.image(output_image_path, caption="Child Classification Result", use_column_width=True)
        with open("runs/classify/predict/labels/test_image.txt",'r') as f:
            a = f.readline()
            if('adults' in a):
                st.markdown(f"<h3 style='text-align: center;'>It's not a Child.</h3>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h3 style='text-align: center;'>It's a Child.</h3>", unsafe_allow_html=True)

                
    else:
        st.write("Error: Output image not found")
    