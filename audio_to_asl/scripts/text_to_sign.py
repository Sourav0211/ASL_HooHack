import re

# Define rules for converting text to a simplified sign language grammar
def convert_to_sign_grammar(text):
    """
    Converts English text into a simplified Sign Language grammar format.
    """
    # Common words to remove (articles, auxiliary verbs, prepositions)
    remove_words = {"is", "are", "was", "were", "am", "the", "a", "an", "to"}

    # Tokenize and filter unnecessary words
    words = text.lower().split()
    filtered_words = [word for word in words if word not in remove_words]

    # Reorder structure (Basic Topic-Comment structure for ASL)
    if len(filtered_words) > 1:
        filtered_words.append(filtered_words.pop(0))  # Move subject to the end

    return " ".join(filtered_words).upper()  # Convert to uppercase

if __name__ == "__main__":
    sample_text = "I am going to the store."
    sign_sentence = convert_to_sign_grammar(sample_text)
    print("Converted Sign Language Sentence:", sign_sentence)
