from aiogram import Router
from diffusers import DiffusionPipeline
import torch
import requests
import io
from PIL import Image

router = Router()

# class TextToImage:
#     def __init__(self):
#         self.pipe = DiffusionPipeline.from_pretrained(
#             "playgroundai/playground-v2-1024px-aesthetic",       # здесь либо указанная ссылка или ссылка на локалькую папку с моделью
#             torch_dtype=torch.float16,
#             use_safetensors=True,
#             add_watermarker=False,
#             variant="fp16"
#         )
#
#     def prompt(self, text):
#         self.pipe.to("mps")
#         image = self.pipe(prompt=text, guidance_scale=3.0).images[0]
#         return image


# По API есть время, которое модель не работает и возвращает ошибку, но API работает быстрее локального использования.
# Сделать обработчик ошибок
class TextToImage:

    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def prompt(self, text):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(self.api_url, headers=headers, json={
            "inputs": text,
            "options": {"wait_for_model": True}
                                                                      })
        return response.content
