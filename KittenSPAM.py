import time
import os
from telethon import *
from termcolor import cprint, colored
os.system('cls' if os.name == 'nt' else 'clear')

cprint(
    '██╗░░██╗██╗████████╗████████╗███████╗███╗░░██╗\n'
    '██║░██╔╝██║╚══██╔══╝╚══██╔══╝██╔════╝████╗░██║\n'
    '█████═╝░██║░░░██║░░░░░░██║░░░█████╗░░██╔██╗██║\n'
    '██╔═██╗░██║░░░██║░░░░░░██║░░░██╔══╝░░██║╚████║\n'
    '██║░╚██╗██║░░░██║░░░░░░██║░░░███████╗██║░╚███║\n'
    '╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝\n',
    'green',
    attrs=['bold', 'blink']
)

cprint(
    '████████╗░██████╗░░██████╗██████╗░░█████╗░███╗░░░███╗\n'
    '╚══██╔══╝██╔════╝░██╔════╝██╔══██╗██╔══██╗████╗░████║\n'
    '░░░██║░░░██║░░██╗░╚█████╗░██████╔╝███████║██╔████╔██║\n'
    '░░░██║░░░██║░░╚██╗░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║\n'
    '░░░██║░░░╚██████╔╝██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║\n'
    '░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝\n',
    'green',
    attrs=['bold', 'blink']
)



try:
    with open('api_file.txt', 'r', encoding='utf8') as api_file:
        api_list = api_file.readlines()
        api_id, api_hash = int(api_list[0].replace('\n', '')), api_list[1].replace('\n', '')
        phone = api_list[2].replace('\n', '')
        api_file.close()
        print(f'API ID: {api_id}, API HASH: {api_hash}, PHONE: +{phone}')
        cprint('API прочитан из файла', 'light_green')
except FileNotFoundError:

    cprint(f'Чтобы узнать api_id и api_hash:'
           f'\n'
           f'Перейдите по ссылке '
           f'{colored("https://my.telegram.org/auth?to=apps", 'light_yellow')}\n'
           +
           colored(f'Войдите в тг аккаунт и создайте новое приложение\n'
                   f'Скопируйте api_id и api_hash\n', 'light_green'), 'light_green')

    api_id = int(input(colored('Введите ваш api_id: ', 'light_yellow')))
    api_hash = input(colored('Введите ваш api_hash: : ', 'light_yellow'))
    phone = input(colored('Введите ваш телефон(Без +): ', 'light_yellow'))
    with open('api_file.txt', 'w', encoding='utf8') as api_file:
        api_list = [str(api_id), '\n', api_hash, '\n', phone]
        api_file.writelines(api_list)
        api_file.close()

try:
    client = TelegramClient('user.session', api_id, api_hash)

    client.start(phone=str(phone))
except Exception as e:
    quit(cprint(f'Ошибка запуска: {e}', 'red', attrs=['bold', 'blink']))


async def start():
    await client.send_message('me', 'Клиент запущен')


try:
    client.loop.run_until_complete(start())
except Exception as e:
    quit(cprint(f'Ошибка запуска: {e}', 'red', attrs=['bold', 'blink']))


to_spam_ids = input(colored("Введите username/ссылки на пользователей/чаты(разделяя ;;): ",
                            'light_yellow')).split(';;')
to_spam_message = input(colored('Введите сообщение(Для переноса строк используйте ;;): ', 'light_yellow')).replace(';;', '\n')
to_spam_count = input(colored('Введите кол-во сообщений: ', 'light_yellow'))
to_spam_delay = input(colored('Введите задержку в секундах(> 0.001): ', 'light_yellow'))


try:
    to_spam_delay = float(to_spam_delay)
    to_spam_count = int(to_spam_count)
except Exception as e:
    quit(cprint(f'Ошибка: {e}', 'red', attrs=['bold', 'blink']))


async def spam(cnt):
    for i in range(cnt):
        for self_id in to_spam_ids:
            await client.send_message(self_id, to_spam_message)
        time.sleep(to_spam_delay)


client.loop.run_until_complete(spam(to_spam_count))
cprint(f'\nЗавершено без ошибок: {client.loop.run_until_complete(client.get_me()).id}', 'green', attrs=['bold', 'blink'])
