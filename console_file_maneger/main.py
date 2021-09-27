import core
import sys
import game

core.save_info('Запуск программы')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. \n'
          'со списком команд мажно ознакомиться с помошью help')
else:
    if command == 'list':
        core.get_list()

    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            core.create_file(name)

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            core.create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            core.delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует название файла, или не указанно новое имя файла')
        else:
            core.copy_file(name, new_name)

    elif command == 'cd':
        try:
            path = sys.argv[2]
        except IndexError:
            print('Укажите имя папки для перехода')
        else:
            core.chdir(path)

    elif command == 'game':
        game.number_game()

    elif command == 'help':
        print('help: ')
        print('list - список файлов и папок, f если отобразить только папки \n'
              'create_file - Создание файла \n'
              'create_folder - Создание папки \n'
              'delete - Удаление файла, папки \n'
              'copy "name" "new_name" - копирование файла, папки'
              'cd "name" - смена директории'
              'game - запустить игру "угадай число"')


core.save_info('Закрытие программы')
