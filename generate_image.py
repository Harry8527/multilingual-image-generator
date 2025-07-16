from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import StableDiffusionPipeline
import torch

class GenerateImage():
    def __init__(self, device="cpu"): 
        model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device=="cuda" else torch.float32)
        self.pipe = self.pipe.to(device)

    def generate_image(self, prompt):
        image = self.pipe(prompt).images[0]
        return image