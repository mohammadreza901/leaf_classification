import streamlit as st
from ultralytics import YOLO
import time
from PIL import Image
model=YOLO("../Model/best.pt")
st.title("Leaf-Detection API")
imagefile=st.file_uploader("Upload an image", type="jpg")
if imagefile is not None:
    our_image=Image.open(imagefile)
    im=our_image.save('../image/out.jpg')
    saved_image=st.image(imagefile,caption="",use_column_width=True)
    btn=st.button("prosecced")

    if btn:
        prediction=model(im)
        if prediction[0].probs.top1==0:
            st.title("prediction is::::Afra")
            time.sleep(5)

        if prediction[0].probs.top1==1:
            st.title("prediction is::::lader")
            time.sleep(5)
        if prediction[0].probs.top1==2:
            st.title("prediction is::::baloot")
            time.sleep(5)
        if prediction[0].probs.top1==3:
            st.title("prediction is::::gerdoo")
            time.sleep(5)
        if prediction[0].probs.top1==4:
            st.title("prediction is::::mmrez")
            time.sleep(5)
        if prediction[0].probs.top1==5:
            st.title("prediction is::::parrot_persica")
            time.sleep(5)
        if prediction[0].probs.top1==6:
            st.title("prediction is::::rush")
            time.sleep(5)
    btn2 = st.button("Reload page")
    if btn2:
        st.rerun()