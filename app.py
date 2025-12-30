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
st.caption("Single-device optimization demo | Input → Processing → Output")

st.divider()

# --------------------------------------------------
# SINGLE DEVICE INPUT
# --------------------------------------------------
st.subheader("🔧 Mobile Application Configuration")

app_name = st.selectbox(
    "Select Mobile Application",
    ["Instagram", "Facebook", "X (Twitter)", "Snapchat", "Google Maps"]
)

data_access = st.multiselect(
    "Data Accessed by Application",
    ["Location", "Personal Information", "Usage Data"]
)

cpu_usage = st.selectbox(
    "CPU Usage Level",
    ["Low", "Medium", "High"]
)

network_usage = st.selectbox(
    "Network Usage Level",
    ["Low", "Medium", "High"]
)

st.divider()

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def to_numeric(value):
    return {"Low": 1, "Medium": 2, "High": 3}[value]

def risk_level(data, network):
    if "Personal Information" in data or network == "High":
        return "High 🔴"
    elif "Location" in data:
        return "Medium 🟠"
    else:
        return "Low 🟢"

# --------------------------------------------------
# RUN OPTIMIZATION
# --------------------------------------------------
if st.button("▶ Run Device Optimization"):

    # -------- BEFORE OPTIMIZATION --------
    c_cpu = to_numeric(cpu_usage)
    c_net = to_numeric(network_usage)
    c_risk = risk_level(data_access, network_usage)

    st.subheader("🔴 Before Optimization")
    st.write(f"**Application:** {app_name}")
    st.write(f"**CPU Usage Level:** {cpu_usage}")
    st.write(f"**Network Usage Level:** {network_usage}")
    st.write(f"**Privacy Risk:** {c_risk}")

    st.divider()

    # -------- AFTER OPTIMIZATION --------
    o_cpu = max(1, c_cpu - 1)
    o_net = 1
    filtered_data = [x for x in data_access if x != "Personal Information"]
    o_risk = risk_level(filtered_data, "Low")

    st.subheader("🟢 After Optimization")
    st.write(f"**Optimized CPU Usage Level:** {['Low','Medium','High'][o_cpu-1]}")
    st.write(f"**Optimized Network Usage Level:** Low")
    st.write("**Blocked Raw Data:** Personal Information")
    st.write(f"**Privacy Risk:** {o_risk}")

    st.divider()

    # --------------------------------------------------
    # BAR GRAPH (GUARANTEED)
    # --------------------------------------------------
    st.subheader("📈 Network Usage Comparison")

    graph_df = pd.DataFrame({
        "Before Optimization": [c_net],
        "After Optimization": [o_net]
    }, index=[app_name])

    st.bar_chart(graph_df)

    st.caption("Network usage scale: 1 = Low, 2 = Medium, 3 = High")

    st.divider()

    # --------------------------------------------------
    # PRIVACY SUMMARY
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Result")

    st.success("""
    ✔ Data processed locally on device  
    ✔ Raw personal information blocked  
    ✔ Network usage reduced  
    ✔ Privacy risk minimized  
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Academic working model – Device Optimization for Privacy-Preserving Mobile Computing")
