import base64
import io

import numpy as np
from PIL import Image


def image2base64(image: np.ndarray, image_format: str = "JPEG", quality: int = 100) -> str:
    buffered = io.BytesIO()

    im = Image.fromarray(image)
    im.save(buffered, format=image_format, quality=quality)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def base64_to_image(image_base64: str, mode: str = "RGB") -> np.ndarray:
    """

    Args:
        image_base64:
        mode: from https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
            ex:
                rgb => RGB
                grayscale => L
    Returns:
    """

    return np.array(
        Image.open(io.BytesIO(base64.b64decode(image_base64))).convert(mode=mode),
        dtype=np.uint8,
    )


def base64_to_rgb(image_base64: str) -> np.ndarray:
    return base64_to_image(image_base64, "RGB")


def base64_to_grayscale(image_base64: str) -> np.ndarray:
    return base64_to_image(image_base64, "L")


def rgb2base64(image: np.ndarray, image_format: str = "JPEG", quality: int = 100) -> str:
    return image2base64(image, image_format, quality)


def grayscale2base64(image: np.ndarray, quality: int = 100) -> str:
    return image2base64(image, image_format="PNG", quality=quality)
