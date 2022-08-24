# Library for converting RGB / Grayscale numpy images from to base64 and back.

## Installation
```bash
pip install -U image_to_base_64
```

## Conversion

### RGB to base 64
```python
base64 = rgb2base64(rgb_image, image_format)
```
where image format is `JPEG`, `PNG`

### Grayscale to base 64

```python
base64 = grayscale2base64(grayscale_image)
```

### Base64 to RGB image

```python
output_type = "cv2" # or "PIL"
rgb_image = base64_to_rgb(base64, output_type)
```

### Base64 to Grayscale image
```python
output_type = "cv2" # or "PIL"
grayscale_image = base64_to_grayscale(base64, output_type)
```


#### Issues
For some reason I cannot convert `RGB` image to `JPEG` representation in base 64 and back without losses.
=> test only for `PNG` and not `JPEG`
