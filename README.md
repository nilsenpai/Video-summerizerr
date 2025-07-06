
# 🎞️ Video Summarizer using Ollama + LangChain

This project allows you to **upload a video**, extract key **frames at intervals**, and generate a **concise summary** using **Ollama's LLM via LangChain**.

## 🧠 Key Features

- ✅ Upload `.mp4`, `.avi`, `.mov`, or `.mkv` video files
- 🖼️ Extracts frames at regular intervals (default: every 5 seconds)
- 🔍 Uses LangChain + Ollama (e.g. Gemma 3 4B model) to summarize video content
- 📄 Simple and clean Streamlit UI

## 🔧 How It Works

1. **Upload** a video file via the Streamlit UI.
2. **Frames** are extracted at intervals using OpenCV.
3. The extracted frames are passed to an LLM with image binding support (`OllamaLLM`).
4. The model **generates a textual summary** based on visual content.

## 📦 Requirements

Install the required packages:

```bash
pip install streamlit opencv-python langchain langchain_community
```

> **Note**: You must have Ollama installed and running locally with a model that supports image input (e.g., `gemma3:4b`). To start Ollama:

```bash
ollama run gemma3:4b
```

## 🏁 How to Run

```bash
streamlit run app.py
```

## 📁 Project Structure

```
video_summerizerr/
├── app.py
├── videos/         # Uploaded videos are saved here
└── frames/         # Extracted frames from video
```

## 📌 Notes

- Make sure your Ollama model is properly named. `gemma3:4b` is used as a placeholder — update if necessary.
- Frame extraction interval can be configured in the `extract_frames()` function.

## 🤖 Credits

Built with ❤️ using:
- [Streamlit](https://streamlit.io)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com)

---

> Give it a ⭐ on GitHub if you find it useful!
