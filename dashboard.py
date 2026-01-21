import streamlit as st
import pandas as pd
import json

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Threat Intelligence SOC",
    layout="wide"
)

# ---------- CUSTOM HACKER STYLE ----------
st.markdown("""
<style>
body {
    background-color: #0b0f14;
    color: #00ff9c;
}
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #0f2027, #000000);
}
h1, h2, h3 {
    color: #00ff9c;
    text-shadow: 0 0 10px #00ff9c;
}
.metric-box {
    background: #111827;
    border: 1px solid #00ff9c;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 15px #00ff9c55;
}
.stDataFrame {
    background-color: #020617;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>🛡️ AI-Powered Cyber Defense SOC</h1>", unsafe_allow_html=True)
st.markdown("### Real-time Threat Intelligence & Risk Analysis")

# ---------- LOAD DATA ----------
with open("analyzed_attacks.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# ---------- METRICS ----------
high = len(df[df["severity"] == "HIGH"])
medium = len(df[df["severity"] == "MEDIUM"])
low = len(df[df["severity"] == "LOW"])

st.markdown("## 🚨 Threat Severity Status")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-box">
        <h2 style="color:red;">HIGH</h2>
        <h1>{high}</h1>
        <p>Critical Threats</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-box">
        <h2 style="color:orange;">MEDIUM</h2>
        <h1>{medium}</h1>
        <p>Suspicious Activity</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-box">
        <h2 style="color:lightgreen;">LOW</h2>
        <h1>{low}</h1>
        <p>Low Risk Events</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- TABLE ----------
st.markdown("## 🧾 Live Threat Feed")
st.dataframe(df, use_container_width=True)
