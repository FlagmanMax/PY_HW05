#  Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def disassamble_path(path:str):
    *path, file = path.split("\\")
    name, extension = file.split(".")
    return (path, name, extension)

path = "c:\Work\!GB\Python\Seminar\Hw_01.py"
print(path)

(path, name, extension) = disassamble_path(path)
print(f"File path:\t\t\t{'/'.join(path)}\nFile name:\t\t\t{name}\nFile expansion:\t\t{extension}\n")

