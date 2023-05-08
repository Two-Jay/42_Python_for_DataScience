import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array:
    """
    function to load image date from a file path
    """
    try:
        with Image.open(path) as im:
            img_array = np.array(im)
            print(f"The shape of image is: {img_array.shape}")
            return img_array
    except:
        return None