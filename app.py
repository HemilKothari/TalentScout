import streamlit as st
from chatbot import Chatbot
from utils import is_exit_command, save_candidate_data

# Initialize chatbot once
if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🧠")
st.title("🧠 TalentScout AI Hiring Assistant")
st.markdown("Hi there! I'm your smart assistant for screening tech candidates.\n\nLet's get started!")

# Collect candidate information step-by-step
with st.form("candidate_info_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.slider("Years of Experience", 0, 30, 1)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (comma separated, e.g., Python, Django, React)")

    submitted = st.form_submit_button("Submit Info")

if submitted:
    candidate = {
        "name": name,
        "email": email,
        "phone": phone,
        "experience": experience,
        "position": position,
        "location": location,
        "tech_stack": tech_stack
    }

    st.session_state.chatbot.set_candidate_info(candidate)

    st.success("Candidate information submitted successfully!")
    st.markdown("### 🤖 Generating technical questions...")
    with st.spinner("Thinking..."):
        questions = st.session_state.chatbot.generate_questions()

    for tech, q_list in questions.items():
        st.markdown(f"**{tech}**:")
        for idx, q in enumerate(q_list, 1):
            st.markdown(f"{idx}. {q}")

    save_candidate_data(candidate, questions)

    st.markdown("---")
    st.markdown("✅ Conversation Ended. Thank you for using TalentScout!")

elif st.session_state.chatbot.has_candidate_info():
    st.markdown("👋 You already submitted the candidate info. Refresh to restart.")
