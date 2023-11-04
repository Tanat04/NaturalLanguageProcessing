import re


def remove_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    replaced_text = re.sub(pattern, "", text)
    removed_emails = re.findall(pattern, text)

    with open("emails.txt", "w") as file:
        file.write("\n".join(removed_emails))

    return replaced_text


# Example usage
text_with_emails = "Contact me at john@example.com or jane.doe@gmail.com or findme@home"
clean_text = remove_emails(text_with_emails)
print(clean_text)
