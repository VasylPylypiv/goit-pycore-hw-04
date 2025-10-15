from pathlib import Path

def total_salary(path):
    try:
        file_path = Path(path)
        if not file_path.exists():
            print(f"{file_path} не існує")
            return 0,0
        
        with file_path.open("r", encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salary = int(salary)
                    total += salary
                    count += 1
                except ValueError:
                    print("Невірний формат даних у рядку: {line}")
                    continue
            if count > 0:
                average = total/count
            else:
                average = 0

            return total, average           
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return 0,0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0,0

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

