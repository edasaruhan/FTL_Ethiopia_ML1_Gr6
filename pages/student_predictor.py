import streamlit as st
from services.predictor import predict_level

def app():
    st.title("Student Understanding Level Predictor")

    with st.form("student_form"):
        age = st.number_input("Age", min_value=10, max_value=100, step=1)
        engagement = st.selectbox("Engagement Level", options=['High', 'Medium', 'Low'])
        learning_style = st.selectbox("Preferred Learning Style", options=['Visual', 'Reading/Writing', 'Auditory', 'Kinesthetic'])
        dropout = st.selectbox("Dropout Course History", options=['None', 'Few course', 'Many course'])
        quiz_readiness = st.selectbox("Number of Quiz Ready to Take", options=['All', 'Half', 'None'])
        
        submit = st.form_submit_button("Predict Understanding Level")
        
        if submit:
            input_data = {
                'Age': age,
                'Quiz_Attempts': {'All': 10, 'Half': 5, 'None': 0}[quiz_readiness],
                'Engagement_Level_High': int(engagement == 'High'),
                'Engagement_Level_Medium': int(engagement == 'Medium'),
                'Engagement_Level_Low': int(engagement == 'Low'),
                'Learning_Style_Visual': int(learning_style == 'Visual'),
                'Learning_Style_Reading/Writing': int(learning_style == 'Reading/Writing'),
                'Learning_Style_Auditory': int(learning_style == 'Auditory'),
                'Learning_Style_Kinesthetic': int(learning_style == 'Kinesthetic'),
                'Dropout_Likelihood_None': int(dropout == 'None'),
                'Dropout_Likelihood_Few course': int(dropout == 'Few course'),
                'Dropout_Likelihood_Many course': int(dropout == 'Many course'),
            }
            
            prediction = predict_level(input_data)
            st.success(f"Predicted Understanding Level: **{prediction.upper()}**")

if __name__ == "__main__":
    app()
