import numpy as np

from base64_image_converters.utils import is_grayscale


def test_is_grayscale():
    grayscale_a = np.random.randint(0, 255, (13, 79), dtype=np.uint8)
    grayscale_b = np.random.randint(0, 255, (13, 79, 1), dtype=np.uint8)

    rgb = np.random.randint(0, 255, (13, 79, 3), dtype=np.uint8)
    two_channel = np.random.randint(0, 255, (13, 79, 2), dtype=np.uint8)

    assert is_grayscale(grayscale_a)
    assert is_grayscale(grayscale_b)

    assert not is_grayscale(rgb)

    assert not is_grayscale(two_channel)
