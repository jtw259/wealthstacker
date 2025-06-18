import streamlit as st
import openai
import os

# Load your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="WealthStacker", layout="centered")
st.title("📈 WealthStacker")
st.subheader("AI–Powered Portfolio Builder")
st.write("Answer a few questions to get your personalized investment plan")

with st.form("investment_form"):
    age = st.text_input("🎂 Age", placeholder="Enter your age")
    goal = st.selectbox("🎯 Investment Goal", ["Retirement", "Wealth Building", "Education", "Home Purchase"])
    horizon = st.text_input("⏳ Investment Time Horizon (years)", placeholder="How many years until you need the money?")
    initial = st.text_input("💵 Initial Investment Amount (Optional)", placeholder="e.g., 10000")
    frequency = st.selectbox("📅 Contribution Frequency", ["Monthly", "Quarterly", "Annually", "One-Time"])
    submitted = st.form_submit_button("Generate My Portfolio")

    if submitted:
        with st.spinner("Analyzing and building your plan..."):
            try:
                prompt = f"""Build an investment portfolio for a {age}-year-old with the goal of {goal}, time horizon of {horizon} years, initial investment of ${initial or '0'}, and contribution frequency: {frequency}."""
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success("Here's your personalized portfolio plan:")
                st.markdown(response.choices[0].message['content'])
            except Exception as e:
                st.error(f"Error generating portfolio: {e}")
