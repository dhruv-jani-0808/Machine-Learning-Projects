import io
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def image_to_bytes(image_pil, format="JPEG", quality=85):
    buffer = io.BytesIO()

    if image_pil.mode != "RGB":
        image_pil = image_pil.convert("RGB")

    image_pil.save(buffer, format=format, quality=quality)
    return buffer.getvalue()

def compress_image_kmeans(image_pil, n_clusters=8, max_samples=10000, is_grayscale=False):
    if is_grayscale:
        img_work = image_pil.convert("L")
        img_np = np.array(img_work)
        height, width = img_np.shape
        pixels = img_np.reshape(-1, 1)
    else:
        img_work = image_pil.convert("RGB")
        img_np = np.array(img_work)
        height, width, _ = img_np.shape
        pixels = img_np.reshape(-1, 3)

    num_pixels = pixels.shape[0]
    if num_pixels > max_samples:
        indices = np.random.choice(num_pixels, max_samples, replace=False)
        sample_pixels = pixels[indices]
    else:
        sample_pixels = pixels

    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", n_init=3, max_iter=300, random_state=42)
    kmeans.fit(sample_pixels)

    labels = kmeans.predict(pixels)
    centroids = kmeans.cluster_centers_.astype(np.uint8)

    quantized_pixels = centroids[labels]

    if is_grayscale:
        quantized_array = quantized_pixels.reshape(height, width)
        compressed_img = Image.fromarray(quantized_array, mode="L")
        hex_colors = [rgb_to_hex([c[0], c[0], c[0]]) for c in centroids]
    else:
        quantized_array = quantized_pixels.reshape(height, width, 3)
        compressed_img = Image.fromarray(quantized_array, mode="RGB")
        hex_colors = [rgb_to_hex(c) for c in centroids]

    return compressed_img, hex_colors

def compress_to_target_size(image_pil, target_kb, is_grayscale=False):
    orig_bytes = image_to_bytes(image_pil=image_pil)
    orig_size_kb = len(orig_bytes) / 1024.0

    if orig_size_kb <= target_kb:
        compressed_img, hex_colors = compress_image_kmeans(image_pil=image_pil, n_clusters=16, is_grayscale=is_grayscale)
        final_bytes = image_to_bytes(compressed_img)

        return {
            "compressed_image" : compressed_img,
            "final_k" : 16,
            "original_size_kb" : round(orig_size_kb, 2),
            "final_size_kb" : round(len(final_bytes) / 1024.0, 2),
            "reduction_percent" : round((1 - (len(final_bytes) / len(orig_bytes))) * 100, 2),
            "hex_colors" : hex_colors
        }

    k_candidates = [32, 16, 8, 4, 2]
    best_result = None
    current_image = image_pil

    for _ in range(3):
        for k in k_candidates:
            compressed_img, hex_colors = compress_image_kmeans(image_pil=current_image, n_clusters=k, is_grayscale=is_grayscale)
            comp_bytes = image_to_bytes(compressed_img)
            comp_kb = len(comp_bytes) / 1024.0

            best_result = {
                "compressed_image": compressed_img,
                "final_k": k,
                "original_size_kb": round(orig_size_kb, 2),
                "final_size_kb": round(comp_kb, 2),
                "reduction_percent": round((1 - (comp_kb / orig_size_kb)) * 100, 2),
                "hex_colors": hex_colors
            }
            if comp_kb <= target_kb:
                return best_result

        w, h = current_image.size
        current_image = current_image.resize((int(w * 0.75), int(h * 0.75)), Image.Resampling.LANCZOS)

    return best_result