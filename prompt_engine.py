def build_candidate_intro_prompt(candidate_info: dict) -> str:
    return (
        f"You are a smart hiring assistant chatbot. A candidate has submitted the following info:\n\n"
        f"Full Name: {candidate_info.get('name')}\n"
        f"Email: {candidate_info.get('email')}\n"
        f"Phone: {candidate_info.get('phone')}\n"
        f"Experience: {candidate_info.get('experience')} years\n"
        f"Desired Role: {candidate_info.get('position')}\n"
        f"Location: {candidate_info.get('location')}\n"
        f"Tech Stack: {candidate_info.get('tech_stack')}\n\n"
        f"Generate 3 to 5 technical interview questions for EACH technology mentioned in the tech stack. "
        f"Be direct, challenging, and relevant to the candidate's years of experience."
    )

def build_fallback_prompt(user_input: str) -> str:
    return (
        f"You are a hiring assistant chatbot. A user has entered:\n'{user_input}'\n"
        f"Respond politely indicating that you couldn't understand the input. "
        f"Ask them to clarify or stay within the interview context."
    )
