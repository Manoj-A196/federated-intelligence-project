import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Device Optimization for Privacy-Preserving Mobile Computing",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Device Optimization for Privacy-Preserving Mobile Computing")
st.caption("Working demo model – academic simulation")

st.divider()

# --------------------------------------------------
# INITIAL DEVICE DATA (BEFORE OPTIMIZATION)
# --------------------------------------------------
data = {
    "App / Device": [
        "Instagram",
        "Facebook",
        "X (Twitter)",
        "Snapchat",
        "Google Maps",
        "Music Player"
    ],
    "Data Accessed": [
        "Location, Usage",
        "Location, Personal Info",
        "Usage Data",
        "Location",
        "Location",
        "None"
    ],
    "CPU Usage": ["High", "High", "Medium", "Medium", "Medium", "Low"],
    "Network Usage": ["High", "High", "High", "Medium", "Medium", "Low"],
    "Privacy Risk": ["High 🔴", "High 🔴", "High 🔴", "Medium 🟠", "Medium 🟠", "Low 🟢"]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# DISPLAY BEFORE OPTIMIZATION
# --------------------------------------------------
st.subheader("🔍 Device Status – Before Optimization")
st.dataframe(df, use_container_width=True)

st.divider()

# --------------------------------------------------
# OPTIMIZATION BUTTON
# --------------------------------------------------
optimize = st.button("⚙️ Optimize Devices")

# --------------------------------------------------
# AFTER OPTIMIZATION LOGIC
# --------------------------------------------------
if optimize:
    st.subheader("✅ Device Status – After Optimization")

    optimized_data = {
        "App / Device": df["App / Device"],
        "CPU Usage": ["Medium", "Medium", "Low", "Low", "Low", "Low"],
        "Network Usage": ["Low", "Low", "Low", "Low", "Low", "Low"],
        "Privacy Risk": ["Medium 🟠", "Medium 🟠", "Low 🟢", "Low 🟢", "Low 🟢", "Low 🟢"]
    }

    optimized_df = pd.DataFrame(optimized_data)
    st.dataframe(optimized_df, use_container_width=True)

    st.success("Device optimization completed successfully")

    st.divider()

    # --------------------------------------------------
    # PRIVACY PRESERVATION STATUS
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Status")

    st.info("""
    ✔ Raw user data remains on the device  
    ✔ Only optimized insights are used  
    ✔ Centralized raw data storage is avoided  
    """)

    st.divider()

    # --------------------------------------------------
    # SECURITY & PERFORMANCE
    # --------------------------------------------------
    st.subheader("🛡 Security & Performance Management")

    col1, col2, col3 = st.columns(3)

    col1.metric("Secure Participation", "Enabled")
    col2.metric("Communication", "Encrypted")
    col3.metric("Latency", "Reduced")

    st.success("System performance optimized with privacy preservation")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Simulated working model for academic demonstration")
