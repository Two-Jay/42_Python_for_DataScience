from load_image import ft_load
from zoom import zoom
import numpy as np

def main():
    origin = ft_load("animal.jpeg")
    if origin is not None:
        print(origin)
        zoom_image = zoom(origin, 100, 100)
        print(zoom_image)

if __name__ == "__main__":
    main()