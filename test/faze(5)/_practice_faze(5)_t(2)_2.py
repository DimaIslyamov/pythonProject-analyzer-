# Нужно написать функцию analyze_log(filename), которая:        # Ограничения:
# Требования:                                                   # Использовать with
# - Пытается открыть файл                                       # Использовать try / except
# - Читает файл построчно                                       # Не использовать print внутри функции
# Для каждой строки:                                            # Если файл не найден → вернуть строку "File not found"
    # - берёт первое слово (INFO, ERROR, WARNING)               # Если строка пустая или странная → просто пропустить её
# - Считает количество строк каждого типа
# Возвращает, словарь вида:
#                           {
#                               "INFO": 2,
#                               "ERROR": 2,
#                               "WARNING": 1
#                           }


# def analyze_log(filename):
#     total_info = 0
#     total_error = 0
#     total_warning = 0
#
#     stats = {"INFO": total_info,
#              "ERROR": total_error,
#              "WARNING": total_warning}
#     try:
#         with open(filename) as f:
#             for line in f:
#                 line = line.strip()
#                 if not line:
#                     continue
#
#                 elif line.startswith("INFO"):
#                     total_info += 1
#                     stats["INFO"] = total_info
#
#                 elif line.startswith("ERROR"):
#                     total_error += 1
#                     stats["ERROR"] = total_error
#
#                 elif line.startswith("WARNING"):
#                     total_warning += 1
#                     stats["WARNING"] = total_warning
#
#
#     except FileNotFoundError:
#         return "File not found"
#     return stats
#
#


 # Минимально оптимизированный вариант (очень важный)\
def analyze_log(filename):
    stats = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                level = line.split()[0]

                if level in stats:
                    stats[level] += 1

    except FileNotFoundError:
        return "File not found"

    return stats


context = analyze_log("log.txt")
for key, value in context.items():
    print(f"{key} : {value}")