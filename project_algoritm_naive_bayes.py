from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Exemplo de dataset
letras = ['Felicidade é viver na sua companhia', #feliz(0)
          'Vagando triste por sobre a flor', #triste(1)
          'Hoje eu acordei feliz, sonhei com ela a noite inteira', #feliz(0)
          'Saudade, palavra triste quando se perde um grande amor', #triste(1)
          'Sou feliz, alegre e forte, tenho amor e sorte', #feliz(0)
          'E quando vem a lucidez, estou sozinho outra vez', #triste(1)
          'É amor, felicidade transbordando em mim', #feliz(0)
          'Ai, meu Deus, eu vou morrer sozinho, se eu continuar nesse caminho', #triste(1)
          'A felicidade então nos sorriu', #feliz(0)
          'E eu sei que chora, não finge que não viveu toda nossa história', #triste(1)
          'Estamos, meu bem, por um triz, pro dia nascer feliz', #feliz(0)
          'Porque não haverá luz do Sol, se eu te perder, amor', #triste(1)
          'Alegria, deixa invadir e transbordar seu coração com boas energias', #feliz(0)
          'Peito machucado, lágrimas caídas pelo chão', #triste(1)
          'Eu quero que a vida seja feita de alegria', #feliz(0)
          'Solidão, quando uma luz se apaga, eu de novo em casa, morrendo de amor por ela', #triste(1)
          'É felicidade que explodiu, todo mundo entende, tá muito evidente', #feliz(0)
          'Por que você não cola em mim? Tô me sentindo muito sozinho', #triste(1)
          'Porque estou feliz, bata palmas se sentir que a felicidade é a verdade', #feliz(0)
          'Mas por trás do celular ainda dói, ainda dói', #triste (1)
          'Olha o meu sorriso de felicidade, veja o nosso mundo de sinceridade', #feliz(0)
          'Não ouvir o coração, desse jeito a gente pede pra sofrer', #triste(1)
          'Eu te vi, já te quis, me vi tão feliz', #feliz(0)
          'Nem me dei conta o tanto que chorei', #triste(1)
          'Esse riso cristalino de alegria', #feliz(0)
          'Lágrimas que invadem meu coração', #triste(1)
          'Agora que voltou, sorri, sou rei', #feliz(0)
          'Coração magoado, amou e não foi amado, sofre todo dia, porque fui enganado', #triste(1)
          'O Sol nas bancas de revista me enche de alegria e preguiça', #feliz(0)
          'É dor que não passa nunca mais, são coisas de anos atrás e eu continuo chorando por ela', #triste(1)
          'Gosto muito de te ver leãozinho', #feliz(0)
          'Já não sinto pena, só dói as feridas', #triste(1)
          'Chegou, chegou, tá na hora da alegria', #feliz(0)
          'E os dias quentes são tão frios e as noites me trazem a dor desse amor', #triste(1)
          'Terminar gostando, dói, dói, dói demais', #triste(1)
          'Eu não quero ser triste pra sempre', #triste(1)
          'Dói sem tanto te lembrar', #triste(1)
          'Dói ter que controlar a vontade doida de te ligar', #triste(1)
          'Eu sou daqueles que chora e cai quando cê não quer mais' #triste(1)
          ] 

#categorias correspondentes (0 para feliz e 1 para triste)"
categorias = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]

# Vetorização dos textos
vetorizador = CountVectorizer()
X = vetorizador.fit_transform(letras)

# Dividir os dados em treino e teste
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, categorias, test_size=0.3, random_state=42)

# Treinar o classificador Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_treinamento, y_treinamento)

# Fazer previsões
previsoes = modelo.predict(X_teste)
precisao = accuracy_score(y_teste, previsoes)
report = classification_report(y_teste, previsoes)

# Avaliar o modelo
print(f"Precisão do modelo: {precisao:.2f}")
print("Relatório de Classificação:\n", report)

# Testar nova música
nova_letra = ["Estou sozinha"]
nova_letra_transformada = vetorizador.transform(nova_letra)
previsao_nova_letra = modelo.predict(nova_letra_transformada)

if previsao_nova_letra[0] == 0:
    print("A frase é positiva.")
else:
    print("A frase é negativa.")