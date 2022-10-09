# importing dependencies
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models 
with open('Parkinsons-Disease-Prediction/parkinson_model.sav', 'rb') as parkinson_model:
    parkinson_model = pickle.load(parkinson_model)


with open('Diabetes-Prediction/diabetes_model.sav', 'rb') as diabetes_model:
    diabetes_model = pickle.load(diabetes_model)


with open('Heart-Disease-Prediction/heart_model.sav', 'rb') as heart_model:
    heart_model = pickle.load(heart_model)

with open('Breast-Cancer-Prediction/breast_model.sav', 'rb') as breast_model:
    breast_model = pickle.load(breast_model)


# Sidebar for Navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',

                            ["Diabetes", 
                            "Parkinson's Disease",
                            "Heart Disease",
                            "Breast Cancer"],
                            icons=['activity', 'person','heart', 'asterisk'],
                            default_index=0)


# Diabetes Prediction Page
if selected == "Diabetes":
    st.title("Diabetes Disease Prediction using ML")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Preganancies =  st.text_input('Number of Pregnancies')

    with col1:
        Glucose =  st.text_input('Glucose Level')

    with col2:
        Blood_Pressure =  st.text_input('Blood Pressure')

    with col2:
        Skin_Thickness =  st.text_input('Skin Thickness value')

    with col1:
        Insulin =  st.text_input('Insulin Level')
    
    with col2:
        BMI =  st.text_input('BMI value')
    
    with col3:
        Diabetes_Pedigree_function =  st.text_input('Diabetes Pedigree Function Value')
    
    with col3:
        Age =  st.text_input('Age of the person')

    # code for prediction
    diab_diagnosis = ""

    # Button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Preganancies, Glucose, Blood_Pressure, Skin_Thickness,
        Insulin, BMI, Diabetes_Pedigree_function, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is Diabetic :("

        if diab_prediction[0] == 0:
            diab_diagnosis = "The person not Diabetic :)"

    st.success(diab_diagnosis)


# Parkinson's Prediction Page
if selected == "Parkinson's Disease":
    st.title("Parkinson's Disease Prediction using ML")
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        mdvp_fo =  st.text_input('MDVP:Fo value(Hz)')

    with col1:
        mdvp_fhi =  st.text_input('MDVP:Fhi value(Hz)')

    with col1:
        mdvp_flo =  st.text_input('MDVP:Flo value(Hz)')

    with col1:
        mdvp_jitter =  st.text_input('MDVP:Jitter(%) value')

    with col1:
        mdvp_jitter_abs =  st.text_input('MDVP:Jitter(Abs) value')

    with col1:
        mdvp_rap =  st.text_input('MDVP:RAP value')
    
    with col1:
        mdvp_ppq =  st.text_input('MDVP:PPQ value')
    
    with col1:
        jitter_ddp =  st.text_input('Jitter:DDP value')
    
    with col2:
        mdvp_shimmer =  st.text_input('MDVP:Shimmer value')
    
    with col2:
        mdvp_shimmer_db =  st.text_input('MDVP:Shimmer(dB) value')
    
    with col2:
        shimmer_apq3 =  st.text_input('Shimmer:APQ3 value')
    
    with col2:
        shimmer_apq5 =  st.text_input('Shimmer:APQ5 value')
    
    with col2:
        mdvp_apq =  st.text_input('MDVP:APQ value')
    
    with col2:
        shimmer_dda =  st.text_input('Shimmer:DDA value')
    
    with col2:
        nhr =  st.text_input('NHR value')
    
    with col3:
        hnr =  st.text_input('HNR value')
    
    with col3:
        rpde =  st.text_input('RPDE value')
    
    with col3:
        dfa =  st.text_input('DFA value')

    with col3:
        spread1 = st.text_input('Spread1 value')

    with col3:
        spread2 = st.text_input('Spread2 value')
   
    with col3:
        d2 = st.text_input('D2 value')
    
    with col3:
        ppe = st.text_input('PPE value')

    # code for prediction
    park_diagnosis = ""

    # Button for prediction
    if st.button("Parkinson's Disease Test Result"):
        park_prediction = parkinson_model.predict([[mdvp_fo, mdvp_fhi, mdvp_flo,
        mdvp_jitter, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer,
        mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda,
        nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])

        if park_prediction[0] == 1:
            park_diagnosis = "The person has Parkinson's disease :("

        if park_prediction[0] == 0:
            park_diagnosis = "The persom does not have Parkinson's disease :)"

    st.success(park_diagnosis)


# Heart Disease Prediction Page
if selected == "Heart Disease":
    st.title("Heart Disease Disease Prediction using ML")
    st.subheader("Enter 1 for Male and 0 for Female in 'SEX'.")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age =  st.text_input('Age of person')

    with col1:
        sex =  st.text_input('Sex')

    with col1:
        cp =  st.text_input('CP value')

    with col1:
        trestbps =  st.text_input('Trestbps value')

    with col1:
        chol =  st.text_input('Chol Level')
    
    with col2:
        fbs =  st.text_input('FBS value')
    
    with col2:
        restecg =  st.text_input('Resetecg Value')
    
    with col2:
        thalach =  st.text_input('Thalach value')

    with col2:
        exang =  st.text_input('Exang Level')

    with col3:
        oldpeak =  st.text_input('Oldpeak')

    with col3:
        slope =  st.text_input('Slope value')

    with col3:
        ca =  st.text_input('CA Level')
    
    with col3:
        thal =  st.text_input('Thal value')
    

    # code for prediction
    heart_diagnosis = ""

    # Button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach),
        int(exang), int(oldpeak), int(slope), int(ca), int(thal)]])

        if heart_prediction[0] == 1:
            heart_diagnosis = "The person has Heart Disease :("

        if heart_prediction[0] == 0:
            heart_diagnosis = "The person does not have any Heart Disease :)"

    st.success(heart_diagnosis)



# Breast Cancer Prediction 
if selected == "Breast Cancer":
    st.title("Breast Cancer Prediction using Neural Networks")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius =  st.text_input('Mean radius')

    with col1:
        mean_texture =  st.text_input('Mean texture')

    with col1:
        mean_perimeter =  st.text_input('Mean perimeter')

    with col1:
        mean_area =  st.text_input('Mean Area')

    with col1:
        mean_smoothness =  st.text_input('Mean smoothness')
    
    with col1:
        mean_compactness =  st.text_input('mean Compactness')
    
    with col1:
        mean_concavity =  st.text_input('Mean concavity')
    
    with col1:
        mean_concave_points =  st.text_input('Mean concave points')
    
    with col1:
        mean_symmetry =  st.text_input('Mean symmetry')

    with col1:
        mean_fractal_dimension =  st.text_input('Mean fractal dimension')

    with col2:
        radius_error =  st.text_input('Radius error')

    with col2:
        texture_error =  st.text_input('Texture Error')

    with col2:
        perimeter_error =  st.text_input('Perimeter Error')
    
    with col2:
        area_error =  st.text_input('Area Error')
    
    with col2:
        smoothness_error =  st.text_input('Smoothness Error')
    
    with col2:
        compactness_error =  st.text_input('Compactness Error')

    with col2:
        concavity_error =  st.text_input('Concavity Error')

    with col2:
        concave_points_error =  st.text_input('Cocave Points error')

    with col2:
        symmetry_error =  st.text_input('Symmetry Error')

    with col2:
        fractal_dimension_error =  st.text_input('Fractal Dimension Error')

    with col3:
        worst_radius =  st.text_input('Worst Radius')
    
    with col3:
        worst_texture =  st.text_input('Worst Texture')
    
    with col3:
        worst_perimeter =  st.text_input('Worst Perimeter')
    
    with col3:
        worst_area =  st.text_input('Worst Area')

    with col3:
        worst_smoothness =  st.text_input('Worst Smoothness')

    with col3:
        worst_compactness =  st.text_input('Worst Comapctness')

    with col3:
        worst_concavity =  st.text_input('Worst Concavity')

    with col3:
        worst_concavity =  st.text_input('Worst Concave Points')

    with col3:
        worst_symmetry =  st.text_input('Worst Symmetry')
    
    with col3:
        worst_fractal_dimension =  st.text_input('Worst Fractal Dimension')

    # code for prediction
    breast_diagnosis = ""

    # Button for prediction
    if st.button('Breast Cancer Test Result'):
        breast_prediction = breast_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area,
        mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
        radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error,
        concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius,
        worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity,
        worst_concavity, worst_symmetry, worst_fractal_dimension]])

    
        prediction_label = [np.argmax(breast_prediction)]

        if prediction_label[0] == 1:
            breast_diagnosis = "The person is Diabetic :("

        if prediction_label[0] == 0:
            breast_diagnosis = "The person not Diabetic :)"

    st.success(breast_diagnosis)