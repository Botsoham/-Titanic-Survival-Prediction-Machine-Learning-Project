import streamlit as st
import joblib
import numpy as np

# Load model safely
@st.cache_resource
def load_model():
    try:
        model = joblib.load("titanic_rf_pipeline.joblib")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

st.title("🚢 Titanic Survival Prediction App")

# If model loaded successfully
if model is not None:
    st.sidebar.header("🧍 Passenger Features")
    
    pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
    sex = st.sidebar.selectbox("Sex", ["male", "female"])
    age = st.sidebar.slider("Age", 0, 80, 25)
    sibsp = st.sidebar.slider("Siblings/Spouses Aboard", 0, 8, 0)
    parch = st.sidebar.slider("Parents/Children Aboard", 0, 6, 0)
    fare = st.sidebar.slider("Fare", 0.0, 500.0, 32.0)
    embarked = st.sidebar.selectbox("Embarked Port", ["S", "C", "Q"])
    
    is_alone = 1 if (sibsp + parch) == 0 else 0

    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked, is_alone]])
    
    if st.button("Predict Survival"):
        try:
            prediction = model.predict(input_data)
            result = "✅ Survived" if prediction[0] == 1 else "❌ Did not survive"
            st.success(result)
        except Exception as e:
            st.error(f"Prediction error: {e}")
else:
    st.warning("Model not loaded. Please check model file.")
