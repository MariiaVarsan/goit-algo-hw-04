with open("cats_file.txt", "w", encoding="utf-8") as cats:
    cats.write("""60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5""")

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    cat_data = line.strip().split(',')
                    cat_info = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка під час обробки файлу: {e}")
    return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
