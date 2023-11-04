import re
# Tanat Arora
# 6410381


def remove_coursecode(code):
    pattern = r"\b[A-Z]{2,3}\d{4}\b"
    replaced_code = re.sub(pattern, "", code)
    removed_code = re.findall(pattern, code)

    with open("courseCode.txt", "w") as file:
        file.write("\n".join(removed_code))

    return replaced_code


# Example usage
text_with_code = "So I have got this course code which are CSX3001 and ITX3002"
clean_code = remove_coursecode(text_with_code)
print(clean_code)
