# from diffusers import StableDiffusionPipeline
# import torch
# from PIL import Image

# ## https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5 ##

# ## pip install torch diffusers transformers accelerate safetensors ##

# # -------------------------------
# # Load model once
# # -------------------------------
# # You can change to any HF Stable Diffusion model, e.g., "runwayml/stable-diffusion-v1-5"
# pipe = StableDiffusionPipeline.from_pretrained(
#     "runwayml/stable-diffusion-v1-5",
#     torch_dtype=torch.float32,
# )
# pipe = pipe.to("cpu")


# def generate_image(prompt: str, width=512, height=512, steps=25) -> Image.Image:
#     """
#     Generate an image from a text prompt using Hugging Face Stable Diffusion.

#     Args:
#         prompt (str): The text prompt.
#         width (int): Width of the output image.
#         height (int): Height of the output image.
#         steps (int): Number of inference steps (higher = better quality).

#     Returns:
#         PIL.Image.Image: Generated image.
#     """
#     if not prompt.strip():
#         raise ValueError("Prompt cannot be empty.")

#     result = pipe(prompt, width=width, height=height, num_inference_steps=steps)
#     return result.images[0]

# ## https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5 ##

# ## py -3.12 pip install torch diffusers transformers accelerate safetensors ##
## py -3.12 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 ##

####CUDA required foor gpu works otherwise use cpu#### ONLY supported on NVIDIA high powered devices#####
##### python 3.12 required for CUDA ######

##Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

##.\venv312\Scripts\Activate.ps1

from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

class Text2ImageModel:
    def __init__(self):
        # Determine device
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load Stable Diffusion
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32  # use half precision only on GPU
        ).to(device)  # move to GPU or CPU automatically

    def generate_image(self, prompt: str, width=512, height=512, steps=25) -> Image.Image:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        result = self.pipe(prompt, width=width, height=height, num_inference_steps=steps)
        return result.images[0]

# # Determine device
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # Load Stable Diffusion
# pipe = StableDiffusionPipeline.from_pretrained(
#     "runwayml/stable-diffusion-v1-5",
#     torch_dtype=torch.float16 if device == "cuda" else torch.float32  # use half precision only on GPU
# )
# pipe = pipe.to(device)  # move to GPU or CPU automatically

# def generate_image(prompt: str, width=512, height=512, steps=25) -> Image.Image:
#     if not prompt.strip():
#         raise ValueError("Prompt cannot be empty.")

#     result = pipe(prompt, width=width, height=height, num_inference_steps=steps)
#     return result.images[0]