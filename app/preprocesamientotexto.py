import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Hello, how are you? I hope you're finding this tutorial helpful.")

# Tokenización y Lemmatización
print([(token.text, token.lemma_) for token in doc])

# Eliminación de Stop Words y Puntuación
filtered_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
print(filtered_tokens)