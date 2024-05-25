from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Exemplo de dataset
letras = []

#categorias correspondentes (0 para feliz e 1 para triste)"
categorias = []

# Vetorização dos textos
vetorizador = CountVectorizer()
X = vetorizador.fit_transform(letras)

# Dividir os dados em treino e teste
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, categorias, test_size=0.2, random_state=37)

# Treinar o classificador Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_treinamento, y_treinamento)

# Fazer previsões
previsoes = modelo.predict(X_teste)
precisao = accuracy_score(y_teste, previsoes)
report = classification_report(y_teste, previsoes)
print(X_treinamento)

# Avaliar o modelo
print(f"Precisão do modelo: {precisao:.2f}")
print("Relatório de Classificação:\n", report)