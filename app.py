import streamlit as st
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Load model and preprocessors
@st.cache_resource
def load_models():
    try:
        model = load_model("model.h5")
        with open("onehotEncoder_geography.pkl", "rb") as f:
            geo_encoder = pickle.load(f)
        with open("label_encoder_gender.pkl", "rb") as f:
            gender_encoder = pickle.load(f)
        with open("scale_data.pickle", "rb") as f:
            scaler = pickle.load(f)
        return model, geo_encoder, gender_encoder, scaler
    except FileNotFoundError as e:
        st.error(f"❌ Error loading model files: {e}")
        st.stop()

model, geo_encoder, gender_encoder, scaler = load_models()

# Header
st.title("🎯 Customer Churn Prediction System")
st.markdown("---")

# Create two columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Enter Customer Details")
    
    # Organize inputs in columns
    input_col1, input_col2 = st.columns(2)
    
    with input_col1:
        CreditScore = st.number_input("💳 Credit Score", 300, 900, 650)
        Age = st.number_input("👤 Age", 18, 100, 40)
        Tenure = st.number_input("📅 Tenure (Years)", 0, 10, 5)
        NumOfProducts = st.number_input("📦 Number of Products", 1, 4, 2)
    
    with input_col2:
        Geography = st.selectbox("🌍 Geography", ["France", "Germany", "Spain"])
        Gender = st.selectbox("👨‍👩 Gender", ["Male", "Female"])
        Balance = st.number_input("💰 Balance ($)", 0.0, 300000.0, 50000.0)
        HasCrCard = st.selectbox("🏧 Has Credit Card", ["Yes", "No"])
    
    IsActiveMember = st.selectbox("⭐ Is Active Member", ["Yes", "No"])
    EstimatedSalary = st.slider("💵 Estimated Salary ($)", 0.0, 200000.0, 50000.0, step=1000.0)

with col2:
    st.subheader("📊 Model Info")
    st.info("""
    **Model Details:**
    - Type: Neural Network
    - Task: Churn Prediction
    - Features: 10
    - Output: Probability
    """)

# Prediction button
st.markdown("---")
if st.button("🚀 Predict Churn", use_container_width=True):
    try:
        # Convert Yes/No to binary
        has_credit_card = 1 if HasCrCard == "Yes" else 0
        is_active = 1 if IsActiveMember == "Yes" else 0
        
        # Create DataFrame
        input_data = pd.DataFrame([{
            "CreditScore": CreditScore,
            "Geography": Geography,
            "Gender": Gender,
            "Age": Age,
            "Tenure": Tenure,
            "Balance": Balance,
            "NumOfProducts": NumOfProducts,
            "HasCrCard": has_credit_card,
            "IsActiveMember": is_active,
            "EstimatedSalary": EstimatedSalary
        }])

        # Encode Geography
        geo_encoded = geo_encoder.transform(input_data[["Geography"]])
        geo_df = pd.DataFrame(
            geo_encoded,
            columns=geo_encoder.get_feature_names_out(["Geography"])
        )

        # Encode Gender
        input_data["Gender"] = gender_encoder.transform(input_data["Gender"])

        # Drop old Geography and add encoded
        input_data = input_data.drop("Geography", axis=1)
        input_data = pd.concat([input_data, geo_df], axis=1)

        # Scale
        input_scaled = scaler.transform(input_data)

        # Predict
        pred = model.predict(input_scaled, verbose=0)[0][0]
        pred = float(pred)  
        
        # Display results
        st.markdown("---")
        st.subheader("🎲 Prediction Results")
        
        result_col1, result_col2 = st.columns(2)
        
        with result_col1:
            st.metric("Churn Probability", f"{pred*100:.2f}%", 
                     delta=f"{pred*100:.2f}%" if pred > 0.5 else None)
        
        with result_col2:
            if pred > 0.5:
                st.error(f"⚠️ **HIGH RISK** - Customer is likely to churn ({pred*100:.2f}%)")
            else:
                st.success(f"✅ **LOW RISK** - Customer is likely to stay ({(1-pred)*100:.2f}%)")
        
        # Visualization
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Risk Gauge")
            risk_percentage = pred * 100
            st.progress(pred, text=f"{risk_percentage:.1f}%")
        
        with col2:
            st.subheader("Summary")
            st.write(f"**Churn Risk Level:** {'🔴 High' if pred > 0.5 else '🟢 Low'}")
            st.write(f"**Confidence:** {max(pred, 1-pred)*100:.2f}%")
    
    except Exception as e:
        st.error(f"❌ Prediction error: {str(e)}")

st.markdown("---")
st.caption("🔐 Customer Churn Prediction System v1.0")
