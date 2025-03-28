import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
def get_sepal_length():
    sepal_length = st.text_input("Sepal Length of IRIS")
    return sepal_length

def get_sepal_width():
    sepal_width = st.text_input("Sepal Width of IRIS")
    return sepal_width

def get_petal_length():
    petal_length = st.text_input("Petal Length of IRIS")
    return petal_length

def get_petal_width():
    petal_width = st.text_input("Petal Width of IRIS")
    return petal_width

def predict_species(sl,sw,pl,pw):
    loaded_model =load_model("mlp_model.h5")
    new_data = [[float(sl),float(sw),float(pl),float(pw)]]
    pred = loaded_model.predict(new_data)
    pred_class=np.argmax(pred, axis=1)
    prediction=le.classes_[pred_class]
    st.write("Prediction with new data: ")
    st.write(prediction)
    



if __name__ == "__main__":
    st.title('IRIS Species prediction with Decision Tree model 2025')
    st.image('iris.png')    
    sepal_length = get_sepal_length()
    sepal_width = get_sepal_width()
    petal_length = get_petal_length()
    petal_width = get_petal_width()
    st.write("The parameters you entered are: ")
    st.write("Sepal length ", sepal_length)
    st.write("Sepal Width ", sepal_width)
    st.write("Petal length ", petal_length)
    st.write("Petal Width ", petal_width)

if st.button("Predict"):
    predict_species(sepal_length,sepal_width,petal_length,petal_width)
    
