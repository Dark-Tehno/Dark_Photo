from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def _get_image_obj_impl(image_or_path):
    if isinstance(image_or_path, str):
        if not os.path.exists(image_or_path):
            raise FileNotFoundError(f"Файл не найден: {image_or_path}")
        return Image.open(image_or_path)
    elif isinstance(image_or_path, Image.Image):
        return image_or_path
    else:
        raise TypeError("Аргумент должен быть путем к файлу или объектом Image")


def open_image_wrapper(args):
    if len(args) != 1: raise TypeError("open() ожидает 1 аргумент: путь к файлу")
    return _get_image_obj_impl(args[0])

def save_image_wrapper(args):
    if len(args) < 2: raise TypeError("save() ожидает минимум 2 аргумента: объект изображения и путь")
    image, path = args[0], args[1]
    quality = args[2] if len(args) > 2 else 95
    
    img_obj = _get_image_obj_impl(image)
    img_obj.save(path, quality=quality)
    return True

def resize_image_wrapper(args):
    if len(args) != 3: raise TypeError("resize() ожидает 3 аргумента: изображение, ширина, высота")
    image, width, height = args
    img_obj = _get_image_obj_impl(image)
    return img_obj.resize((int(width), int(height)))

def rotate_image_wrapper(args):
    if len(args) < 2: raise TypeError("rotate() ожидает минимум 2 аргумента: изображение и угол")
    image, angle = args[0], args[1]
    expand = args[2] if len(args) > 2 else True
    img_obj = _get_image_obj_impl(image)
    return img_obj.rotate(angle, expand=expand)

def to_grayscale_wrapper(args):
    if len(args) != 1: raise TypeError("grayscale() ожидает 1 аргумент: изображение")
    img_obj = _get_image_obj_impl(args[0])
    return img_obj.convert("L")

def apply_blur_wrapper(args):
    if len(args) < 1: raise TypeError("blur() ожидает минимум 1 аргумент: изображение")
    image = args[0]
    radius = args[1] if len(args) > 1 else 2
    img_obj = _get_image_obj_impl(image)
    return img_obj.filter(ImageFilter.GaussianBlur(radius))

def get_size_wrapper(args):
    if len(args) != 1: raise TypeError("size() ожидает 1 аргумент: изображение")
    img_obj = _get_image_obj_impl(args[0])
    return list(img_obj.size)

def add_watermark_wrapper(args):
    if len(args) < 3: raise TypeError("add_watermark() ожидает минимум 3 аргумента: изображение, текст, позиция")
    image, text, position = args[0], args[1], args[2]
    color = tuple(args[3]) if len(args) > 3 else (255, 255, 255)
    size = int(args[4]) if len(args) > 4 else 30
    
    img_obj = _get_image_obj_impl(image).copy().convert("RGBA")
    draw = ImageDraw.Draw(img_obj)
    try:
        font = ImageFont.load_default(size=size)
    except AttributeError:
        font = ImageFont.load_default()
    draw.text(tuple(position), text, fill=color, font=font)
    return img_obj