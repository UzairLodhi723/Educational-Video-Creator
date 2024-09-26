from diffusers import StableDiffusionPipeline
import numpy as np
import torch


class TextToVideoStableDiffusion:
    def __init__(self, model_name="CompVis/stable-diffusion-v1-4", num_frames=10, frame_size=(512, 512)):
        self.num_frames = num_frames
        self.frame_size = frame_size

        self.pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float32)
        self.pipe = self.pipe.to("cpu")  # Running on GPU (change to "cpu" if needed)

    def generate_video_frames(self, text_prompt):
        frames = []
        for i in range(self.num_frames):
            frame_prompt = f"{text_prompt}, frame {i+1}"
            image = self.pipe(frame_prompt).images[0]

            frame = np.array(image).astype(np.uint8)  # Changed to uint8
            frames.append(frame)
        return frames
