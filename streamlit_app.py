
import streamlit as st
import openai

st.set_page_config(page_title="WealthStacker", layout="centered")

st.title("📈 WealthStacker")
st.subheader("AI–Powered Portfolio Builder")
st.write("Answer a few questions to get your personalized investment plan")

# Input form
with st.form("investment_form"):
    age = st.text_input("🎂 Age")
    goal = st.selectbox("🎯 Investment Goal", ["Retirement", "Wealth Growth", "Education", "Real Estate", "Other"])
    horizon = st.text_input("🕒 Investment Time Horizon (years)")
    initial = st.text_input("💵 Initial Investment Amount (optional)", placeholder="e.g., 10000")
    frequency = st.selectbox("📅 Contribution Frequency", ["None", "Weekly", "Monthly", "Quarterly", "Yearly"])
    submitted = st.form_submit_button("Get Portfolio")

if submitted:
    st.info("📡 Generating your portfolio...")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial advisor."},
                {"role": "user", "content": f"My age is {age}, my goal is {goal}, time horizon is {horizon} years, initial investment is {initial}, and I will contribute {frequency}."}
            ]
        )
        st.success("✅ Portfolio suggestion:")
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"⚠️ Error generating portfolio: {e}")
    