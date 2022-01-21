from pathlib import Path
from typing import Union

import requests
from skimage.io import imread

from config.config import ApiConfig


def image_request(model_name: str, img_path: Union[str, Path], verbose=True):
    config = ApiConfig()
    print("Reading input sample to memory...")
    image = imread(img_path)

    json_data = {"input_payload": image.tolist()}

    print("Make predict request to inference API...")
    response = requests.post(
        url=f"{config.API_URL}/image/{model_name}/predict",
        json=json_data,
        headers=config.headers
    )
    if verbose: print(f"Response received: {response.json()}")
    response.raise_for_status()
    return response.content
