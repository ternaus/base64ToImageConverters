import numpy as np
import pytest

from image2base64.converters import base64_to_grayscale, base64_to_rgb, grayscale2base64, rgb2base64


@pytest.mark.parametrize("image_format", ["PNG"])
def test_rgb_cv2(image_format):
    rgb_image = np.random.randint(0, 255, (13, 79, 3), dtype=np.uint8)
    base64 = rgb2base64(rgb_image, image_format)

    converted_image = base64_to_rgb(base64, output_type="cv2")

    assert converted_image.shape == rgb_image.shape

    assert np.allclose(converted_image.flatten(), rgb_image.flatten()), (converted_image - rgb_image).mean()


@pytest.mark.parametrize("image_format", ["PNG"])
def test_rgb_pil(image_format):
    rgb_image = np.random.randint(0, 255, (13, 79, 3), dtype=np.uint8)
    base64 = rgb2base64(rgb_image, image_format)

    converted_image = base64_to_rgb(base64, output_type="PIL")

    assert converted_image.size == rgb_image.shape[:2][::-1]

    assert np.allclose(np.array(converted_image).flatten(), rgb_image.flatten()), (converted_image - rgb_image).mean()


def test_grayscale_cv2():
    grayscale_image = np.random.randint(0, 255, (13, 79), dtype=np.uint8)

    base64 = grayscale2base64(grayscale_image)
    converted_image = base64_to_grayscale(base64, output_type="cv2")

    assert converted_image.shape == grayscale_image.shape

    assert np.allclose(converted_image.flatten(), grayscale_image.flatten())


def test_grayscale():
    grayscale_image = np.random.randint(0, 255, (13, 79), dtype=np.uint8)

    base64 = grayscale2base64(grayscale_image)
    converted_image = base64_to_grayscale(base64, output_type="PIL")

    assert converted_image.size == grayscale_image.shape[::-1]

    assert np.allclose(np.array(converted_image).flatten(), grayscale_image.flatten())
