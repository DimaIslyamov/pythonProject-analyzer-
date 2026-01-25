
with open("raw_data.txt", "w") as f:
    for i in ["", "10", "abc", "", "25", "??", "40"]:
        f.write(i + "\n")


def clean_numbers(input_file, output_file):
    quantity = {
        "written": 0,
        "skipped": 0
    }

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:

            for line in infile:
                line = line.strip()

                if not line:
                    quantity["skipped"] += 1
                    continue

                try:
                    number = int(line)
                except ValueError:
                    quantity["skipped"] += 1
                    continue

                outfile.write(f"{number}\n")
                quantity["written"] += 1

    except FileNotFoundError:
        return "File not found"

    return quantity


print(clean_numbers("raw_data.txt", "raw_data_new.txt"))