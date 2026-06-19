import streamlit as st


st.set_page_config(
    page_title="Bank Reconciliation Portal", 
    page_icon="🏦", 
    layout="wide"
)

st.markdown(
    """
    <style>
    /* Hide top menu bar completely */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide bottom footer completely */
    footer {visibility: hidden;}
    
    /* Force-hide any floating hosting badges or viewer elements at the bottom right */
    [data-testid="stConnectionStatus"],
    div[class^="viewerBadge"],
    a[class^="viewerBadge"],
    div[class*="viewerBadge"],
    .stAppDeployDropdown {
        display: none !important;
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


st.markdown(
    """
    <style>
    /* Absolute target on any element with a viewerBadge attribute */
    div[class*="viewerBadge"], 
    a[class*="viewerBadge"], 
    iframe + div, 
    .stAppDeployDropdown,
    [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* Clean up bottom spacing */
    footer {
        visibility: hidden !important;
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)