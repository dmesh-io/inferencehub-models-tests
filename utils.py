import json
from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from skimage.transform import resize
from skimage.io import imsave

def show_image_from_path(path: Union[str, Path], size=(4, 4)):
    img = pltimg.imread(path)
    plt.figure(figsize=size)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def show_image_from_numpy(array: np.array):
    plt.imshow(array)
    plt.axis('off')
    plt.show()

def show_image_from_response(bt_resp: bytes):
    result = np.array(json.loads(bt_resp))
    show_image_from_numpy(result)

def resize_image(path: Union[str, Path], size=(512, 512)):
    img = pltimg.imread(path)
    img = resize(img, output_shape=size, order=0, anti_aliasing=False, preserve_range=True)
    imsave("input_samples/image-yolo5.png", img)

if __name__=="__main__":
    resize_image("input_samples/image-yolo5.jpg", (512, 512))
