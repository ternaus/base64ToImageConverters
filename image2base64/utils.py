import numpy as np


def is_grayscale(image: np.ndarray) -> bool:
    if len(image.shape) == 2:
        return True
    return len(image.shape) == 3 and image.shape[2] == 1
