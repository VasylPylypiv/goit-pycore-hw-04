import sys
from pathlib import Path
from colorama import Fore



# Створення об'єкту Path для директорії
directory = Path(sys.argv[1] if len(sys.argv) > 1 else '.')

# Функція для рекурсивного оброблення директорії
def directory_walk(directory, indent=""):
    # Отримуємо всі елементи в директорії, включаючи файли та папки
    # Сортуємо їх разом по алфавіту
    for path in sorted(directory.iterdir(), key=lambda p: p.name.lower()):
        # Виводимо елементи з відступом
        if path.is_dir():
            print(Fore.BLUE + indent + path.name + "/")  # додаємо "/ " для директорій
            # Рекурсивно обробляємо підкаталоги з додатковим відступом
            directory_walk(path, indent + "    ")  # додаємо 4 пробіли для кожного рівня
        else:
            print(Fore.GREEN + indent + path.name)  # Виводимо лише ім'я файлу

# Виведення назви кореневої директорії на початку
print(Fore.BLUE + directory.name + "/")

# Викликаємо функцію для виведення структури директорії
directory_walk(directory, indent="    ")