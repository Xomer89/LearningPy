# Игра "Анаграммы", где надо отгадать исходное слово по анаграмме



import random

WORDS = ("торговец", "гроза", "видеозапись")

word = random.choice(WORDS)
correct = word
jumble = ""

while word:
    pos = random.randrange(len(word))
    jumble += word[pos]
    word = word[:pos] + word[pos + 1:]

print("""           Добро пожаловать!!!
                ЭТО ИГРА АНАГРАММЫ          """)

print("\nЭто анаграмма: ", jumble)

guess = input("Поробуйте отгадать исходное слово: ")

while guess != correct and guess != "":
    print("\nУвы, Вы ошиблись.")
    guess = input("Попробуйте ещё: ")
if guess == correct:
    print("Вы угадали. Это слово ", guess)
input("\n\nНажмите Enter для выхода")
