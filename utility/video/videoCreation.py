import moviepy.editor as mpy


# --- UTILITY FUNCTION TO SAVE VIDEO ---
def save_video_with_audio(frames, audio_path, filename='output_video.mp4', image_duration=5, captions=[]):
    clips = []

    for i, frame in enumerate(frames):
        img_clip = mpy.ImageClip(frame).set_duration(image_duration)

        if i < len(captions):
            caption_text = captions[i][1]
            txt_clip = mpy.TextClip(caption_text, fontsize=24, color='white', bg_color='black', size=img_clip.size)
            txt_clip = txt_clip.set_duration(img_clip.duration).set_position(('center', 'bottom'))
            img_clip = mpy.CompositeVideoClip([img_clip, txt_clip])

        clips.append(img_clip)

    video = mpy.concatenate_videoclips(clips, method="compose")

    audio_clip = mpy.AudioFileClip(audio_path)
    video = video.set_audio(audio_clip)
    video = video.set_duration(audio_clip.duration)

    video.write_videofile(filename, fps=24)
    return video