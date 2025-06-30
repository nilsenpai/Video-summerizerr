import os
import cv2
import streamlit as st
from langchain_ollama.llms import OllamaLLM

# Ensure these directories exist
videos_directory = "video_summerizerr/videos/"
frames_directory = "video_summerizerr/frames/"
os.makedirs(videos_directory, exist_ok=True)
os.makedirs(frames_directory, exist_ok=True)

# Initialize the Ollama model
model = OllamaLLM(model="gemma3:4b")  # ❗ Fix model name: gemma3.4b does not exist

# Upload video function
def upload_video(file):
    save_path = os.path.join(videos_directory, file.name)
    with open(save_path, "wb") as f:
        f.write(file.getbuffer())
    return save_path

# Extract frames from video at regular intervals
def extract_frames(video_path, interval_seconds=5):
    # Clear previous frames
    for file in os.listdir(frames_directory):
        os.remove(os.path.join(frames_directory, file))

    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frames_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    current_frame = 0
    frame_number = 1

    while current_frame <= frames_count:
        video.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        success, frame = video.read()

        if not success:
            break

        frame_path = os.path.join(frames_directory, f"frame_{frame_number:03d}.jpg")
        cv2.imwrite(frame_path, frame)

        current_frame += fps * interval_seconds
        frame_number += 1

    video.release()

# Describe video using the model + image frames
def describe_video():
    images = [os.path.join(frames_directory, f) for f in sorted(os.listdir(frames_directory))]

    model_with_images = model.bind(images=images)
    return model_with_images.invoke("Summarize the video content in a few sentences.")

# Streamlit UI
st.title("🎞️ Video Summarizer using Ollama + LangChain")

uploaded_file = st.file_uploader(
    "Upload a video file", type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file:
    st.info("Uploading and processing video...")
    video_path = upload_video(uploaded_file)

    st.info("Extracting frames...")
    extract_frames(video_path)

    st.info("Generating summary...")
    summary = describe_video()

    st.subheader("📝 Video Summary")
    st.markdown(summary)
