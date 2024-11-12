from fastapi import APIRouter
from PIL import Image

router = APIRouter()


@router.get("/upload")
async def test():
    img = Image.open("IMG20241110212918.jpg")
    width, height = img.size
    new_size = (width // 2, height // 2)
    resized_img = img.resize(new_size)
    resized_img.save("IMG20241110212918_new.jpg", optimize=True, quality=90)
    return {"message": "11"}
