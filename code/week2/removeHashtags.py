import re


def remove_hashtags(text):
    pattern = r"#\w+"
    replaced_text = re.sub(pattern, "", text)
    removed_hashtags = re.findall(pattern, text)

    with open("hashtags.txt", "w") as file:
        file.write("\n".join(removed_hashtags))

    return replaced_text


# Example usage
text_with_hashtags = "Check out this #awesome #website #coding #python"
clean_text = remove_hashtags(text_with_hashtags)
print(clean_text)
