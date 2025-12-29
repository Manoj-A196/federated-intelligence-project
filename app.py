import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Device Optimization – Privacy Preserving Mobile Computing",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Device Optimization for Privacy-Preserving Mobile Computing")
st.caption("Multi-device simulation | Centralized vs Optimized | Federated-style demo")

st.divider()

# --------------------------------------------------
# DEVICE INPUT CONFIGURATION
# --------------------------------------------------
st.subheader("🔧 Device Input Configuration")

num_devices = st.slider("Number of Mobile Devices", 1, 5, 3)

apps = ["Instagram", "Facebook", "X (Twitter)", "Snapchat", "Google Maps"]

device_data = []

for i in range(num_devices):
    st.markdown(f"### 📱 Device {i+1}")
    app = st.selectbox(f"Select App (Device {i+1})", apps, key=f"app{i}")

    data_access = st.multiselect(
        f"Data Accessed (Device {i+1})",
        ["Location", "Personal Information", "Usage Data"],
        key=f"data{i}"
    )

    cpu = st.selectbox(
        f"CPU Usage (Device {i+1})",
        ["Low", "Medium", "High"],
        key=f"cpu{i}"
    )

    network = st.selectbox(
        f"Network Usage (Device {i+1})",
        ["Low", "Medium", "High"],
        key=f"net{i}"
    )

    device_data.append({
        "Device": f"Device {i+1}",
        "App": app,
        "Data": data_access,
        "CPU": cpu,
        "Network": network
    })

st.divider()

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def risk_level(data, cpu, network):
    if "Personal Information" in data or network == "High":
        return 3
    elif "Location" in data:
        return 2
    else:
        return 1

def risk_label(level):
    return ["Low 🟢", "Medium 🟠", "High 🔴"][level-1]

# --------------------------------------------------
# PROCESS BUTTON
# --------------------------------------------------
if st.button("▶ Run Device Optimization Simulation"):
    st.subheader("📊 Centralized vs Optimized Processing")

    centralized = []
    optimized = []
    federated_log = []

    for d in device_data:
        # CENTRALIZED
        c_cpu = 3 if d["CPU"] == "High" else 2 if d["CPU"] == "Medium" else 1
        c_net = 3 if d["Network"] == "High" else 2 if d["Network"] == "Medium" else 1
        c_risk = risk_level(d["Data"], d["CPU"], d["Network"])

        # OPTIMIZED (FEDERATED STYLE)
        o_cpu = max(1, c_cpu - 1)
        o_net = 1
        o_data = [x for x in d["Data"] if x != "Personal Information"]
        o_risk = risk_level(o_data, "Low", "Low")

        centralized.append([d["Device"], d["App"], c_cpu, c_net, c_risk])
        optimized.append([d["Device"], d["App"], o_cpu, o_net, o_risk])

        federated_log.append(
            f"{d['Device']} processed data locally → sent optimized update → raw data blocked"
        )

    # --------------------------------------------------
    # DATAFRAMES
    # --------------------------------------------------
    df_c = pd.DataFrame(
        centralized,
        columns=["Device", "App", "CPU", "Network", "Privacy Risk"]
    )

    df_o = pd.DataFrame(
        optimized,
        columns=["Device", "App", "CPU", "Network", "Privacy Risk"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔴 Centralized Processing")
        st.dataframe(df_c)

    with col2:
        st.markdown("### 🟢 Optimized (Federated-Style)")
        st.dataframe(df_o)

    st.divider()

    # --------------------------------------------------
    # CHARTS
    # --------------------------------------------------
    st.subheader("📈 Performance Comparison (Before vs After)")

    fig, ax = plt.subplots()
    ax.bar(df_c["Device"], df_c["Network"], label="Centralized")
    ax.bar(df_o["Device"], df_o["Network"], label="Optimized")
    ax.set_ylabel("Network Usage Level")
    ax.set_title("Network Usage Reduction")
    ax.legend()
    st.pyplot(fig)

    st.divider()

    # --------------------------------------------------
    # FEDERATED OPTIMIZATION LOG
    # --------------------------------------------------
    st.subheader("📜 Federated Optimization Log")

    for log in federated_log:
        st.code(log)

    st.divider()

    # --------------------------------------------------
    # PRIVACY CONFIRMATION
    # --------------------------------------------------
    st.subheader("🔐 Privacy Preservation Summary")

    st.success("""
    ✔ Data processed locally on devices  
    ✔ Raw personal data blocked  
    ✔ Only optimized updates shared  
    ✔ Reduced network usage and risk  
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Academic working model – simulated device optimization with federated principles")
