import numpy as np

def zoom(image, x: int, y: int):
    if isinstance(image, np.ndarray) == False:
        return None
    origin_height = image.shape[0]
    origin_width = image.shape[1]
    if x > origin_width or y > origin_height:
        return None
    zoom_image = image[y:x]
    print(f"New shape after slicing: {zoom_image.shape}")
    return zoom_image