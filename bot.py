from datetime import *
import psycopg2
import requests
from telebot import *

bot = TeleBot(str(input('Введите API-ключ для телеграм-бота: ')))  # ключ к тг боту
key = str(input('\nВведите API-ключ сервиса OpenWeather: '))  # ключ к openweather
city = 'Moscow,RU'  # город для openweather вместо координат


def WeatherBot(x):  # функция, выдающая погоду на неделю
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': city, 'units': 'metric', 'cnt': x, 'lang': 'ru',
                               'APPID': key})  # делает запрос к сайту openweather с определенными параметрами
    # res = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={55}&lon={37}&exclude=daily&cnt=7&units=metric&appid={key}")
    data = res.json()  # переводит данные с запроса в json файл
    answer = 'Город: Москва\n\n'  # создается переменная answer, в которую потом будут записываться значения
    if x == 1:
        pass
    else:
        answer += '\n'
    today = datetime.now()
    for i in range(x):
        wordly_day = today.strftime('%A')  # 2022.01.01 -> Saturday
        wordly_day = coverterDAYtoNUM(wordly_day)  # Saturay -> 6
        wordly_day = coverterNUMtoDAY(wordly_day)  # 6 -> Суббота
        day = today.strftime('%d.%m, ')  # 2022.01.01 -> 01.01
        answer += str(day) + '' + str(wordly_day) + ', ' + str(
            data['list'][i]['weather'][0]['description']) + '\nСредняя температура: ' + str(
            data['list'][i]['main']['temp']) + '\n\n'
        today += timedelta(days=1)  # прибавляет к текущей дате 1 день
    return answer


def raspisanie(today):  # огромная функция, которая представляет из себя рассписание, которое можно было реализовать через какую-нибудь субд, например, postgresql, но я сделал это расписание ещё 11 февраля, so..
    week = WeekLooker(today)
    day = today.strftime('%A')
    day = coverterDAYtoNUM(day)

    if week == 1:

        if day == 1:
            if today < datetime(2022, 2, 21) or today > datetime(2022, 4, 24):
                return "Понедельник, нечетная неделя.\n1 - 9:30-11:05, дистант, лекция по Философии;\n2 - 11:20-12:55, дистант, Английский язык;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."
            else:
                return "Понедельник, нечетная неделя.\n1 - 9:30-11:05, дистант, лекция по Философии;\n2 - 11:20-12:55, дистант, Английский язык;\n3 - 13:10-14:45, дистант, пратика по ВвИТ;\n4 - Пары нет;\n5 - Пары нет."



        elif day == 2:
            if today > datetime(2022, 4, 3):
                return "Вторник, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - 13:10-14:45, дистант, пратика Математики;\n4 - 15:25-17:00, дистант, пратика Философии;\n5 - Пары нет."
            else:
                return "Вторник, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, лекция по Физике;\n3 - 13:10-14:45, дистант, пратика Математики;\n4 - 15:25-17:00, дистант, пратика Философии;\n5 - Пары нет."



        elif day == 3:
            if today < datetime(2022, 2, 21):
                return "Среда, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, пратика Математики;\n3 - 13:10-14:45, дистант, пратика ТОЭ;\n4 - Пары нет;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today < datetime(2022, 5, 2):
                return "Среда, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, пратика Математики;\n3 - 13:10-14:45, дистант, пратика ТОЭ;\n4 - 15:25-17:00, дистант, пратика ВвИТ;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today > datetime(2022, 5, 2) and today < datetime(2022, 5, 15):
                return "Среда, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - 13:10-14:45, дистант, пратика ТОЭ;\n4 - 15:25-17:00, дистант, пратика ВвИТ;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today > datetime(2022, 5, 2) and today > datetime(2022, 5,15) and today < datetime(2022, 5, 22):
                return "Среда, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - 15:25-17:00, дистант, пратика ВвИТ;\n5 - Пары нет."
            else:
                return "Среда, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."



        elif day == 4:
            if today < datetime(2022, 3, 14):
                return "Четверг, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."
            elif today > datetime(2022, 3, 14) and today < datetime(2022, 4, 4):
                return "Четверг, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - Пары нет;\n5 - 17:15-18:50, очно, лабы по ТОЭ."
            elif today > datetime(2022, 3, 14) and today > datetime(2022, 4, 4) and today < datetime(2022, 5, 29):
                return "Четверг, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, очно, лабы по Физике;\n3 - 13:10-14:45, очно, лабы по ИиКГ;\n4 - Пары нет;\n5 - 17:15-18:50, очно, лабы по ТОЭ."
            else:
                return "Четверг, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, очно, лабы по Физике;\n3 - Пары нет;\n4 - Пары нет;\n5 - 17:15-18:50, очно, лабы по ТОЭ."



        elif day == 5:
            if today < datetime(2022, 4, 3):
                return "Пятница, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, лекция по ИиКГ;\n3 - 13:10-14:45, дистант, лекция по ТОЭ;\n4 - 15:25-17:00, дистант, лекция по Математике;\n5 - 17:15-18:50, дистант, лекция по Социологии."
            elif today > datetime(2022, 4, 3) and today < datetime(2022, 5, 1):
                return "Пятница, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - 15:25-17:00, дистант, лекция по Математике;\n5 - 17:15-18:50, дистант, лекция по Социологии."
            else:
                return "Пятница, нечетная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - 15:25-17:00, дистант, лекция по Математике;\n5 - Пары нет."



        elif day == 6:
            if today < datetime(2022, 4, 28):
                return "Суббота, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, Физ-ра;\n3 - 13:10-14:45, дистант, Физ-ра;\n4 - Пары нет;\n5 - 17:15-18:50, дистант, лабы по ВвИТ."
            else:
                return "Суббота, нечетная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, Физ-ра;\n3 - 13:10-14:45, дистант, Физ-ра;\n4 - 15:25-17:00, дистант, пратика по Социологии;\n5 - 17:15-18:50, дистант, лабы по ВвИТ."


        elif day == 7:
            return "Это же воскресенье, занятий нет!"



        else:
            return "Ошибка."



    elif week == 2:

        if day == 1:
            if today < datetime(2022, 2, 21):
                return "Понедельник, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, Английский язык;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today < datetime(2022, 4, 24):
                return "Понедельник, четная неделя.\n1 - 9:30-11:05, дистант, практика по Физике;\n2 - 11:20-12:55, дистант, Английский язык;\n3 - 13:10-14:45, дистант, пратика по ВвИТ;\n4 - Пары нет;\n5 - Пары нет."
            else:
                return "Понедельник, четная неделя.\n1 - 9:30-11:05, дистант, практика по Физике;\n2 - 11:20-12:55, дистант, Английский язык;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."



        elif day == 2:
            if today > datetime(2022, 4, 3):
                return "Вторник, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - 13:10-14:45, дистант, пратика Математики;\n4 - 15:25-17:00, дистант, пратика Философии;\n5 - Пары нет."
            else:
                return "Вторник, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, лекция по Физике;\n3 - 13:10-14:45, дистант, пратика Математики;\n4 - 15:25-17:00, дистант, пратика Философии;\n5 - Пары нет."



        elif day == 3:
            if today < datetime(2022, 2, 21):
                return "Среда, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, пратика Математики;\n3 - 13:10-14:45, дистант, пратика ТОЭ;\n4 - Пары нет;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today < datetime(2022, 5, 2):
                return "Среда, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, пратика Математики;\n3 - 13:10-14:45, дистант, пратика ТОЭ;\n4 - 15:25-17:00, дистант, пратика ВвИТ;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today > datetime(2022, 5, 2) and today < datetime(2022, 5, 15):
                return "Среда, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - 13:10-14:45, дистант, пратика ТОЭ;\n4 - 15:25-17:00, дистант, пратика ВвИТ;\n5 - Пары нет."
            elif today > datetime(2022, 2, 21) and today > datetime(2022, 5, 2) and today > datetime(2022, 5,
                                                                                                     15) and today < datetime(
                    2022, 5, 22):
                return "Среда, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - 15:25-17:00, дистант, пратика ВвИТ;\n5 - Пары нет."
            else:
                return "Среда, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."



        elif day == 4:
            if today < datetime(2022, 3, 14):
                return "Четверг, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - Пары нет;\n5 - Пары нет."
            elif today > datetime(2022, 3, 14) and today < datetime(2022, 4, 4):
                return "Четверг, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - Пары нет;\n5 - 17:15-18:50, очно, лабы по ТОЭ."
            elif today > datetime(2022, 3, 14) and today > datetime(2022, 4, 4) and today < datetime(2022, 5, 29):
                return "Четверг, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, очно, лабы по Физике;\n3 - 13:10-14:45, очно, лабы по ИиКГ;\n4 - Пары нет;\n5 - 17:15-18:50, очно, лабы по ТОЭ."
            else:
                return "Четверг, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, очно, лабы по Физике;\n3 - Пары нет;\n4 - Пары нет;\n5 - 17:15-18:50, очно, лабы по ТОЭ."



        elif day == 5:
            if today < datetime(2022, 4, 3):
                return "Пятница, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - 13:10-14:45, дистант, лекция по ТОЭ;\n4 - 15:25-17:00, дистант, лекция по Математике;\n5 - 17:15-18:50, дистант, лекция по Социологии."
            elif today > datetime(2022, 4, 3) and today < datetime(2022, 5, 1):
                return "Пятница, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - 15:25-17:00, дистант, лекция по Математике;\n5 - 17:15-18:50, дистант, лекция по Социологии."
            else:
                return "Пятница, четная неделя.\n1 - Пары нет;\n2 - Пары нет;\n3 - Пары нет;\n4 - 15:25-17:00, дистант, лекция по Математике;\n5 - Пары нет."



        elif day == 6:
            if today < datetime(2022, 4, 28):
                return "Суббота, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, Физ-ра;\n3 - 13:10-14:45, дистант, Физ-ра;\n4 - Пары нет;\n5 - 17:15-18:50, дистант, лабы по ВвИТ."
            else:
                return "Суббота, четная неделя.\n1 - Пары нет;\n2 - 11:20-12:55, дистант, Физ-ра;\n3 - 13:10-14:45, дистант, Физ-ра;\n4 - 15:25-17:00, дистант, пратика по Социологии;\n5 - 17:15-18:50, дистант, лабы по ВвИТ."


        elif day == 7:
            return "Это же воскресенье, занятий нет!"



        else:
            return "Ошибка."


def raspisanie_sql(today):
    conn = psycopg2.connect(dbname='admin', user='postgres', password='admin', port=5432)
    cur_sql = conn.cursor()
    week = WeekLooker(today)
    day = today.strftime('%A')
    day = coverterDAYtoNUM(day)

    if week == 1:
        if day == 1:
            cur_sql.execute("SELECT md1 FROM book")
        elif day == 2:
            cur_sql.execute("SELECT tu1 FROM book")
        elif day == 3:
            cur_sql.execute("SELECT wd1 FROM book")
        elif day == 4:
            cur_sql.execute("SELECT th1 FROM book")
        elif day == 5:
            cur_sql.execute("SELECT fd1 FROM book")
        elif day == 6:
            cur_sql.execute("SELECT sd1 FROM book")
        elif day == 7:
            cur_sql.execute("SELECT sud FROM book")
    elif week == 2:
        if day == 1:
            cur_sql.execute("SELECT md2 FROM book")
        elif day == 2:
            cur_sql.execute("SELECT tu2 FROM book")
        elif day == 3:
            cur_sql.execute("SELECT wd2 FROM book")
        elif day == 4:
            cur_sql.execute("SELECT th2 FROM book")
        elif day == 5:
            cur_sql.execute("SELECT fd2 FROM book")
        elif day == 6:
            cur_sql.execute("SELECT sd2 FROM book")
        elif day == 7:
            cur_sql.execute("SELECT sud FROM book")
    answer = str(coverterNUMtoDAY(day))+', '
    if week == 1:
        answer+='нечётная неделя.\n'
    else:
        answer+='чётная неделя.\n'
    answer_help = cur_sql.fetchall()
    for i in range(len(answer_help)):
        c=str(answer_help[i])
        c = c[2:-3]
        answer+=f'X{i}'+str(c)+'\n'
        answer = answer.replace('X0', '9:30-11:05 - ')
        answer = answer.replace('X1', '11:20-12:55 - ')
        answer = answer.replace('X2', '13:10-14:45 - ')
        answer = answer.replace('X3', '15:25-17:00 - ')
        answer = answer.replace('X4', '17:15-18:50 - ')
    return(answer)


def WeekLooker(
        today):  # функция, определяющая четность\нечетность недели относительно превой недели. Возвращает 1 или 2
    while today > datetime(2022, 2, 14):
        today -= timedelta(weeks=2)
    if today > datetime(2022, 2, 7):
        return 2
    else:
        return 1


def coverterDAYtoNUM(today):  # переводит английское название для недели в цифру
    if today == "Monday":
        return 1
    elif today == 'Tuesday':
        return 2
    elif today == 'Wednesday':
        return 3
    elif today == 'Thursday':
        return 4
    elif today == 'Friday':
        return 5
    elif today == 'Saturday':
        return 6
    elif today == 'Sunday':
        return 7


def coverterNUMtoDAY(today):  # переводит цифру в день недели
    if today == 1:
        return 'Понедельник'
    elif today == 2:
        return 'Вторник'
    elif today == 3:
        return 'Среда'
    elif today == 4:
        return 'Четверг'
    elif today == 5:
        return 'Пятница'
    elif today == 6:
        return 'Суббота'
    elif today == 7:
        return 'Воскресенье'


def Program(x):
    if x == 1:
        answer = 'Расписание на сегодня:\n\n'  # создаёт переменную answer и добавляет контекст для расписания на 1 день при условии, что x = 1
    elif x == 2 or x == 3 or x == 4:
        answer = 'Расписание на ' + str(x) + ' дня:\n\n\n'
    else:
        answer = 'Расписание на ' + str(
            x) + ' дней:\n\n\n'  # так же создаёт переменную answer, но добавляет контекст для расписания на неделю
    today = datetime.now()  # вычисляет сегоднящний день
    for i in range(x):
        answer += str(
            raspisanie_sql(today))  # обращается к расписанию и добавляет к переменной answer расписание на день today
        answer += '\n\n'  # добаввляет пропуски строки для упрощения понимания ответа (персонально)
        today += timedelta(days=1)  # увеличивает переменную today на 1 день
    return answer  # возвращает целостное расписание на 7 дней


@bot.message_handler(commands=["обновить"])  # просто заменил команду /start на команду /обновить
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Расписание на неделю')
    itembtn2 = types.KeyboardButton('Прогноз на неделю')
    itembtn3 = types.KeyboardButton('Расписание на сегодня')
    itembtn4 = types.KeyboardButton('Прогноз на сегодня')
    itembtn5 = types.KeyboardButton('/обновить')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(m.chat.id,
                     text="Здравствуйте. Список доступных команд на данный момент:\n1)Расписание на неделю;\n2)Прогноз на неделю;\n3)Расписание на сегодня;\n4)Прогноз на сегодня;\n5)/обновить.\nЕсли что-то не работает или не отображается,\nнажмите /обновить!",
                     reply_markup=markup)


@bot.message_handler(regexp="Прогноз на неделю")  # реакция бота на кнопку или сообщение с текстом "Прогноз на неделю"
def weather(message):
    bot.reply_to(message, WeatherBot(7))


@bot.message_handler(regexp="Расписание на неделю")  # реакция бота на кнопку или сообщение с текстом "Расписание на неделю"
def to_day(message):
    today = datetime.now()
    bot.reply_to(message, Program(7))


@bot.message_handler(regexp="Расписание на сегодня")  # реакция бота на кнопку или сообщение с текстом "Расписание на сегодня"
def to_day(message):
    today = datetime.now()
    bot.reply_to(message, Program(1))


@bot.message_handler(regexp="Прогноз на сегодня")  # реакция бота на кнопку или сообщение с текстом "Прогноз на сегодня"
def to_day(message):
    today = datetime.now()
    bot.reply_to(message, WeatherBot(1))


bot.polling(none_stop=True, interval=0)  # позволяет боту проверять наличие и соответсвие сообщений нон-стоп