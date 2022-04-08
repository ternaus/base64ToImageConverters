import numpy as np
import pytest

from base64_image_converters.converters import (
    base64_to_grayscale,
    base64_to_rgb,
    grayscale2base64,
    rgb2base64,
)


@pytest.mark.parametrize("image_format", ["PNG"])
def test_rgb(image_format):
    rgb_image = np.random.randint(0, 255, (13, 79, 3), dtype=np.uint8)
    base64 = rgb2base64(rgb_image, image_format)

    converted_image = base64_to_rgb(base64)

    assert converted_image.shape == rgb_image.shape

    assert np.allclose(converted_image.flatten(), rgb_image.flatten()), (converted_image - rgb_image).mean()


def test_grayscale():
    grayscale_image = np.random.randint(0, 255, (13, 79), dtype=np.uint8)

    base64 = grayscale2base64(grayscale_image)
    converted_image = base64_to_grayscale(base64)

    assert converted_image.shape == grayscale_image.shape

    assert np.allclose(converted_image.flatten(), grayscale_image.flatten())
