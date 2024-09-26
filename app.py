import asyncio
from utility.script.script_generator import generate_script
from utility.audio.audio_generator import generate_audio
from utility.captions.timed_captions_generator import generate_timed_captions
from utility.video.videoCreation import save_video_with_audio
from utility.model.Model import TextToVideoStableDiffusion
import time
import moviepy.editor as mpy

def main(SAMPLE_TOPIC):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    unique_filename = f"{SAMPLE_TOPIC}_{timestamp}.mp4"
    AUDIO_FILE_NAME = "audio_tts.wav"
    FILE_NAME = unique_filename
    FILE_NAME = "test.mp4"
    response = generate_script(SAMPLE_TOPIC)
    print("script: {}".format(response))
    asyncio.run(generate_audio(response, AUDIO_FILE_NAME))
    audio_path = "audio_tts.wav"
    audio_clip = mpy.AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    image_duration = 5
    num_frames = int(audio_duration / image_duration)
    timed_captions = generate_timed_captions(SAMPLE_FILE_NAME)
    print(timed_captions)
    
    model = TextToVideoStableDiffusion(num_frames=num_frames, frame_size=(256, 256))
    video_frames = model.generate_video_frames(response)
    video =  save_video_with_audio(video_frames, audio_path, filename=FILE_NAME, image_duration=image_duration, captions=[])
    return "/Users/app/Downloads/Text-To-Video-AI-main/data.mp4"
    # return video