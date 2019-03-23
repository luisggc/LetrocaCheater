# Gerador de Combinações de Palavras

Esse script gera todas as combinações de palavras em português para uma combinação de letras e digita pressionando enter entre as palavras.

## Passos:

1. Clonar ou fazer download do código
2. Pelo terminal/cmd acessar a pasta e executar o arquivo index.py como administrador (sudo python index.py)
3. Digitar as letras a serem combinadas
4. Ir para um editor de texto e pressionar "ENTER"

## Dependências:

É necessário ter o python instalado e as seguintes bibliotecas: unidecode, pyautogui e keyboard
```
pip install unidecode pyautogui keyboard
```

## Usos:

Pode ser usado em jogos relacionado a adivinhação de palavras embaralhadas como letroca.

## Exemplo:

- Digitamos "arrco"
- Vamos a um editor de texto qualquer
- Pressionamos "ESC"
- Automaticamente serão digitados todas as palavras que possuem essas letras combinadas baseada no arquivo "dict.pkl" que é criado a partir do "create_dic.py" que lê o arquivo "palavras.txt".

Resultado:
rocar
carro
corar
corra
racor
orcar
ocra
orar
arco
caro
arro
raro
coar
carr
ocar
roca
corr
acro
acor
cora
croa
orca
aro
car
aco
rac
cao
cor
cra
cro
roa
coa
ora
ror
oca
ra
ac
ro
cr
ca
rr
co
oc
ar
or
oa
ao
o
c
r
a

