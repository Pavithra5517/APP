import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import LabelEncoder
classes={0:"Absent",1:"Present"}
le=LabelEncoder()
def get_gravity():
    gravity = st.text_input("Gravity of URINE")
    return gravity

def get_osmolarity():
    osmolarity = st.text_input("Osmolarity of URINE")
    return osmolarity

def get_conductivity():
    conductivity = st.text_input("Conductivity of URINE")
    return conductivity

def get_urea():
    urea = st.text_input("Urea of URINE")
    return urea

def get_calcium():
    calcium = st.text_input("Calcium of URINE")
    return calcium

def predict(gr,os,co,ur,ca):
    loaded_model =load_model("mlp_kidney.h5")
    new_data =np.array([[float(gr),float(os),float(co),float(ur),float(ca)]])
    pred = loaded_model.predict(new_data)
    pred_class=np.argmax(pred, axis=1)
    prediction=classes[int(pred_class)]
    st.write("Prediction with new data: ")
    st.write(prediction)
    



if __name__ == "__main__":
    st.title('Kidney Stone Presence prediction with MLP model 2025')
    st.image('kidney.jpg')    
    gravity = get_gravity()
    osmolarity = get_osmolarity()
    conductivity = get_conductivity()
    urea=get_urea()
    calcium=get_calcium()
    st.write("The parameters you entered are: ")
    st.write("Gravity ", gravity)
    st.write("Osmolarity ", osmolarity)
    st.write("Conductivity ", conductivity)
    st.write("Urea ", urea)
    st.write("Calcium ", calcium)

if st.button("Predict"):
    predict(gravity,osmolarity,conductivity,urea,calcium)
    
