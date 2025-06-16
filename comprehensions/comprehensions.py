def get_words(filename):
    """Read words from a text file and return them as a list."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            # Split content into words
            words = content.split()
            # Remove punctuation from words
            cleaned_words = []
            for word in words:
                cleaned_word = ""
                for char in word:
                    if char.isalpha():
                        cleaned_word += char
                if cleaned_word:  # Only add non-empty words
                    cleaned_words.append(cleaned_word)
            return cleaned_words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


def save_counts(counts):
    """Save word counts to a CSV file."""
    try:
        with open("word_counts.csv", "w") as file:
            file.write("Word,Count\n")  # CSV header
            for word, count in counts.items():
                file.write(f"{word},{count}\n")
        print("Word counts saved to 'word_counts.csv'")
    except Exception as e:
        print(f"Error saving file: {e}")


def main():
    # get the address.txt file and extract the words content from it
    words = get_words("address.txt")
    # list comprehension
    lowercase_words = [word.lower() for word in words if len(word) > 4]
    # dictionary comprehension
    counts = {word: lowercase_words.count(word) for word in lowercase_words}
    # create a csv file and write the counts content on it
    save_counts(counts)


main()
