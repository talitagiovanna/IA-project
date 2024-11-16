import spacy

# Carregar o modelo em português
nlp = spacy.load("pt_core_news_lg")

# Exemplo de letras de músicas
letras = ['Felicidade é viver na sua companhia', 
          'Vagando triste por sobre a flor', 
          'Hoje eu acordei feliz, sonhei com ela a noite inteira', 
          'Saudade, palavra triste quando se perde um grande amor',
          'Sou feliz, alegre e forte, tenho amor e sorte', 
          'E quando vem a lucidez, estou sozinho outra vez',
          'É amor, felicidade transbordando em mim', 
          'Ai, meu Deus, eu vou morrer sozinho, se eu continuar nesse caminho', 
          'A felicidade então nos sorriu', 
          'E eu sei que chora, não finge que não viveu toda nossa história',
          'Estamos, meu bem, por um triz, pro dia nascer feliz', 
          'Porque não haverá luz do Sol, se eu te perder, amor', 
          'Alegria, deixa invadir e transbordar seu coração com boas energias',
          'Peito machucado, lágrimas caídas pelo chão', 
          'Eu quero que a vida seja feita de alegria', 
          'Solidão, quando uma luz se apaga, eu de novo em casa, morrendo de amor por ela',
          'É felicidade que explodiu, todo mundo entende, tá muito evidente',
          'Por que você não cola em mim? Tô me sentindo muito sozinho',
          'Porque estou feliz, bata palmas se sentir que a felicidade é a verdade',
          'Mas por trás do celular ainda dói, ainda dói',
          'Olha o meu sorriso de felicidade, veja o nosso mundo de sinceridade',
          'Não ouvir o coração, desse jeito a gente pede pra sofrer',
          'Eu te vi, já te quis, me vi tão feliz',
          'Nem me dei conta o tanto que chorei',
          'Esse riso cristalino de alegria',
          'Lágrimas que invadem meu coração',
          'Agora que voltou, sorri, sou rei',
          'Coração magoado, amou e não foi amado, sofre todo dia, porque fui enganado',
          'O Sol nas bancas de revista me enche de alegria e preguiça',
          'É dor que não passa nunca mais, são coisas de anos atrás e eu continuo chorando por ela',
          'Gosto muito de te ver leãozinho',
          'Já não sinto pena, só dói as feridas',
          'Chegou, chegou, tá na hora da alegria',
          'E os dias quentes são tão frios e as noites me trazem a dor desse amor',
          'Terminar gostando, dói, dói, dói demais',
          'Eu não quero ser triste pra sempre',
          'Dói sem tanto te lembrar',
          'Dói ter que controlar a vontade doida de te ligar',
          'Eu sou daqueles que chora e cai quando cê não quer mais',
          'O seu sorriso vale mais que diamante',
          'Você vai rir sem perceber Felicidade é só questão de ser',
          'Um dia pretendo tentar descobrir porque é mais forte quem sabe mentir',
          'Meu melhor amigo é o meu amor',
          'Me perdi no sorriso nem preciso me encontrar',
          'Meu coração bate ligeiramente apertado',
          'Você partiu meu coração',
          'Estou mal vem me ajudar',
          'Vou tomar conta de você',
          'saudade palavra triste'
          'Hoje eu acordei me veio a falta de você',
          'uma eternidade pra se arrepender',
          'faz uma loucura por mim sai bebendo por ai',
          'A amizade nem mesmo a força do tempo irá destruir',
          'Quero chorar o teu choro quero sorrir seu sorriso',
          'Valeu por você existir amigo',
          'O tempo passou e eu sofri calado'
          ]

# Dicionário de tradução das classificações gramaticais
traducao_pos = {
    "ADJ": "Adjetivo",
    "ADP": "Preposição",
    "ADV": "Advérbio",
    "AUX": "Verbo Auxiliar",
    "CCONJ": "Conjunção Coordenativa",
    "DET": "Determinante",
    "INTJ": "Interjeição",
    "NOUN": "Substantivo",
    "NUM": "Número",
    "PART": "Partícula",
    "PRON": "Pronome",
    "PROPN": "Nome Próprio",
    "PUNCT": "Pontuação",
    "SCONJ": "Conjunção Subordinativa",
    "SYM": "Símbolo",
    "VERB": "Verbo",
    "X": "Outro"
}

# Função para classificar gramaticalmente e traduzir para português
def classificar_gramaticalmente(texto):
    doc = nlp(texto)
    classificacao = [(token.text, traducao_pos.get(token.pos_, token.pos_)) for token in doc]
    return classificacao

# Aplicando a função nas letras e exibindo a classificação
for letra in letras:
    print(f"Frase: {letra}")
    print("Classificação gramatical:", classificar_gramaticalmente(letra))
    print()