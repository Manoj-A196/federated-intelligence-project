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
st.caption("Interactive Working Model | Input → Optimization → Output")

st.divider()

# --------------------------------------------------
# FIXED DEVICE INPUTS (NO SLIDER)
# --------------------------------------------------
st.subheader("🔧 Mobile Device Inputs")

devices = [
    {"Device": "Device 1", "App": "Instagram"},
    {"Device": "Device 2", "App": "Facebook"},
    {"Device": "Device 3", "App": "Google Maps"}
]

device_inputs = []

for i, d in enumerate(devices):
    st.markdown(f"### 📱 {d['Device']} – {d['App']}")

    data_access = st.multiselect(
        "Data Accessed",
        ["Location", "Personal Information", "Usage Data"],
        key=f"data_{i}"
    )

    cpu_usage = st.selectbox(
        "CPU Usage Level",
        ["Low", "Medium", "High"],
        key=f"cpu_{i}"
    )

    network_usage = st.selectbox(
        "Network Usage Level",
        ["Low", "Medium", "High"],
        key=f"net_{i}"
    )

    device_inputs.append({
        "Device": d["Device"],
        "App": d["App"],
        "Data": data_access,
        "CPU": cpu_usage,
        "Network": network_usage
    })

st.divider()

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def usage_to_num(value):
    return {"Low": 1, "Medium": 2, "High": 3}[value]

def calculate_risk(data, network):
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

    centralized = []
    optimized = []

    for d in device_inputs:
        # CENTRALIZED
        c_cpu = usage_to_num(d["CPU"])
        c_net = usage_to_num(d["Network"])
        c_risk = calculate_risk(d["Data"], d["Network"])

        centralized.append([
            d["Device"], d["App"], c_cpu, c_net, c_risk
        ])

        # OPTIMIZED (PRIVACY PRESERVING)
        o_cpu = max(1, c_cpu - 1)
        o_net = 1
        filtered_data = [x for x in d["Data"] if x != "Personal Information"]
        o_risk = calculate_risk(filtered_data, "Low")

        optimized.append([
            d["Device"], d["App"], o_cpu, o_net, o_risk
        ])

    # --------------------------------------------------
    # TABLE OUTPUT
    # --------------------------------------------------
    df_c = pd.DataFrame(
        centralized,
        columns=["Device", "App", "CPU Usage", "Network Usage", "Privacy Risk"]
    )

    df_o = pd.DataFrame(
        optimized,
        columns=["Device", "App", "CPU Usage", "Network Usage", "Privacy Risk"]
    )

    st.subheader("📊 Processing Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔴 Centralized Processing")
        st.dataframe(df_c, use_container_width=True)

    with col2:
        st.markdown("### 🟢 Optimized (Privacy-Preserving)")
        st.dataframe(df_o, use_container_width=True)

    st.divider()

    # --------------------------------------------------
    # CLEAR GRAPH (FIXED)
    # --------------------------------------------------
    st.subheader("📈 Network Usage Reduction (Before vs After)")

    graph_df = pd.DataFrame({
        "Centralized": df_c["Network Usage"],
        "Optimized": df_o["Network Usage"]
    }, index=df_c["Device"])

    st.bar_chart(graph_df, use_container_width=True)

    st.divider()

    # --------------------------------------------------
    # PRIVACY CONFIRMATION
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Result")

    st.success("""
    ✔ Raw personal data blocked  
    ✔ Data processed locally on devices  
    ✔ Network usage reduced  
    ✔ Device performance optimized  
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Academic working model – Device Optimization for Privacy-Preserving Mobile Computing")
