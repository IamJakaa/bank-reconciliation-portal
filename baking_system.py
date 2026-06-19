import streamlit as st


st.set_page_config(
    page_title="Bank Reconciliation Portal", 
    page_icon="🏦", 
    layout="wide"
)

# --- MASTER CSS OVERRIDE TO FORCE BRANDING DELETION ---
st.markdown(
    """
    <style>
    /* 1. Target and strip the top main header and digital menu bar */
    header, [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* 2. Strip default footer margins */
    footer {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* 3. Universal target rule to completely wipe the red crown badge */
    [class*="viewerBadge"], 
    [class*="DeployDropdown"],
    [data-testid="stAppDeployDropdown"],
    .stAppDeployDropdown {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        width: 0px !important;
        height: 0px !important;
    }
    
    /* 4. Shift page content up to fill the empty header gap */
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


try:
    conn = st.connection("postgresql", type="sql")
except Exception as e:
    st.error(f"❌ Critical Connection Failure: Ensure secrets.toml or cloud deployment parameters are correct. Error details: {e}")
    st.stop()



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


