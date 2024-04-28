import re
from collections import Counter

def word_frequency(file_path, n=10):
    # Define common stop words
    stop_words = {"a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "for", "with", "by", "from"}

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Remove punctuation and split text into words
    words = re.findall(r'\b\w+\b', text)

    # Filter out stop words
    words = [word for word in words if word not in stop_words]

    # Count word frequencies
    word_counts = Counter(words)

    # Display the top N most frequent words
    print(f"Top {n} most frequent words:")
    for word, count in word_counts.most_common(n):
        print(f"{word}: {count}")

# Example usage:
word_frequency("sample_text.txt", n=10)