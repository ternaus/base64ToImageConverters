import numpy as np
from PIL import Image

rgb_image_shape = (13, 79, 3)

grayscale_image_shape = (13, 79)

rgb_cv2_image = np.random.randint(0, 255, rgb_image_shape, dtype=np.uint8)

rgb_pil_image = Image.fromarray(rgb_cv2_image)

grayscale_cv2_image = np.random.randint(0, 255, grayscale_image_shape, dtype=np.uint8)

grayscale_pil_image = Image.fromarray(grayscale_cv2_image)
