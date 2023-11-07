"""
zip_module: Модуль для работы с ZIP-архивами.

Предоставляет функциональность для создания, извлечения, добавления и просмотра содержимого ZIP-архивов.
"""

import zipfile


def create_zip(source_files, output_filename):
    """
    Создает ZIP-архив из указанных файлов.

    Parameters:
    source_files (list of str): Список путей к файлам для добавления в архив.
    output_filename (str): Имя создаваемого ZIP-архива.

    Returns:
    bool: True при успешном создании архива, иначе False.
    """
    try:
        with zipfile.ZipFile(output_filename, 'w') as zipf:
            for file in source_files:
                zipf.write(file)
        return True
    except Exception as e:
        print(f"Ошибка при создании ZIP-архива: {e}")
        return False


def extract_zip(zip_filename, output_dir):
    """
    Извлекает все файлы из ZIP-архива.

    Parameters:
    zip_filename (str): Путь к ZIP-архиву.
    output_dir (str): Директория, в которую будут извлечены файлы.

    Returns:
    bool: True при успешной распаковке архива, иначе False.
    """
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(output_dir)
        return True
    except Exception as e:
        print(f"Ошибка при извлечении файлов из ZIP-архива: {e}")
        return False


def add_file_to_zip(zip_filename, file):
    """
    Добавляет файл в существующий ZIP-архив.

    Parameters:
    zip_filename (str): Путь к ZIP-архиву.
    file (str): Путь к файлу, который нужно добавить.

    Returns:
    bool: True если файл успешно добавлен, иначе False.
    """
    try:
        with zipfile.ZipFile(zip_filename, 'a') as zipf:
            zipf.write(file)
        return True
    except Exception as e:
        print(f"Ошибка при добавлении файла в ZIP-архив: {e}")
        return False


def list_files_in_zip(zip_filename):
    """
    Отображает список файлов, содержащихся в ZIP-архиве.

    Parameters:
    zip_filename (str): Путь к ZIP-архиву.

    Returns:
    list of str or None: Список файлов в архиве или None в случае ошибки.
    """
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            return zipf.namelist()
    except Exception as e:
        print(f"Ошибка при получении списка файлов из ZIP-архива: {e}")
        return None
