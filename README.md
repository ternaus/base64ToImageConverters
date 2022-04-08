# Library for converting RGB / Grayscale numpy images from to base64 and back.

## Installation
```
pip install -U image_to_base_64
```

## Conversion

### RGB to base 64
```
base64 = rgb2base64(rgb_image, image_format)
```
where image format is `JPEG`, `PNG`

### Grayscale to base 64

```
base64 = grayscale2base64(grayscale_image)
```

### Base64 to RGB image

```
rgb_image = base64_to_rgb(base64)
```

### Base64 to Grayscale image
```
grayscale_image = base64_to_grayscale(base64)
```


#### Issues
For some reason I cannot convert `RGB` image to `JPEG` representation in base 64 and back without losses.
=> test only for `PNG` and not `JPEG`
