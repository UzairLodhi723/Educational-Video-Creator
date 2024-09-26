# imports
import streamlit as st
from app import main
import cv2
import time

# Set the page title and layout
st.set_page_config(page_title="Educational Video Creator", layout="centered")

# Customize the title section with styling
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>Educational Video Creator</h1>", unsafe_allow_html=True)

    

# Add space for better layout
st.write("")
st.write("")

def compose(vid_arr):
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)  # Simulate a delay to show the progress bar
        progress_bar.progress(percent_complete + 1)
    st.video(vid_arr)
    # Once the progress is complete, display the video
    st.success("Video generated successfully!")

# Input field and submit button
st.write("## Enter a prompt")

with st.form(key='feedback_form'):
    user_input = st.text_input("Enter a prompt below in the text field, to generate a video out of it!")
    submit_button = st.form_submit_button(label='Generate')

    if submit_button:
        video_result = main(user_input)
        compose(video_result)
        st.success(f"Please wait, while your video is generated: '{user_input}'")
