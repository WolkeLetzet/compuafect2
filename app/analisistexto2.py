from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Cargar el tokenizador y el modelo
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Crear un pipeline de análisis de sentimientos
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
# Texto en español
text = "Estoy muy feliz de aprender sobre análisis de sentimientos."

# Realizar el análisis de sentimientos
result = nlp(text)
print(result)
