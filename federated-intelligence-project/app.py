import streamlit as st
import random
import time

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Federated Intelligence Demo",
    page_icon="📱",
    layout="wide"
)

# -------------------- SESSION STATE --------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------- LOGIN PAGE --------------------
def login_page():
    st.title("🔐 Secure Login")
    st.write("Simulated authentication for authorized mobile devices")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Please enter username and password")

# -------------------- DASHBOARD --------------------
def dashboard():
    st.title("📊 Federated Intelligence Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Connected Devices", "5")
    col2.metric("Privacy Status", "Enabled 🔒")
    col3.metric("Data Sharing", "Local Only")

    st.success("✔ Raw user data never leaves the device")

    st.markdown("---")
    st.subheader("System Overview")
    st.write("""
    This application demonstrates **Federated Intelligence for Privacy-Preserving
    Mobile Computing Environments** using a simulated workflow.
    """)

# -------------------- ARCHITECTURE PAGE --------------------
def architecture():
    st.title("🏗 Architecture Diagram")

    st.image("assets/architecture.png", caption="Federated Mobile Computing Architecture", use_column_width=True)

    st.markdown("""
    ### Architecture Layers
    - **Mobile Layer:** Local data processing on user devices  
    - **Network Layer:** Secure communication channel  
    - **Cloud Layer:** Aggregation of model updates  
    - **Optimization Layer:** Performance & scalability improvement  
    """)

# -------------------- FEDERATED DEMO --------------------
def federated_demo():
    st.title("🤖 Federated Learning Simulation")

    st.write("Each device trains locally and sends **only model updates**")

    devices = ["Device 1", "Device 2", "Device 3", "Device 4", "Device 5"]
    updates = []

    if st.button("Start Federated Training"):
        progress = st.progress(0)

        for i, device in enumerate(devices):
            time.sleep(0.5)
            update = random.uniform(0.1, 1.0)
            updates.append(update)
            st.write(f"📱 {device} update sent: {update:.3f}")
            progress.progress((i + 1) * 20)

        global_model = sum(updates) / len(updates)

        st.success("✔ Global Model Aggregated Successfully")
        st.metric("Global Model Value", f"{global_model:.3f}")

        st.info("🔐 Raw data remained on user devices")

# -------------------- MODULES PAGE --------------------
def modules():
    st.title("📦 Project Modules")

    with st.expander("Module 1 – Federated Mobile Computing Framework"):
        st.write("""
        Mobile devices perform local computation using private data.
        Only model updates are shared with the server.
        """)

    with st.expander("Module 2 – Privacy Preservation and Optimization"):
        st.write("""
        - No raw data transmission  
        - Reduced network overhead  
        - Improved scalability  
        """)

    with st.expander("Module 3 – Security and Performance Management"):
        st.write("""
        - Secure authentication  
        - Encrypted communication  
        - Adaptive resource management  
        """)

# -------------------- FUTURE SCOPE --------------------
def future_scope():
    st.title("🚀 Future Scope")

    st.checkbox("Differential Privacy")
    st.checkbox("Secure Multi-party Computation")
    st.checkbox("Edge Computing Integration")
    st.checkbox("5G Network Support")
    st.checkbox("Energy-aware Optimization")

    st.info("Future enhancements will further improve privacy and performance")

# -------------------- LOGOUT --------------------
def logout():
    st.session_state.logged_in = False
    st.rerun()

# -------------------- MAIN APP --------------------
if not st.session_state.logged_in:
    login_page()
else:
    st.sidebar.title("📱 Navigation")
    choice = st.sidebar.radio(
        "Go to",
        [
            "Dashboard",
            "Architecture",
            "Federated Demo",
            "Modules",
            "Future Scope",
            "Logout"
        ]
    )

    if choice == "Dashboard":
        dashboard()
    elif choice == "Architecture":
        architecture()
    elif choice == "Federated Demo":
        federated_demo()
    elif choice == "Modules":
        modules()
    elif choice == "Future Scope":
        future_scope()
    elif choice == "Logout":
        logout()

