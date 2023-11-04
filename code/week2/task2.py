import re
# Tanat Arora
# 6410381


def remove_urls(text):
    pattern = r"(https?://)?(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z]+)+(/[a-zA-Z0-9-]*)*(\.[a-zA-Z]+)?"
    replaced_text = re.sub(pattern, "", text)
    removed_urls = ["".join(url_tuple)
                    for url_tuple in re.findall(pattern, text)]

    with open("urls.txt", "w") as file:
        file.write("\n".join(removed_urls))

    return replaced_text


def remove_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    replaced_text = re.sub(pattern, "", text)
    removed_emails = re.findall(pattern, text)

    with open("emails.txt", "w") as file:
        file.write("\n".join(removed_emails))

    return replaced_text


def remove_hashtags(text):
    pattern = r"#\w+"
    replaced_text = re.sub(pattern, "", text)
    removed_hashtags = re.findall(pattern, text)

    with open("hashtags.txt", "w") as file:
        file.write("\n".join(removed_hashtags))

    return replaced_text


# Example usage
text_with_urls = "Check out this website: https://www.au.edu/study and this one: http://google.com"
clean_text = remove_urls(text_with_urls)
print("Task 2, Removing the URL: \n" + clean_text)

# Example usage
print()
text_with_emails = "Contact me at john@example.com or jane.doe@gmail.com or findme@home"
clean_text = remove_emails(text_with_emails)
print("Task 2, Removing the Email: \n" + clean_text)

# Example usage
print()
text_with_hashtags = "Check out this #awesome #website #coding #python"
clean_text = remove_hashtags(text_with_hashtags)
print("Task 2, Removing the Hashtags: \n" + clean_text)
