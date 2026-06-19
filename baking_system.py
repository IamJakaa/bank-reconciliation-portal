import streamlit as st

# 1. Page Global Setup
st.set_page_config(
    page_title="Bank Reconciliation Portal", 
    page_icon="🏦", 
    layout="wide"
)

# 2. Establish Secure Relational Database Connection
try:
    conn = st.connection("postgresql", type="sql")
except Exception as e:
    st.error(f"❌ Critical Connection Failure: Ensure secrets.toml or cloud deployment parameters are correct. Error details: {e}")
    st.stop()

# 3. Main Dashboard Headers

st.title("🏦 Automated Bank Reconciliation & Audit Portal")
st.caption("Ouk Capstone Project Production Pipeline")
st.markdown("---")

st.write("") 
st.success("📢 **PROPOSAL PRESENTATION FOR MY FELLOW STUDENTS**")


st.subheader("👥 Team Reviewers: Jim, Daniel, and Wafula")

st.markdown(
    """
    ### 🚀 Project Architecture Proposal
    I have initialized this live environment to demonstrate my proposal core data-driven pipeline. 
    """
)

st.info("💡 **Next Step:** I am looking forward to seeing your proposals so we can collaborate on the final design!")
