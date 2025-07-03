import streamlit as st
import os
from datetime import datetime

UPLOAD_FOLDER = "uploads"

# Create folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="AI Micro-Solutions Platform", layout="centered")
st.title("🎥 AI Micro-Solutions Platform")
st.subheader("Empowering educators with short videos that solve classroom problems")

st.markdown("Upload a short video that addresses a common classroom or student challenge.")

# Upload Form
with st.form("upload_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    problem_tag = st.text_input("Problem Addressed (e.g., bullying, motivation)")
    video_file = st.file_uploader("Upload Video (MP4)", type=["mp4"])
    submitted = st.form_submit_button("Upload")

    if submitted and video_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{problem_tag}_{timestamp}.mp4"
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(save_path, "wb") as f:
            f.write(video_file.read())
        st.success(f"✅ Uploaded as `{filename}`")

# Display Existing Videos
st.markdown("---")
st.subheader("🎬 Available Micro-Solution Videos")

videos = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".mp4")]
if videos:
    for video in sorted(videos, reverse=True):
        st.video(os.path.join(UPLOAD_FOLDER, video))
        st.caption(f"`{video}`")
else:
    st.info("No videos uploaded yet.")
