import numpy as np
import pytest

from image2base64.converters import base64_to_grayscale, base64_to_rgb, grayscale2base64, rgb2base64

from .conftest import grayscale_cv2_image, grayscale_pil_image, rgb_cv2_image, rgb_pil_image


def get_converted_image(image_format, image):
    if isinstance(image, np.ndarray):
        image_shape = image.shape
    else:
        image_width, image_height = image.size
        if image.mode == "RGB":
            image_shape = (image_height, image_width, 3)
        else:
            image_shape = (image_height, image_width)

    if len(image_shape) == 3:
        base64 = rgb2base64(image, image_format)
        converted_image = base64_to_rgb(base64, output_type="cv2")
    else:
        base64 = grayscale2base64(image)
        converted_image = base64_to_grayscale(base64, output_type="cv2")

    return converted_image, image_shape


@pytest.mark.parametrize(
    ["image_format", "image"],
    [("PNG", rgb_cv2_image), ("PNG", rgb_pil_image), ("PNG", grayscale_cv2_image), ("PNG", grayscale_pil_image)],
)
def test_to_cv2(image_format, image):
    converted_image, image_shape = get_converted_image(image_format, image)

    assert converted_image.shape == image_shape
    assert np.allclose(converted_image.flatten(), np.array(image).flatten()), (converted_image - np.array(image)).mean()


@pytest.mark.parametrize(
    ["image_format", "image"],
    [("PNG", rgb_cv2_image), ("PNG", rgb_pil_image), ("PNG", grayscale_cv2_image), ("PNG", grayscale_pil_image)],
)
def test_to_pil(image_format, image):
    converted_image, image_shape = get_converted_image(image_format, image)

    assert converted_image.shape == image_shape

    assert np.allclose(np.array(converted_image).flatten(), np.array(image).flatten()), (
        np.array(converted_image) - np.array(image)
    ).mean()
