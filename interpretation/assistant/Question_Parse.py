import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Question parsing ------------------------------------------------------------
# This file contains functions to determine if a sentence is a question and miscellaneous functions related to question parsing.
# ------------------------------------------------------------------------------

def is_question(sentence):
    
    # Tokenize and tag
    words = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    
    # Define question words
    question_words = set(["what", "when", "where", "who", "whom", "which", "whose", "why", "how"])
    
    if sentence.strip().endswith('?'):
        return True
    if words[0].lower() in question_words:
        return True
    
    # Check for auxiliary verbs at the beginning of the sentence
    auxiliary_verbs = set(["is", "are", "am", "was", "were", "do", "does", "did", "has", "have", "had", "will", "would", "shall", "should", "can", "could", "may", "might", "must"])
    if words[0].lower() in auxiliary_verbs:
        return True
    
    return False

def test_is_question(sentence):
    if is_question(sentence):
        print(f"'{sentence}' is a question.")
    else:
        print(f"'{sentence}' is not a question.")
