import os
from colorama import *
from disc import list_disc

init(autoreset=True)

disc = 'D:\\'
password_name = 'Passwords.txt'
password_for_way = '\Passwords.txt'

if disc in list_disc:
    way_no_file = disc + password_name
elif list_disc == ['C:\\Users']:
    way = []
    for i in os.walk('C:\\Users'):
        for z in i:
            if '\Documents' in z and 'Public' not in z and 'Default' not in z:
                way.append(z)
    way_no_file = way[0] + password_for_way
else:
    way_no_file = list_disc[1] + password_for_way


def writing(site=None, login=None, password_g=None):
    with open(all_way, 'a') as file:
        file.write('\nСайт: ' + site + '\n\n')
        file.write('ЛОГИН: ' + login + '\n')
        file.write('ПАРОЛЬ: ' + password_g + '\n')
    opening()


def opening():
    print(Fore.BLUE + Style.BRIGHT + '\nДобавлен новый пароль:\n')
    with open(all_way) as file:
        for line in file.readlines()[-4:]:
            print(Fore.BLACK + Back.WHITE + Style.BRIGHT + line, end='')
    print(f"\nФайл сохранен в папке {q}\n")


def writing_no_file(site=None, login=None, password_g=None):
    with open(way_no_file, 'a') as file:
        file.write('\nСайт: ' + site + '\n\n')
        file.write('ЛОГИН: ' + login + '\n')
        file.write('ПАРОЛЬ: ' + password_g + '\n')
    opening_no_file()


def opening_no_file():
    print(Fore.BLUE + Style.BRIGHT + '\nДобавлен новый пароль:\n')
    with open(way_no_file) as file:
        for line in file.readlines()[-4:]:
            print(Fore.BLACK + Back.WHITE + Style.BRIGHT + line, end='')
    if disc in list_disc:
        print(f"\nФайл сохранен в папке {disc}\n")
    elif list_disc == ['C:\\Users']:
        print(f"\nФайл сохранен в папке {way[0]}\n")
    elif len(list_disc) >1:
        print(f"\nФайл сохранен в папке {list_disc[1]}\n")


def find_file(site=None, login=None, password_g=None):
    global a, q, all_way
    if list_disc == ['C:\\']:
        for way in os.walk('C:\\'):
            for z in way:
                if password_name in z:
                    a = 'File found'
                    q = (way[0])
                    all_way = q + password_for_way
    else:
        for h in list_disc:
            for way in os.walk(h):
                for z in way:
                    if password_name in z:
                        a = 'File found'
                        q = (way[0])
                        all_way = q + password_for_way
    try:
        if a == 'File found':
            writing(site, login, password_g)
    except NameError:
        writing_no_file(site, login, password_g)
