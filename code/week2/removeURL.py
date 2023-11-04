import re


def remove_urls(text):
    pattern = r"(https?://)?(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z]+)+(/[a-zA-Z0-9-]*)*(\.[a-zA-Z]+)?"
    replaced_text = re.sub(pattern, "", text)
    removed_urls = ["".join(url_tuple)
                    for url_tuple in re.findall(pattern, text)]

    with open("urls.txt", "w") as file:
        file.write("\n".join(removed_urls))

    return replaced_text


# Example usage
text_with_urls = "Check out this website: https://www.au.edu.com/study and this one: http://google.com"
clean_text = remove_urls(text_with_urls)
print(clean_text)
