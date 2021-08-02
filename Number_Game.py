#Написать игру угодай число
import random

#Игра угодай число

print(' Привет , давай сыграем в игру')
print('Я загадал число,от 1 до 10 попробуй его отгодать, у тебя есть 3 попытки')
print('Введите число: ')

texte_one = 'меньше'
text_free = 'больше'
note = 'Вы не отгодали, '
texte_two = 'Осталось попыток: '
text_winner = 'Поздравляем!!!! Вы угодали это число '

plaery = int(input())
komputer = int(random.randrange(1,10))
i = 3

while i != 1:
    i -= 1
    print('Ваше число: ' , str(plaery))
    if plaery > 10:
        print('Вы ввели не провельную цыфру')
        print('Повторите ввод')
        plaery = int(input())
        continue
    else:
        if plaery > komputer:
            print(note, texte_one)
            print(texte_two, str(i))
            plaery = int(input())
        if plaery < komputer:
            print(note, text_free)
            print(texte_two, str(i))
            plaery = int(input())
        if plaery == komputer:
            print(text_winner, str(komputer))
            break
else:
    print('Вы не угодали число. Ваше число: ' , str(plaery) , '. Число которое загодал я: ' , str(komputer))
input('\n\nТы выграл. Нажми Enter, чтобы выйти')
