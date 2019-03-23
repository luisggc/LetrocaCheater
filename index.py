#!/usr/bin/env python3
from itertools import permutations
from pyautogui import press, typewrite, hotkey
import keyboard
import pickle

palavras = pickle.load(open('dict.pkl',"rb"))


def words_combinations(letters):
    for n in range(1, len(letters)+1):
        yield from map(''.join, permutations(letters, n))

def possible_word(letrocaInput):
    answers=[]
    for word in set(words_combinations(letrocaInput)):
        if word in palavras:
            answers.append(word)

    answers.sort(key = lambda s: -len(s))
    return answers

while True:
    print("Pressione ENTER para sair ou")
    letrocaInput=input("Digite as letras possíveis: ")
    if letrocaInput=="":
        break
    print("Pressione ESC para começar")
    keyboard.wait('esc')

    for word in possible_word(letrocaInput):
        typewrite(word, interval=0)
        press('enter')