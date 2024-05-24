from textblob import TextBlob

# Ejemplo de texto
text = "I love this car. It handles amazingly well."

# Crear un objeto TextBlob
blob = TextBlob(text)

# Obtener el análisis de sentimientos
sentiment = blob.sentiment

print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
# Polarity varía de -1 (muy negativo) a 1 (muy positivo)
# Subjectivity varía de 0 (muy objetivo) a 1 (muy subjetivo)
