# Dark_Photo

`Photo` — это самодостаточная библиотека для языка Dark для манипуляции изображениями.

Библиотека включает в себя ("вендорит") все необходимые зависимости (`Pillow`, `numpy`) и не требует от пользователя их отдельной установки через `pip`.

## Установка

Создайте виртуальное окружене:
```bash
dark --denv denv
```
После активируйте командой
```bash
source denv/bin/activate
```
Загрузите себе расширение
```dark
dark --dpm install Photo
```

## Использование

Библиотека предоставляет следующие функции:

*   `Photo.open(path: str)`: Открывает изображение и возвращает его объект.
*   `Photo.save(image, path: str, quality: int = 95)`: Сохраняет объект изображения в файл.
*   `Photo.resize(image, width: int, height: int)`: Изменяет размер изображения.
*   `Photo.rotate(image, angle: int, expand: bool = true)`: Поворачивает изображение.
*   `Photo.grayscale(image)`: Преобразует изображение в оттенки серого.
*   `Photo.blur(image, radius: int = 2)`: Применяет фильтр размытия.
*   `Photo.size(image)`: Возвращает кортеж `(ширина, высота)`.
*   `Photo.add_watermark(image, text: str, position: tuple, color: tuple, size: int)`: Добавляет текстовый водяной знак.

## Пример использования в Dark

```dark
import "Photo"

my_image = Photo.open("D:/images/cat.jpg")
watermarked_image = Photo.add_watermark(my_image, "My Cat", (20, 20), (255, 0, 0), 50)

Photo.save(watermarked_image, "D:/images/cat_with_watermark.png")
```
