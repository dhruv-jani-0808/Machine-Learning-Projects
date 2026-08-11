import io
import base64
from PIL import Image

def read_image_from_bytes(file_bytes: bytes) -> Image.Image:
    """
    Converts raw uploaded byte stream into a PIL Image object.
    """
    buffer = io.BytesIO(file_bytes)
    image = Image.open(buffer)
    image.load()
    return image

def image_to_base64(image_pil: Image.Image, format: str = "JPEG", quality: int = 85) -> str:
    """
    Encodes a PIL Image into a Base64 Data URL string (data:image/jpeg;base64,...)
    for instant rendering on the web frontend.
    """
    buffer = io.BytesIO()
    if image_pil.mode != "RGB" and format.upper() == "JPEG":
        image_pil = image_pil.convert("RGB")

    image_pil.save(buffer, format=format, quality=quality)
    encoded_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    mime_type = "jpeg" if format.upper() == "JPEG" else "png"
    return f"data:image/{mime_type};base64,{encoded_str}"
