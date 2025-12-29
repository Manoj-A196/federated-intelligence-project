import streamlit as st
import pandas as pd

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="Privacy Tracking Demo",
    page_icon="🔐",
    layout="wide"
)

st.title("🔍 Device Privacy Tracking – Working Model")
st.caption("Simulation of raw data and sensitive information tracking in mobile devices")

st.divider()

# ---------------------------------------
# SIMULATED DEVICE DATA
# ---------------------------------------
data = {
    "Device / App Name": [
        "Location Tracker",
        "Social Media App",
        "Fitness App",
        "Camera Service",
        "System Analytics",
        "Music Player"
    ],
    "Tracks Location": ["Yes", "Yes", "No", "No", "No", "No"],
    "Tracks Personal Info": ["No", "Yes", "No", "No", "No", "No"],
    "Tracks Usage Data": ["Yes", "Yes", "Yes", "No", "Yes", "No"],
    "Tracks Raw Data": ["Yes", "Yes", "No", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

# ---------------------------------------
# RISK LEVEL CALCULATION
# ---------------------------------------
def calculate_risk(row):
    if row["Tracks Raw Data"] == "Yes":
        return "High 🔴"
    elif row["Tracks Personal Info"] == "Yes":
        return "Medium 🟠"
    else:
        return "Low 🟢"

df["Privacy Risk Level"] = df.apply(calculate_risk, axis=1)

# ---------------------------------------
# DISPLAY TABLE
# ---------------------------------------
st.subheader("📱 Detected Devices / Applications")

st.dataframe(df, use_container_width=True)

st.divider()

# ---------------------------------------
# RAW DATA TRACKING HIGHLIGHT
# ---------------------------------------
st.subheader("🚨 Raw Data Tracking Detection")

raw_tracking = df[df["Tracks Raw Data"] == "Yes"]

if not raw_tracking.empty:
    for device in raw_tracking["Device / App Name"]:
        st.error(f"⚠️ {device} is tracking RAW USER DATA")
else:
    st.success("No devices detected tracking raw data")

st.divider()

# ---------------------------------------
# PRIVACY SUMMARY
# ---------------------------------------
st.subheader("🔐 Privacy Status Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Devices", len(df))
col2.metric("Raw Data Tracking", len(raw_tracking))
col3.metric(
    "Privacy Status",
    "At Risk" if len(raw_tracking) > 0 else "Safe"
)

st.info("""
✔ This model simulates privacy monitoring  
✔ Raw data tracking is highlighted clearly  
✔ No real user data is accessed  
✔ Demonstrates need for privacy-preserving architectures
""")

st.caption("Academic demo – simulated privacy tracking model")
