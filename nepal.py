import streamlit as st
import joblib
import pandas as pd

model = joblib.load('nepal_model.pkl')
st.title("Buildding Damage Prediction App")
st.header("input Features")


# Input fields
age_building = st.number_input("Age of Building (0-999)", min_value=0, max_value=999)

foundation_type = st.selectbox(
    "Foundation Type", 
    options=['Mud mortar-Stone/Brick', 'Cement-Stone/Brick', 'RC', 'Other', 'Bamboo/Timber']
)

ground_floor_type = st.selectbox(
    "Ground Floor Type", 
    options=['Mud', 'Brick/Stone', 'RC', 'Timber', 'Other']
)

height_ft_pre_eq = st.number_input(
    "Height (ft) Pre-Earthquake (6-99)", min_value=6, max_value=99
)

land_surface_condition = st.selectbox(
    "Land Surface Condition", 
    options=['Flat', 'Moderate slope', 'Steep slope']
)

other_floor_type = st.selectbox(
    "Other Floor Type", 
    options=['Timber/Bamboo-Mud', 'Timber-Plank', 'RCC/RB/RBC', 'Not applicable']
)

plan_configuration = st.selectbox(
    "Plan Configuration", 
    options=['Rectangular', 'Square', 'L-shape', 'Multi-projected', 'Others', 
             'U-shape', 'T-shape', 'H-shape', 'E-shape', 'Building with Central Courtyard']
)
plinth_area_sq_ft = st.number_input("Plinth Area (sq ft) (70-4995)", min_value=70, max_value=4995)

position = st.selectbox("Position", 
    options=['Not attached', 'Attached-1 side', 'Attached-2 side', 'Attached-3 side'])

roof_type = st.selectbox("Roof Type", 
    options=['Bamboo/Timber-Heavy roof', 'Bamboo/Timber-Light roof', 'RCC/RB/RBC'])

superstructure = st.selectbox("Superstructure", 
    options=['Mud mortar stone', 'Cement mortar brick', 'RE non-engineered', 
             'Stone flag', 'Adobe mud', 'Mud mortar brick', 'Timber', 
             'Cement mortar stone', 'RE engineered', 'Bamboo', 'Other']
)

# Create a dictionary of the input data
input_data = {
    'age_building': age_building,
    'foundation_type': foundation_type,
    'ground_floor_type': ground_floor_type,
    'height_ft_pre_eq': height_ft_pre_eq,  
    'land_surface_condition': land_surface_condition,
    'other_floor_type': other_floor_type,
    'plan_configuration': plan_configuration,
    'plinth_area_sq_ft': plinth_area_sq_ft,
    'position': position,
    'roof_type': roof_type,
    'superstructure': superstructure
}

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df)  # Ensure model is defined before this

    # Display prediction results
    if prediction[0] == 1:  # Access first element of the prediction array
        st.info("Prediction: The building was affected by the earthquake")
    else:
        st.info("Prediction: The building was not affected by the earthquake")