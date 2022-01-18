from pathlib import Path
from typing import Union
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

def show_image(path: Union[str, Path]):
    img = pltimg.imread(path)
    plt.figure(figsize=[1, 1])
    plt.imshow(img)
    plt.axis('off')
    plt.show()
