
# Мини-задание (Фаза 5 — Тема 3)

# Условие:
#   Напиши функцию read_first_line(filename), которая:
#   Пытается открыть файл
#   Читает, только первую строку
#   Возвращает её (без \n)

# Если файл:
#   не существует → вернуть "File not found"
#   пустой → вернуть "Empty file"

# ❗ Использовать with
# ❗ Использовать try / except
# ❗ Без print внутри функции


# def read_first_line(filename):
#     try:
#         with open(filename) as f:
#             return f.readline().strip()
#
#     except FileNotFoundError:
#         return "File not found"
#
#
# print(read_first_line("data.txt"))


def read_first_line(filename):
    try:
        with open(filename, "r") as f:
            content = f.readline()

            if len(content) == 0:
                return "Empty file"
            else:
                return content[0].strip()


    except FileNotFoundError:
        return "File not found"


print(read_first_line("data.txt"))
print(read_first_line("numbers.txt"))
