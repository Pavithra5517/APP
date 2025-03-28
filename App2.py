import streamlit as st
import pickle
import sklearn


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
    loaded_model = pickle.load(open('decision_tree_iris.pkl','rb'))
    new_data = [[float(sl),float(sw),float(pl),float(pw)]]
    prediction = loaded_model.predict(new_data)
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
    
