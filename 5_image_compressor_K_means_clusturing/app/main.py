import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from app.kmeans import compress_image_kmeans, compress_to_target_size
from app.utils import read_image_from_bytes, image_to_base64

app = FastAPI(title="Image Compressor via K-Means Clustering")

static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def serve_index():
    index_path = os.path.join(static_dir, "index.html")
    return FileResponse(index_path)

@app.post("/api/compress")
async def compress_image_endpoint(
    file: UploadFile = File(...),
    mode: str = Form("clusters"),
    n_clusters: int = Form(8),
    target_kb: float = Form(100.0),
    is_grayscale: bool = Form(False)
):
    try:
        contents = await file.read()
        if not contents:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        orig_img = read_image_from_bytes(contents)
        orig_size_kb = round(len(contents) / 1024.0, 2)
        orig_b64 = image_to_base64(orig_img)

        if mode == "target_size":
            result = compress_to_target_size(orig_img, target_kb=target_kb, is_grayscale=is_grayscale)
            comp_img = result["compressed_image"]
            final_k = result["final_k"]
            final_size_kb = result["final_size_kb"]
            reduction_percent = result["reduction_percent"]
            hex_colors = result["hex_colors"]
        else:
            comp_img, hex_colors = compress_image_kmeans(
                orig_img, 
                n_clusters=n_clusters, 
                is_grayscale=is_grayscale
            )
            final_k = n_clusters
            comp_b64_temp = image_to_base64(comp_img)
            comp_bytes_len = len(comp_b64_temp.split(",")[1]) * 3 / 4
            final_size_kb = round(comp_bytes_len / 1024.0, 2)
            reduction_percent = round((1 - (final_size_kb / orig_size_kb)) * 100, 2) if orig_size_kb > 0 else 0.0
        comp_b64 = image_to_base64(comp_img)

        return JSONResponse(content={
            "success": True,
            "filename": file.filename,
            "mode": mode,
            "is_grayscale": is_grayscale,
            "final_k": final_k,
            "original_size_kb": orig_size_kb,
            "final_size_kb": final_size_kb,
            "reduction_percent": max(0.0, reduction_percent),
            "original_image": orig_b64,
            "compressed_image": comp_b64,
            "hex_colors": hex_colors
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))