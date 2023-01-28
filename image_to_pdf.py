from PIL import Image
import os
from pathlib import Path

image_list = []
im_1 = None
image_dir = input("Каталог изображений: ")

if os.path.isdir(image_dir):  # проверяет наличие пути
    for root, dirs, files in os.walk(image_dir):  # проход файлов
        for image_name in files:
            if image_name == files[0]:
                im_1 = Image.open(Path(image_dir).joinpath(image_name))
            else:
                image_list.append(Image.open(Path(image_dir).joinpath(image_name)))  # формирование списка
    im_1.save(Path(image_dir).joinpath("out.pdf"), save_all=True, append_images=image_list)  # сохраняем pdf
else:
    print("Каталог не найден")
