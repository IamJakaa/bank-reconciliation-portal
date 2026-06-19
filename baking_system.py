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
