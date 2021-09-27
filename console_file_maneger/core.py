import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf8') as f:
        if text:
            f.write(text)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
    else:
        shutil.copy(name, new_name)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def get_list(folders_only=False):
    rez = os.listdir()
    if folders_only:
        rez = [f for f in rez if os.path.isdir(f)]
    print(rez)


def save_info(message):
    current_tyme = datetime.datetime.now()
    rez = f'{current_tyme} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(rez + '\n')


def chdir(path):
    os.chdir(path)
    print(os.getcwd())


if __name__ == '__main__':
    # create_file('test.dat')
    # create_file('test.dat', 'some text')
    # create_folder('new_f')
    # get_list(True)
    # get_list()
    # delete_file('new2')
    # delete_file('test.dat')
    # copy_file('new_f', 'new2')
    save_info('abc')
