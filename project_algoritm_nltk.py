import nltk

# Fazer o download novamente dos pacotes
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

from nltk import word_tokenize
from nltk.tag import pos_tag

# Exemplo de letras de músicas
letras = ['Felicidade é viver na sua companhia', 
          'Vagando triste por sobre a flor', 
          'Hoje eu acordei feliz, sonhei com ela a noite inteira']

# Função para tokenizar e realizar a classificação gramatical
def classificar_gramaticalmente(texto):
    # Tokenizar o texto em palavras
    palavras_tokenizadas = word_tokenize(texto)
    # Fazer a anotação gramatical
    classificacao = pos_tag(palavras_tokenizadas)
    return classificacao

# Aplicando a função nas letras
for letra in letras:
    print(f"Frase: {letra}")
    print("Classificação gramatical:", classificar_gramaticalmente(letra))
    print()
