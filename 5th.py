def count_words(file_path):
    result= {}
    with open(file_path, "r") as file:
        lines = file.readlines()
        line_number = 1
        for line in lines:
            words = len(line.split())
            result[f"Line {line_number}"] = words
            line_number += 1
    return result


file = "5th_example.txt"
x = count_words(file)
print(x)
