---
title: Question Parse
---
## Introduction

This doc gives a high level overview of <SwmPath>[interpretation/assistant/Question_Parse.py](/interpretation/assistant/Question_Parse.py)</SwmPath>. It is a helper file that is functions as a helper file to determine questions in a query.

## Main features

The main features of the file are are:

- <SwmToken path="/interpretation/assistant/Question_Parse.py" pos="14:2:4" line-data="def Is_Question(sentence):">`Is_Question(sentence`</SwmToken>)
- <SwmToken path="/interpretation/assistant/Question_Parse.py" pos="35:2:4" line-data="def Test_Is_Question(sentence):">`Test_Is_Question(sentence`</SwmToken>)

## <SwmToken path="/interpretation/assistant/Question_Parse.py" pos="14:2:4" line-data="def Is_Question(sentence):">`Is_Question(sentence`</SwmToken>)

This function uses python's NLTK to tokenize a sentence it takes (in this case a query), to determine if there is a question in it, returning true if there is.

<SwmSnippet path="/interpretation/assistant/Question_Parse.py" line="14">

---

Function Definition

```python
def Is_Question(sentence):
    
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
```

---

</SwmSnippet>

## <SwmToken path="/interpretation/assistant/Question_Parse.py" pos="35:2:4" line-data="def Test_Is_Question(sentence):">`Test_Is_Question(sentence`</SwmToken>)

This function is a test function used to determine questions. It uses <SwmToken path="/interpretation/assistant/Question_Parse.py" pos="14:2:4" line-data="def Is_Question(sentence):">`Is_Question(sentence`</SwmToken>) as a baseline.&nbsp;

<SwmSnippet path="/interpretation/assistant/Question_Parse.py" line="35">

---

Function Definition

```python
def Test_Is_Question(sentence):
    if Is_Question(sentence):
        print(f"'{sentence}' is a question.")
    else:
        print(f"'{sentence}' is not a question.")
```

---

</SwmSnippet>

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
