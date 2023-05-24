import telebot
from config import keys, token  # связываем параметры keys, token с текущим файлом
from extensions import APIException, CurrencyConverter  # связываем классы APIException, CurrencyConverter с текущим файлом


bot = telebot.TeleBot(token) # привязываем токен доступа к боту


@bot.message_handler(commands=['start', 'help'])  # конструкция для работы с commands
def help(message: telebot.types.Message):  # функция по командам start, help
    text = 'Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # конструкция для работы с commands
def values(message: telebot.types.Message):  # функция по команде values
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ]) # конструкция для работы с content_types
def convert(message: telebot.types.Message):  # функция обработки сообщения вида <валюта> <валюта> <количество>
    try:
        values = message.text.split(' ')  # создаем список из введенного текста

        if len(values) != 3:  # условие длины сообщения (списка)
            raise APIException('Неверное количество параметров.')  # вывод сообщения если условие не выполняется

        quote, base, amount = values  # присваеваем переменные к первым 3м элементам списка
        total_base = CurrencyConverter.get_price(quote, base, amount)  #
    except APIException as e:  #
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:  #
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:


        text = f'Цена {amount} {quote} в {base} - {round(float(total_base)*float(amount), 3)}'  # вывод сообщения при валидных данных
        bot.send_message(message.chat.id, text)  # маркер завершения обработчика текста для бота


bot.polling(none_stop=True)  # бесконечный цикл для работы бота
