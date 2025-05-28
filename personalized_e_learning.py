import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset and prepare training data
file_path = './dataset/personalized_learning_dataset.csv'
df = pd.read_csv(file_path)

# Select relevant features
feature_cols = ['Age', 'Engagement_Level', 'Learning_Style', 'Dropout_Likelihood', 'Quiz_Attempts']
df = df[feature_cols + ['Final_Exam_Score']]

# Preprocess
df_encoded = pd.get_dummies(df, columns=['Engagement_Level', 'Learning_Style', 'Dropout_Likelihood'])
def classify_level(score):
    if score < 60:
        return 'low'
    elif score < 85:
        return 'medium'
    else:
        return 'high'
df_encoded['Level'] = df['Final_Exam_Score'].apply(classify_level)
X = df_encoded.drop(columns=['Final_Exam_Score', 'Level'])
y = df_encoded['Level']

# Split and scale
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train_scaled, y_train)

# --- Streamlit UI ---
st.title("Student Understanding Level Predictor")

with st.form("student_form"):
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    engagement = st.selectbox("Engagement Level", options=['High', 'Medium', 'Low'])
    learning_style = st.selectbox("Preferred Learning Style", options=['Visual', 'Reading/Writing', 'Auditory', 'Kinesthetic'])
    dropout = st.selectbox("Dropout Course History", options=['None', 'Few course', 'Many course'])
    quiz_readiness = st.selectbox("Number of Quiz Ready to Take", options=['All', 'Half', 'None'])
    
    submit = st.form_submit_button("Predict Understanding Level")
    
    if submit:
        # Map inputs to match encoding in training data
        input_data = {
            'Age': age,
            'Quiz_Attempts': {'All': 10, 'Half': 5, 'None': 0}[quiz_readiness],
            'Engagement_Level_High': int(engagement == 'High'),
            'Engagement_Level_Low': int(engagement == 'Low'),
            'Engagement_Level_Medium': int(engagement == 'Medium'),
            'Learning_Style_Auditory': int(learning_style == 'Auditory'),
            'Learning_Style_Reading/Writing': int(learning_style == 'Reading/Writing'),
            'Learning_Style_Visual': int(learning_style == 'Visual'),
            'Learning_Style_Kinesthetic': int(learning_style == 'Kinesthetic'),
            'Dropout_Likelihood_None': int(dropout == 'None'),
            'Dropout_Likelihood_Few course': int(dropout == 'Few course'),
            'Dropout_Likelihood_Many course': int(dropout == 'Many course')
        }

        input_df = pd.DataFrame([input_data])
        
        # Align features
        for col in X.columns:
            if col not in input_df.columns:
                input_df[col] = 0  # Fill missing columns

        input_scaled = scaler.transform(input_df[X.columns])
        prediction = clf.predict(input_scaled)[0]
        st.success(f"Predicted Understanding Level: **{prediction.upper()}**")
