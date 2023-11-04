import re
# Tanat Arora
# 6410381


def remove_urls(text):
    pattern = r"(https?://)?(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z]+)+(/[a-zA-Z0-9-]*)*(\.[a-zA-Z]+)?"
    replaced_text = re.sub(pattern, "", text)
    return replaced_text


def remove_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    replaced_text = re.sub(pattern, "", text)
    return replaced_text


def remove_hashtags(text):
    pattern = r"#\w+"
    replaced_text = re.sub(pattern, "", text)
    return replaced_text


# Example usage
text_with_urls = "Check out this website: https://www.au.edu.com/study and this one: http://google.com"
clean_text = remove_urls(text_with_urls)
print("Task 1, Removing the URL: \n" + clean_text)

# Example usage
print()
text_with_emails = "Contact me at john@example.com or jane.doe@gmail.com or findme@home"
clean_text = remove_emails(text_with_emails)
print("Task 1, Removing the Email: \n" + clean_text)

# Example usage
print()
text_with_hashtags = "Check out this #awesome #website #coding #python"
clean_text = remove_hashtags(text_with_hashtags)
print("Task 1, Removing the Hashtag: \n" + clean_text)
