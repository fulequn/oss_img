"""
按照年份将图片文件分类到相应的文件夹中。我们将根据图片文件名中的时间戳来判断年份，并将图片文件移动到相应的文件夹中。
"""
import os
import re
from shutil import move


def create_folder_if_not_exists(directory):
    """创建文件夹，如果不存在"""
    if not os.path.exists(directory):
        os.makedirs(directory)


def organize_images_by_year(base_directory, year):
    """
    按年份将图片分类到相应的文件夹中。

    :param base_directory: 包含图片文件的基目录
    :param year: 要分类的图片的年份
    """
    # 正则表达式匹配图片文件名
    pattern = re.compile(rf'{year}\d{{10}}\.(png|jpg|svg)')

    folder_prefix = 1
    img_count = 0
    for root, _, files in os.walk(base_directory):
        for file_name in files:
            if pattern.match(file_name):
                if img_count % 1000 == 0:
                    folder_name = f'img{str(year)[-2:]}{folder_prefix}'
                    folder_path = os.path.join(base_directory, folder_name)
                    create_folder_if_not_exists(folder_path)
                    folder_prefix += 1
                img_count += 1
                src_path = os.path.join(root, file_name)
                dest_path = os.path.join(folder_path, file_name)
                move(src_path, dest_path)
                print(f'Moved {src_path} to {dest_path}')


if __name__ == "__main__":
    base_directory = 'D:\\workspace\\picture\\oss_img'  # 替换为你的图片文件所在目录
    year = 2022  # 替换为你需要处理的年份
    organize_images_by_year(base_directory, year)
