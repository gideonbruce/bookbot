def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            words = content.split()

            return len(words)

    except FileNotFoundError:
        print(f"The file {filename} was not found")
        return 0

def count_character_occurrences(text):
    character_counts = {}

    text = text.lower()

    for character in text:
        if character.isalpha():
            if character in character_counts:
                character_counts[character] += 1

            else:
                character_counts[character] = 1

    sorted_character_counts = dict(sorted(character_counts.items(), key=lambda item: item[1], reverse=True))

    return sorted_character_counts

filename = "books/frankenstein.txt"

word_count = count_words_in_file(filename)
print(f"The file '{filename}' contains {word_count} words.")

try: 
    with open (filename, 'r') as file:
        content = file.read()

    character_counts = count_character_occurrences(content)
    print("Character occurences in the file:")
    for character, count in character_counts.items():
        print(f"The '{character}' character was found {count} times")

except FileNotFoundError:
    print(f"'{filename}' does not exist")