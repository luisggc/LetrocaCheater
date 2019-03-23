import pickle
import unidecode

ENTRADA = 'palavras.txt'
palavras = set()

with open(ENTRADA, encoding='utf-8') as entrada:
    for i, linha in enumerate(entrada):
        palavras.add(unidecode.unidecode(linha[0:len(linha)-1]).lower())  # para evitar palavra vazia


def words_combinations(letters):
    for n in range(1, len(letters)+1):
        yield from map(''.join, permutations(letters, n))


pickle.dump(palavras, open('dict.pkl', 'wb'))