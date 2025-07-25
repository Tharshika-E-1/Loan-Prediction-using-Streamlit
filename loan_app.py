import streamlit as st

st.set_page_config(page_title="Loan Eligibility Checker", page_icon="💸")

st.title("💸 Loan Eligibility Predictor")
st.subheader("Check if you're eligible for a loan in seconds!")

# Sidebar for user details
st.sidebar.header("📋 Applicant Information")

name = st.sidebar.text_input("Full Name")
gender = st.sidebar.radio("Gender", ["Male", "Female", "Other"])
married = st.sidebar.selectbox("Marital Status", ["Unmarried", "Married"])
dependents = st.sidebar.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.sidebar.radio("Education", ["Graduate", "Not Graduate"])
employment = st.sidebar.radio("Employment Type", ["Salaried", "Self-Employed"])
applicant_income = st.sidebar.number_input("Monthly Income (₹)", min_value=0)
loan_amount = st.sidebar.number_input("Loan Amount (₹)", min_value=0)
loan_term = st.sidebar.slider("Loan Term (in months)", 12, 360, 120)

st.write("### 👇 Result:")
if st.button("Check Eligibility"):
    # Simple Rule-Based Logic
    eligibility = False
    if applicant_income >= 20000 and loan_amount <= applicant_income * 10 and employment == "Salaried":
        eligibility = True
    elif applicant_income >= 30000 and employment == "Self-Employed":
        eligibility = True

    if eligibility:
        st.success(f"🎉 {name}, you are eligible for the loan!")
    else:
        st.error(f"😞 Sorry {name}, you are not eligible based on the provided information.")

st.markdown("---")
st.caption("📌 *This is a demo project. Real loan approvals depend on many financial factors.*")
