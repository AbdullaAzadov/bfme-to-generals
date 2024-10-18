import os
import shutil

# Укажите путь к директории с файлами
source_dir = r'C:\Users\113\Desktop\GenData\Art\W3D'

# Перебор файлов в директории
for filename in os.listdir(source_dir):
    prefix = filename[:2]  # Получите первые два символа как префикс
    subdir = os.path.join(source_dir, prefix)  # Создайте путь к подпапке
    os.makedirs(subdir, exist_ok=True)  # Создайте подпапку, если ее нет
    shutil.move(os.path.join(source_dir, filename), os.path.join(subdir, filename))  # Переместите файл