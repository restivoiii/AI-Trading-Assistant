import streamlit as st
import sys
import os

# Ensure Python finds the 'utils' folder
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils.usaspending_api import fetch_agency_overview, fetch_agency_awards

# ---- STREAMLIT UI ----
st.title("USAspending Agency Data Viewer")

# User selects an agency top-tier code
agency_code = st.sidebar.text_input("Enter Agency Top-Tier Code", "097")  # Default: DoD

if st.sidebar.button("Fetch Data"):
    st.subheader(f"Agency Overview ({agency_code})")
    agency_overview = fetch_agency_overview(agency_code)
    st.json(agency_overview)

    st.subheader("Award Summary")
    awards_data = fetch_agency_awards(agency_code)
    st.json(awards_data)

st.sidebar.markdown("---")
st.sidebar.text("Powered by USAspending API")
