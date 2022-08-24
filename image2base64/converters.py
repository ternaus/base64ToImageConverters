import base64
import io
from typing import Union

import numpy as np
from PIL import Image


def output_type_check(output_type: str) -> None:
    if output_type not in ["cv2", "PIL"]:
        raise ValueError(f"output_type should be cv2 or PIL, not {output_type}")


def image2base64(image: np.ndarray, image_format: str = "JPEG", quality: int = 100) -> str:
    buffered = io.BytesIO()

    im = Image.fromarray(image)
    im.save(buffered, format=image_format, quality=quality)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def base64_to_image(image_base64: str, mode: str = "RGB", output_type: str = "cv2") -> Union[np.ndarray, Image.Image]:
    """

    Args:
        image_base64:
        mode: from https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
            ex:
                rgb => RGB
                grayscale => L
        output_type: cv2 or PIL
    Returns:
    """
    output_type_check(output_type)

    image_pil = Image.open(io.BytesIO(base64.b64decode(image_base64))).convert(mode)
    if output_type == "PIL":
        return image_pil

    return np.asarray(image_pil, dtype=np.uint8)


def base64_to_rgb(image_base64: str, output_type: str = "cv2") -> Union[np.ndarray, Image.Image]:
    output_type_check(output_type)
    return base64_to_image(image_base64, "RGB", output_type)


def base64_to_grayscale(image_base64: str, output_type: str = "cv2") -> Union[np.ndarray, Image.Image]:
    output_type_check(output_type)
    return base64_to_image(image_base64, "L", output_type)


def rgb2base64(image: np.ndarray, image_format: str = "JPEG", quality: int = 100) -> str:
    return image2base64(image, image_format, quality)


def grayscale2base64(image: np.ndarray, quality: int = 100) -> str:
    return image2base64(image, image_format="PNG", quality=quality)
