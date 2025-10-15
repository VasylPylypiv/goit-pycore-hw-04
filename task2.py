from pathlib import Path

def get_cats_info(path):
    try:
        file_path = Path(path)
        with file_path.open("r", encoding="utf-8") as file:
            info = []
            for line in file:
                if line.strip():    
                    try:
                        id, name, age = line.strip().split(',')
                        info.append({'id': id, 'name': name, 'age': age})
                    except ValueError:
                        print(f"Невірний формат даних у рядку: {line}")                    
                        continue

            return info
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return None 
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None
    
        
cats_info = get_cats_info("cats.txt")
print(cats_info)
