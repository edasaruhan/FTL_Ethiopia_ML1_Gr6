import streamlit as st

st.set_page_config(page_title="Adaptive Learning Platform", layout="wide")

# st.sidebar.title("Adaptive Learning Platform")
# page = st.sidebar.radio("Choose a feature:", 
#                         ["Home", "Student Predictor", "Translation", "Motion Alerts", "Chat Agent"])


st.title("Welcome to the Adaptive Learning Platform")
st.markdown("""
Choose a feature from the sidebar to begin:
- 📊 **Student Predictor**
- 🔍 Translation
- 👀 Motion Alerts
- 💬 Chat Agent
""")

# elif page == "Student Predictor":
#     import pages.student_predictor
#     # Assuming pages.student_predictor.py runs code on import or
#     # you can create a function inside pages.student_predictor.py like `def app():`
#     # then call pages.student_predictor.app()

# elif page == "Translation":
#     import pages.translation_tool
#     # similarly, display translation page

# elif page == "Motion Alerts":
#     import pages.motion_alerts

# elif page == "Chat Agent":
#     import pages.chat_agent
