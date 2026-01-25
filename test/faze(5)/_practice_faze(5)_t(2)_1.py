
# Условие
# Создай файл numbers.txt
# Запиши в него числа от 1 до 5 (каждое с новой строки)

# Затем:
# - прочитай файл
# - посчитай сумму чисел
# - верни сумму из функции sum_from_file(filename)
# ❗ Используй with
# ❗ Обработай ситуацию, если файл не существует
# ❗ Внутри функции — никаких print

# Пример:
    #  print(sum_from_file("numbers.txt"))  # 15


# Мини-задание 2 (Фаза 5)
# Запись файла
with open("numbers.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"{i}\n")


def sum_from_file(filename):
    total = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                total += int(line.strip())
    except FileNotFoundError:
        return "File not found"
    except ValueError:
        return "Invalid file content"
    return total


print(sum_from_file("numbers.txt"))



# Практика — Фаза 5, Тема 2 (Файлы)
with open("scores.txt", "w") as f:
    for i in ["85", "90", "abc", "70", "100"]:
        f.write(f"{i}\n")


def analyze_scores(filename):
    total_count = 0
    total_sum = 0

    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    value = int(line.strip())

                    total_count += 1
                    total_sum += value

                except ValueError:
                    continue

    except FileNotFoundError:
        return "File not found"

    average = total_sum / total_count
    result = {
        "count": total_count,
        "sum": total_sum,
        "average": average
    }

    return result

print(analyze_scores("scores.txt"))
