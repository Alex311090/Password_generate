from random import shuffle
from Save_Password import find_file
import string
import secrets
from colorama import *
import time
from progress.spinner import Spinner
from threading import *

init(autoreset=True)

letter_list = string.ascii_letters
simwols_list = string.punctuation

DEF_QTY = 15
dict_pass = {}

print(Fore.CYAN + "Вас приветствует генератор паролей.\nПрограмма создает пароли с возможностью настройки "
                  "сложности\n")
print(
    Fore.CYAN + "Пароль будет создан с настройками по умолчанию:\nДлина пароля: 15\nСпец. символы: нет\n")


def question1():
    global answer_1
    answer_1 = input(Fore.YELLOW + Style.BRIGHT +
                     'Хотите изменить настройки сложности (Изменить длину или включить спец. символы)?\nда/нет: '
                     ).lower()
    if answer_1 == 'нет':
        config_easy(DEF_QTY)
    elif answer_1 == 'да':
        question2()
    else:
        print(Fore.RED + Style.BRIGHT + f"Введены не корректные данные: '{answer_1}', повторите попытку\n")
        question1()


def question2():
    global quantity, simwols
    try:
        quantity = int(input(Fore.YELLOW + Style.BRIGHT + "\nУкажите длину пароля от 6 до 25 символов: "))
        if quantity < 6 or quantity > 25:
            print(
                Fore.RED + Style.BRIGHT + f"Длина пароль должна быть от 6 до 25 символов, вы ввели число: '{quantity}'")
            question2()

        else:
            simwols = input(Fore.YELLOW + Style.BRIGHT + "\nПароль будет содержать спец символы? Да/Нет: ").lower()

    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Введено не число, повторите ввод...")
        question2()

    if simwols == 'да':
        config_hard(quantity)

    elif simwols == 'нет':
        config_easy(quantity)
    else:
        print(Fore.RED + Style.BRIGHT + f"Введены некорректные данные: '{simwols}' , повторите ввод...")
        question2()


def config_easy(qty_all):
    global qty_let, qty_num
    qty_let = round(qty_all * 0.75)
    qty_num = qty_all - qty_let
    generate(qty_let, qty_num)


def config_hard(qty_all):
    global qty_let, qty_num, qty_sim
    qty_let = round(qty_all * 0.55)
    qty_num = round(qty_all * 0.25)
    qty_sim = qty_all - qty_let - qty_num
    generate(qty_let, qty_num, qty_sim)


def generate(let, num, sim=None):
    global pass_create, exit
    pass_create = []
    for n in range(0, let):
        pass_create.append(secrets.choice(letter_list))
    for n in range(0, num):
        pass_create.append(str(secrets.choice(string.digits)))
    if sim is not None:
        for n in range(0, sim):
            pass_create.append(secrets.choice(simwols_list))
    shuffle(pass_create)
    password = (''.join(pass_create))
    save_y_n(password)


def save_y_n(password):
    print(Fore.CYAN + Style.BRIGHT + '\nСгенерирован пароль: ' + Fore.MAGENTA + password)
    save = input(Fore.BLUE + Style.BRIGHT + "\nСохранить пароль? Да/Нет ").lower()
    if save == 'да':
        save_pas(password)
    elif save == 'нет':
        restart()
    else:
        print(Fore.RED + Style.BRIGHT + f"Некорректная команда: '{save}'")
        save_y_n(password)


def save_pas(password=None):
    site = input(Fore.GREEN + "\nВведите название сайта: ")
    login = input(Fore.BLUE + Style.BRIGHT + "Введите логин: ")
    print('')

    def gonka():
        print(Back.CYAN + Style.BRIGHT + "Ожидайте, идет сохранение...")
        with Spinner('Processing...') as bar:
            for i in range(100):
                time.sleep(0.001)
                bar.next()
    p1 = Thread(target=gonka)
    p2 = Thread(target=find_file, args=(site, login, password,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    restart()


def restart():
    exit = input(Fore.YELLOW + Style.BRIGHT + "Повторить генерация? Да/Нет ").lower()
    if exit == 'да':
        question1()
    elif exit == 'нет':
        print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + "Спасибо за использование :-)")
        time.sleep(15)
    else:
        print(Fore.RED + Style.BRIGHT + f"Некорректная команда: '{exit}'\n")
        restart()


question1()