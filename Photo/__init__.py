import os
import sys

vendor_path = os.path.join(os.path.dirname(__file__), 'vendor')

if vendor_path not in sys.path:
    sys.path.insert(0, vendor_path)

try:
    from . import photo_core
except ImportError:
    raise ImportError("Не удалось найти Pillow в папке vendor. Убедитесь, что она создана и наполнена.")

def get_module(**kwargs):
    """Регистрирует функции для импорта в язык Dark, согласно документации."""
    return {
        "open": photo_core.open_image_wrapper,
        "save": photo_core.save_image_wrapper,
        "resize": photo_core.resize_image_wrapper,
        "rotate": photo_core.rotate_image_wrapper,
        "grayscale": photo_core.to_grayscale_wrapper,
        "blur": photo_core.apply_blur_wrapper,
        "size": photo_core.get_size_wrapper,
        "add_watermark": photo_core.add_watermark_wrapper,
    }
