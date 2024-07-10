with open("personal_data.txt", "w", encoding="utf-8") as zp:
    zp.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            salaries = [int(line.split(',')[1]) for line in lines]
            total = int(sum(salaries))
            average = int(total / len(salaries)) if salaries else 0
            return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка під час обробки файлу: {e}")
        return None, None

total, average = total_salary('personal_data.txt')

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
