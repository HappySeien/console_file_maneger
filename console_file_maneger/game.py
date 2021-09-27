import random

def number_game():
    number = random.randint(1, 100)
    #print(number)
    print('Игра "угадай число" \n Вам загаданно число от 1 до 100')
    user_answer = None
    user_count = int(input('Укажите количество игроков: '))
    users = []

    for i in range(user_count):
        user_name = input(f'Введите имя игрока {i+1}: ')
        users.append(user_name)
    print(f'В игре учавствуют {",".join(users)}')

    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    level = int(input('Уровни сложности: \n'
                      '1 уровень = 10 попыток, '
                      '2 уровень = 5 попыток, '
                      '3 уровень = 3 попыткии \n'
                      'Выберите уровень сложности: '))
    max_count = levels[level]

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('Вcе игроки проиграли!\n'
                  'Правлильный ответ:', number)
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход игрока {user}')
            user_answer = int(input('Введите число: '))
            if number == user_answer:
                is_winner = True
                winner_name = user
                break
            elif number > user_answer:
                print('Ваше число меньше загаданного')
            else:
                print('Ваше число больше загаданного')
    else:
        print(f'Число угаданно! \nПоздравляем игрока {winner_name} вы победили!')


if __name__ == '__main__':
    number_game()