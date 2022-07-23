import config #In this file, the token variable contains the token of our bot
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executor
from random import randint


class TheBestBotInTheWorld():

    def __init__(self):
        self.token = config.token
        self.bot = Bot(self.token)
        self.dp = Dispatcher(bot=self.bot)

    def start(self):
        @self.dp.message_handler(commands=['start'])
        async def start(messsage: types.Message):
            await messsage.answer('Вас приветствует бот @king_offkaif\n'
                                  'Бот умеет решать распространееные задачи, а также типо посмеяться\n'
                                  'Напишите команду /tasks, для просмотра списка задач\n'
                                  'Напишите команду /mems для того, чтобы умереть от мемов😎\n'
                                  'А кроме этого есть команда /video, которая отправляет\n'
                                  'прикольный видосик, посмотрите🤨\n'
                                  'Команда /information узнает информацию о пользователе\n')

        @self.dp.message_handler(commands=['information'])
        async def information(message):
            await message.answer(f'Я пробил информацию\n\nId чата: {message.chat.id}\n'
                                 f'Id пользователя: {message.from_user.id}\n'
                                 f'Имя: {str(message.from_user.first_name)}\n'
                                 f'Фамилия: {str(message.from_user.last_name)}\n'
                                 f'Псевдоним: {str(message.from_user.username)}\n\n')


        @self.dp.message_handler(commands=['mems'])
        async def memes(message: types.Message):
            with open(f'innopolis_bot_memes\photos\{randint(1, 24)}.jpg', 'rb') as photo:
                await message.answer_photo(photo=photo)

        @self.dp.message_handler(commands=['video'])
        async def memes(message: types.message):
            with open('innopolis_bot_memes\\videos\good_video.mp4', 'rb') as vid:
                await message.answer_video(video=vid)

        @self.dp.message_handler(commands=['tasks'])
        async def tasks(message: types.message):
            await message.answer("Список задач(есть код для них, для подробного разбора задач)\n"
                                 "1)Решето эратосфена /sieve\n"
                                 "2)Последовательноть фибоначчи /fib\n"
                                 "3)Проверка на простое число(является\не является) /easy\n"
                                 "4)Рандомное число от А до В /rand\n"
                                 "5)Сортировать последовательность(ввод осуществляется через пробел) /sorting\n"
                                 "6)Создать список [ 18, 14, 10, 6, 2 ]  с помощью функции range()  /list_range\n"
                                 "7)Перевернуть строчку /reversing\n"
                                 "8)Файловая система /file\n"
                                 "9)Задача на стек /stack\n"
                                 "10)Задача на дек /deq\n"
                                 "11)Полиглоты(словари) /sets\n")

        @self.dp.message_handler(commands='sieve')
        async def sieve(message: types.message):
            await message.answer("Условие задачи:\n"
                                 "Напишите программу,которая принимает на вход число n и выводит количество простых чисел в диапазоне от 2 до n.\n"
                                 "Для нахождения всех простых чисел не больше заданного n, следуя методу Эратосфена, нужно выполнить следующие шаги:\n"
                                 " 1)Выписать подряд все целые числа от 2 до n (2p, 3p, 4p,..., ).\n"
                                 " 2)Пусть переменная p изначально равна 2 — первому простому числу.\n"
                                 " 3)Зачеркнуть в списке числа от 2p до n считая шагами по p (это будут числа кратные p: 2p, 3p, 4p,...).\n"
                                 " 4)Найти первое незачёркнутое число в списке, большее чем p, и присвоить значению переменной p это число.\n"
                                 " 5)Повторять шаги 3 и 4, пока возможно.\n"
                                 "просмотр кода задачи - /sev_code\n")
            await message.answer("Входные данные\n"
                                 "10\n"
                                 "Выходные данные\n"
                                 "4")

        @self.dp.message_handler(commands=['sev_code'])
        async def sev_examination(message: types.message):
            await message.answer('def sieve(n):\n'
                                 '  prime = [True] * (n + 1)\n'
                                 '  for i in range(2, n + 1):\n'
                                 '  if prime[i]:\n'
                                 '  for j in range(i ** 2, n + 1, i):\n'
                                 '  prime[j] = False\n'
                                 '  last = prime.count(True) - 2\n'
                                 '  return last\n'
                                 'print(sieve(int(input())))')
            await message.answer("Данный код работает на codefoces.com\n"
                                 "Задача взята с https://codeforces.com/group/N6UYx1b3Cf/contest/389708/problem/A")

        @self.dp.message_handler(commands=['fib'])
        async def sieve(message: types.message):
            await message.answer('Условие задачи:\n'
                                 'Программа принимает на вход число членов последовательности Фибоначчи\n'
                                 'и при помощи рекурсии вычисляет все числа, входящие в эту последовательность.\n'
                                 'Нужно прописать саму функцию\n'
                                 'просмотр кода задачи - /fib_code\n'
                                 )
            await message.answer('Входные данные\n'
                                 '10\n'
                                 'Выходные данные:\n'
                                 '1 1 2 3 5 8 13 21 34 55')

        @self.dp.message_handler(commands=['fib_code'])
        async def fib_code(message: types.message):
            await message.answer('def fibonacci(n):\n'
                                 '    if n in (1, 2):\n'
                                 '        return 1\n'
                                 '    return fibonacci(n - 1) + fibonacci(n - 2)\n'
                                 )

        @self.dp.message_handler(commands=['easy'])
        async def easy(message: types.message):
            await message.answer("Условие задачи:\n"
                                 "Нужно проверить число на простоту\n"
                                 "т.е. является ли оно простым или нет.\n"
                                 "вывести True - при правильности ответа, иначе False\n"
                                 "просмотр кода задачи - /easy_code")
            await message.answer("Входные данные:\n"
                                 "7\n"
                                 "Выходные данные:\n"
                                 "True")
            await message.answer("Входные данные:\n"
                                 "10\n"
                                 "Выходные данные:\n"
                                 "False")

        @self.dp.message_handler(commands=['easy_code'])
        async def easy_cod(message: types.message):
            await message.answer("n = int(input())\n"
                                 "flag = True\n"
                                 "for i in range(2, int(n ** 0.5) + 1):\n"
                                 "    if n % i == 0:\n"
                                 "        flag = False\n"
                                 "print(flag)")

        @self.dp.message_handler(commands=['rand'])
        async def rand(message: types.message):
            await message.answer("Условие задчи:\n"
                                 "На вход подаются два числа: А и В\n"
                                 "Нужно вывести рандомное число в диапазоне от А до В\n"
                                 "просмотр кода задачи - /rand_code")
            await message.answer("Входные данные:n"
                                 "5\n"
                                 "7\n"
                                 "Выходные данные:\n"
                                 "6")

        @self.dp.message_handler(commands=['rand_code'])
        async def rand_code(message: types.message):
            await message.answer("import random\n"
                                 "a = int(input())\n"
                                 "b = int(input())\n"
                                 "print(random.randint(a, b))"
                                 )

        @self.dp.message_handler(commands=['sorting'])
        async def sorting(message: types.message):
            await message.answer("Вам дается последовательность чисел\n"
                                 "Нужно вывести её отсортированной(только давайте без sorted)\n"
                                 "просмотр кода задачи - /sorting_code")
            await message.answer("Входные данные:\n"
                                 "1 2 6 7 9 15 68 0\n"
                                 "Выходные данные:\n"
                                 "0 1 2 6 7 9 15 68")

        @self.dp.message_handler(commands=['sorting_code'])
        async def sorting_code(message: types.message):
            await message.answer('def merge(left, right):\n'
                                 '    res = list()\n'
                                 '    i, j = 0, 0\n'
                                 '    while i < len(left) and j < len(right):\n'
                                 '        if left[i] < right[j]:\n'
                                 '            res.append(left[i])\n'
                                 '            i += 1\n'
                                 '        else:\n'
                                 '            res.append(right[j])\n'
                                 '            j += 1\n'
                                 '    while i < len(left):\n'
                                 '        res.append(left[i])\n'
                                 '        i += 1\n'
                                 '    while j < len(right):\n'
                                 '        res.append(right[j])\n'
                                 '        j += 1\n'
                                 '    return res\n'
                                 'def merge_sort(lst):\n'
                                 '    if len(lst) <= 1:\n'
                                 '        return lst\n'
                                 '    left = merge_sort(lst[:len(lst) // 2])\n'
                                 '    right = merge_sort(lst[len(lst) // 2:])\n'
                                 '    return merge(left, right)\n'
                                 'n = int(input())\n'
                                 'lst = list(map(int, input().split()))\n'
                                 'print(*merge_sort(lst))')
            await message.answer("Данный код работает на codefoces.com\n"
                                 "Задача взята с: https://codeforces.com/group/N6UYx1b3Cf/contest/103851/problem/B")

        @self.dp.message_handler(commands=['list_range'])
        async def list_range(message: types.message):
            await message.answer("Условие задачи:\n"
                                 "Создать список [ 18, 14, 10, 6, 2 ]  с помощью функции range()\n"
                                 "просмотр кода задачи -  /list_range_code")
            await message.answer("Входные данные:\n\n"
                                 "Выходные данные:\n"
                                 "18 14 10 6 2")

        @self.dp.message_handler(commands=['list_range_code'])
        async def list_range_code(message: types.message):
            await message.answer("lst = []\n"
                                 "for i in range(18, 1, -4):\n"
                                 "    lst.append(i)\n"
                                 "print(lst)")

        @self.dp.message_handler(commands=['reversing'])
        async def reversing(message: types.message):
            await message.answer("Условие задачи:\n"
                                 "Перевернуть строчку\n"
                                 "просмотр кода задачи - /reversing_code")
            await message.answer("Входные данные:\n"
                                 "Всем привет!\n"
                                 "Выходные данные:\n"
                                 "!тевирп месВ")

        @self.dp.message_handler(commands=['reversing_code'])
        async def reversing_code(message: types.message):
            await message.answer("s = str(input())\n"
                                 "print(s[::-1])")

        @self.dp.message_handler(commands=['file'])
        async def file(message: types.message):
            await message.answer("event - переменная с текстом события\n"
                                 "file_name - имя файла с логом\n"
                                 "Файл с логом содержит записи о некоторых событиях вида:\n\n"

                                 "event 3 - 'git log -2'\n"
                                 "event 2 - 'git log'\n"
                                 "event 1 - 'git status'\n"
                                 "Пример нового события:\n\n"

                                 'git fetch origin\n'
                                 'Дополните лог в файле так, чтобы новое событие было записано вверху. Не забудьте указать порядковый номер события.\n\n'

                                 "event 4 - 'git fetch origin'\n"
                                 "event 3 - 'git log -2'\n"
                                 "event 2 - 'git log'\n"
                                 "event 1 - 'git status'\n"
                                 'Если файл отсутствует или не содержит записей, начните нумеровать события с 1.\n\n'

                                 'Не забывайте про переносы строк!\n\n\n'



                                 'Примечание. Гарантируется, что путь не указывает на каталог. Т.е. ситуация когда файла нет и его невозможно создать исключена.\n\n'
                                 'Примечание. Используйте import os.path\n'
                                 'Примечание. В логе могут быть пустые строки\n'
                                 "P.S в тестировочной системе курса, в задачи перменные уже даны.\n"
                                 "Ничего вводить не надо\n"
                                 "просмотр кода задачи - /file_code")
            await message.answer("Ввод данных 1:\n\n"

                                 'event = "git fetch origin"\n'
                                 'file_name = "tmp/git.log"\n'
                                 "'Вывод данных 1:\n\n'"

                                 "'event 4 - 'git fetch origin'\n'"
                                 "'event 3 - 'git log -2'\n'"
                                 "'event 2 - 'git log'\n'"
                                 "'event 1 - 'git status'\n'"
                                 "'Ввод данных 2:\n\n'"

                                 'event = "git fetch origin"\n'
                                 'file_name = "tmp/empty_git.log"\n'
                                 "'Вывод данных 2:\n\n'"

                                 "'event 1 - 'git fetch origin'\n'"
                                 "'Ввод данных 3:\n\n'"

                                 'event = "2020_02_05 15_05_31"\n'
                                 'file_name = "tmp/access.log"\n'
                                 "'Вывод данных 3:\n\n'"

                                 "'event 3 - '2020_02_05 15_05_31'\n'"
                                 "'event 2 - '2020_02_05 15_05_30'\n\n'"

                                 "event 1 - '2020_02_01 15_05_31'")

        @self.dp.message_handler(commands=['file_code'])
        async def file_code(message: types.message):
            await message.answer("import os.path\n\n"
                                 "if os.path.isfile(file_name):\n"
                                 "   with open(file_name, 'r', encoding = 'utf-8') as f:\n"
                                 "        s = [i.strip() for i in f.readlines()]\n"
                                 "        lenq = 0\n"
                                 "        for i in s:\n"
                                 "            if len(i) > 0:\n"
                                 "                lenq += 1\n"
                                 "        if lenq == 0:\n"
                                 "            with open(file_name, 'w', encoding = 'utf-8') as f:\n"
                                 '                st = f\"event {lenq + 1} - \'{event}\''
                                 "        else:\n"
                                 "            lst = list()\n"
                                 '            st = f\"event {lenq + 1} - \'{event}\'\"\n'
                                 "            lst.append(st)\n"
                                 "            for i in s:\n"
                                 "                lst.append(i)\n"
                                 "   with open(file_name, 'w', encoding = 'utf-8') as f:\n"
                                 "        f.seek(0)\n"
                                 "        for i in lst:\n"
                                 "            f.write(i + \''\\n'\')\n"
                                 "else:\n"
                                 "    with open(file_name, 'w', encoding = 'utf-8') as f:\n"
                                 "        s = f\"event 1 - \'{event}\'\"\n"
                                 "        f.write(s + \'\\n\')\n")

            await message.answer("Данный код работает на https://stepik.org/\n"
                                 "Задача взята с https://stepik.org/lesson/305015/step/15?unit=287494")

        @self.dp.message_handler(commands=['stack'])
        async def stack(message: types.message):
            await message.answer('Простой стек\n'
                                 'Реализуйте структуру данных "стек". Напишите программу, содержащую описание стека\n'
                                 'и моделирующую работу стека, реализовав все указанные здесь методы.  Программа считывает последовательность команд\n'
                                 'и в зависимости от команды выполняет ту или иную операцию.\n'
                                 'После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:\n\n'

                                 'push n\n\n'

                                 'Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.\n'

                                 'pop\n\n'

                                 'Удалить из стека последний элемент. Программа должна вывести его значение.\n\n'

                                 'back\n\n'

                                 'Программа должна вывести значение последнего элемента, не удаляя его из стека.\n\n'

                                 'size\n\n'

                                 'Программа должна вывести количество элементов в стеке.\n\n'

                                 'clear\n\n'

                                 'Программа должна очистить стек и вывести ok.\n\n'

                                 'exit\n\n'

                                 'Программа должна вывести bye и завершить работу.\n\n'

                                 'Входные данные\n\n'

                                 'Команды управления стеком вводятся в описанном ранее формате по 1 на строке.\n\n'

                                 'Гарантируется, что набор входных команд удовлетворяет следующим требованиям:\n'
                                 'максимальное количество элементов в стеке в любой момент не превосходит 100,\n'
                                 'все команды pop и back корректны, то есть при их исполнении в стеке содержится хотя бы один элемент.\n\n'

                                 'Выходные данные\n\n'

                                 'Требуется вывести протокол работы со стеком, по 1 сообщению в строке\n'
                                 'просмотр кода задачи - /stack_code\n')

            await message.answer('Ввод данных:\n\n'
                                 'push 3\n'
                                 'push 14\n'
                                 'size\n'
                                 'clear\n'
                                 'push 1\n'
                                 'back\n'
                                 'push 2\n'
                                 'back\n'
                                 'pop\n'
                                 'size\n'
                                 'pop\n'
                                 'size\n'
                                 'exit\n'
                                 'Вывод данных:\n\n'
                                 'ok\n'
                                 'ok\n'
                                 '2\n'
                                 'ok\n'
                                 'ok\n'
                                 '1\n'
                                 'ok\n'
                                 '2\n'
                                 '2\n'
                                 '1\n'
                                 '1\n'
                                 '0\n'
                                 'bye')

        @self.dp.message_handler(commands=['stack_code'])
        async def stack_code(message: types.message):
            await message.answer("k = list()\n"
                                 "stackHIH = list()\n"
                                 "while True:\n"
                                 "    a =  input()\n"
                                 "    if a == 'exit':\n"
                                 "        break\n"
                                 "    if 'push' in a:\n"
                                 "        a,b = a.split()\n"
                                 "        stackHIH.append(b)\n"
                                 "        print('ok')\n"
                                 "    elif a == 'pop':\n"
                                 "        print(stackHIH.pop())\n"
                                 "    elif a == 'back':\n"
                                 "        print(stackHIH[-1])\n"
                                 "    elif a == 'size':\n"
                                 "        print(len(stackHIH))\n"
                                 "    elif a == 'clear':\n"
                                 "        stackHIH.clear()\n"
                                 "        print('ok')\n"
                                 "print('bye')\n")
            await message.answer("Данный код работает на https://stepik.org/\n"
                                 "Задача взята с https://stepik.org/lesson/389230/step/4?unit=378335")

        @self.dp.message_handler(commands=['deq'])
        async def deq(message: types.message):
            await message.answer('Простая очередь\n'
                                 'Реализуйте структуру данных "очередь".\n'
                                 'Напишите программу, содержащую описание очереди и моделирующую работу очереди,\n'
                                 'реализовав все указанные здесь методы. Программа считывает последовательность команд и\n'
                                 'в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды\n'
                                 'программа должна вывести одну строчку. Возможные команды для программы:\n\n'

                                 'push n\n\n'

                                 'Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.\n\n'

                                 'pop\n\n'

                                 'Удалить из очереди первый элемент. Программа должна вывести его значение.\n\n'

                                 'front\n\n'

                                 'Программа должна вывести значение первого элемента, не удаляя его из очереди.\n\n'

                                 'size\n\n'

                                 'Программа должна вывести количество элементов в очереди.\n\n'

                                 'clear\n\n'

                                 'Программа должна очистить очередь и вывести ok.\n\n'

                                 'exit\n\n'

                                 'Программа должна вывести bye и завершить работу.\n\n'

                                 'Гарантируется, что набор входных команд удовлетворяет следующим требованиям:\n'
                                 'максимальное количество элементов в очереди в любой момент не превосходит 100,\n'
                                 'все команды pop и front корректны, то есть при их исполнении\n'
                                 'в очереди содержится хотя бы один элемент.\n\n'

                                 'Входные данные\n\n'

                                 'Вводятся команды управления очередью, по одной на строке\n\n'

                                 'Выходные данные\n\n'

                                 'Требуется вывести протокол работы с очередью, по одному сообщению на строке'
                                 "просмотр кода задачи - /deq_code\n")
            await message.answer('Ввод данных:\n\n'
                                 'size\n'
                                 'push 1\n'
                                 'size\n'
                                 'push 2\n'
                                 'size\n'
                                 'push 3\n'
                                 'size\n'
                                 'exit\n\n'

                                 'Вывод данных:\n\n'

                                 '0\n'
                                 'ok\n'
                                 '1\n'
                                 'ok\n'
                                 '2\n'
                                 'ok\n'
                                 '3\n'
                                 'bye')

        @self.dp.message_handler(commands=['deq_code'])
        async def deq(message: types.message):
            await message.answer('from collections import deque\n'
                                 'deq = deque()\n'
                                 'while True:\n'
                                 '    n = input()\n'
                                 '    if n == "exit":\n'
                                 '        break\n'
                                 '    elif "push" in n:\n'
                                 '        a, b = n.split()\n'
                                 '        deq.append(int(b))\n'
                                 '        print("ok")\n'
                                 '    elif n == "pop":\n'
                                 '        print(deq.popleft())\n'
                                 '    elif n == "front":\n'
                                 '        print(deq[0])\n'
                                 '    elif n == "size":\n'
                                 '        print(len(deq))\n'
                                 '    elif n == "clear":\n'
                                 '        deq.clear()\n'
                                 '        print("ok")\n'
                                 'print("bye")')
            await message.answer("Данный код работает на https://stepik.org/\n"
                                 "Задача взята с https://stepik.org/lesson/389076/step/4?unit=378185")

        @self.dp.message_handler(commands=['sets'])
        async def sets(message: types.message):
            await message.answer('Полиглоты\n'
                                 'Каждый из N школьников некоторой школы знает Mi языков. Определите,\n'
                                 'какие языки знают все школьники и языки, которые знает хотя бы один из школьников.\n'

                                 'Входные данные\n\n'

                                 'Первая строка входных данных содержит количество школьников N.\n'
                                 'Далее идет N чисел M(i), после каждого из чисел идет M(i) строк, содержащих названия языков,\n'
                                 'которые знает i-й школьник. Длина названий языков не превышает 1000 символов,\n'
                                 'количество различных языков не более 1000. 1  N 1000, 1  M(i) 500.\n\n'

                                 'Выходные данные\n\n'

                                 'В первой строке выведите количество языков, которые знают все школьники.\n'
                                 'Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник,\n'
                                 'на следующих строках - список таких языков.\n'
                                 'Вывод необходимо сделать в алфавитном порядке.'
                                 'просмотр кода задачи - /sets_code\n')
            await message.answer('Ввод данных:\n\n'
                                 '3\n'
                                 '3\n'
                                 'Russian\n'
                                 'English\n'
                                 'Japanese\n'
                                 '2\n'
                                 'Russian\n'
                                 'English\n'
                                 '1\n'
                                 'English\n'
                                 'Вывод данных:\n\n'
                                 '1\n'
                                 'English\n'
                                 '3\n'
                                 'English\n'
                                 'Japanese\n'
                                 'Russian')

        @self.dp.message_handler(commands=['sets_code'])
        async def sets_code(message: types.message):
            await message.answer("students = [{input() for j in range(int(input()))} for i in range(int(input()))]\n"
                                 "known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)\n"
                                 "print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')\n"
                                 "print(len(known_by_someone), *sorted(known_by_someone), sep='\n')")
            await message.answer("Данный код работает на https://stepik.org/\n"
                                 "Задача взята с https://stepik.org/lesson/389077/step/6?unit=378186")

        executor.start_polling(self.dp, skip_updates=True)


if __name__ == '__main__':
    TheBestBotInTheWorld().start()
