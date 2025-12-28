import streamlit as st
from youtube_loader import load_youtube_docs
from rag_pipeline import build_vectorstore, answer_question

st.set_page_config(
    page_title="YouTube Chat Assistant",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 Chat with YouTube Video")
st.caption("Paste a YouTube link, process once, then chat instantly ⚡")

# Session states
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat" not in st.session_state:
    st.session_state.chat = []

# Video input
video_url = st.text_input("📌 Paste YouTube Video URL")

if st.button("🚀 Process Video"):
    with st.spinner("Processing video transcript..."):
        docs = load_youtube_docs(video_url)
        st.session_state.vectorstore = build_vectorstore(docs)
        st.success("✅ Video processed! Ask questions below.")

# Chat UI
if st.session_state.vectorstore:
    st.divider()
    st.subheader("💬 Ask Questions")

    user_question = st.chat_input("Ask something about the video...")

    if user_question:
        st.chat_message("user").write(user_question)

        with st.spinner("Thinking..."):
            answer = answer_question(
                st.session_state.vectorstore,
                user_question
            )

        st.chat_message("assistant").write(answer)
