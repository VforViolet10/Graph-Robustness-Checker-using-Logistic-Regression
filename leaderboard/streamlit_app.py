import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:5000"

st.set_page_config(page_title="Graph Robustness Leaderboard", layout="wide")

st.title("🏆 Graph Robustness Challenge Leaderboard")

# -----------------------------
# Sidebar - Submission Upload
# -----------------------------
st.sidebar.header("📤 Submit Your Model")
username = st.sidebar.text_input("Username")
uploaded_file = st.sidebar.file_uploader("Upload submission.csv", type=["csv"])

if st.sidebar.button("Submit"):
    if username and uploaded_file:
        files = {"file": uploaded_file.getvalue()}
        data = {"username": username}
        response = requests.post(f"{API_URL}/submit", files={"file": uploaded_file}, data=data)

        if response.status_code == 200:
            st.sidebar.success(f" Score: {response.json()['score']:.4f}")
        else:
            st.sidebar.error("Submission failed")
    else:
        st.sidebar.warning("Enter username and upload file")

# -----------------------------
# Leaderboard Display
# -----------------------------
st.subheader(" Live Rankings")

try:
    res = requests.get(f"{API_URL}/leaderboard")
    data = res.json()
    df = pd.DataFrame(data)

    if not df.empty:
        df = df.sort_values("score", ascending=False).reset_index(drop=True)
        df.index += 1
        df.index.name = "Rank"

        st.dataframe(df, use_container_width=True)

        # Top 3 Highlight
        st.subheader("🥇 Top Performers")
        top3 = df.head(3)

        cols = st.columns(3)
        medals = ["🥇", "🥈", "🥉"]

        for i, col in enumerate(cols):
            if i < len(top3):
                with col:
                    st.metric(
                        label=f"{medals[i]} {top3.iloc[i]['username']}",
                        value=f"{top3.iloc[i]['score']:.4f}"
                    )

        # Score Chart
        st.subheader(" Score Distribution")
        st.line_chart(df['score'])

    else:
        st.info("No submissions yet.")

except Exception as e:
    st.error(" Could not connect to backend API")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("Built for Graph Robustness Challenge")
