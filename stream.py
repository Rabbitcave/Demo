import streamlit as st

# ✅ Caching questions using st.cache_data (instead of deprecated st.experimental_memo)
@st.cache_data
def get_questions():
    return [
        {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Rome"], "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What is the largest mammal?", "options": ["Elephant", "Whale", "Shark", "Giraffe"], "answer": "Whale"},
    ]

def run_quiz():
    st.title("🧠 Simple Quiz App")

    questions = get_questions()
    score = 0

    for idx, q in enumerate(questions):
        st.subheader(f"Q{idx + 1}: {q['question']}")
        user_answer = st.radio("Choose an answer:", q["options"], key=idx)
        if user_answer == q["answer"]:
            score += 1

    if st.button("Submit"):
        st.success(f"✅ You got {score} out of {len(questions)} correct!")

# Run the quiz app
if __name__ == "__main__":
    run_quiz()
