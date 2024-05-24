import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Hello, how are you? I hope you're finding this tutorial helpful."
tokens = word_tokenize(text)
print(tokens)

#stopwords
'''
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

filtered_sentence = [word for word in tokens if not word in stop_words]
print(filtered_sentence)

'''

#Stemming + lemmatizacion
'''
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(word) for word in filtered_sentence]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_sentence]

print("Stemmed:", stemmed_words)
print("Lemmatized:", lemmatized_words)

'''
#vectorizacion
'''from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform([text])

print(vectorizer.get_feature_names_out())
print(X.toarray())'''

