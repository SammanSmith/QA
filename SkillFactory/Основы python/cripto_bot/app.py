import telebot
import config as cfg
import extensions as ext

bot = telebot.TeleBot(cfg.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def echo_test(message):
    text = 'Чтобы начать работу введите команду боту через пробел в следующем формате:\n<из какой валюты> <в какую валюту перевести> <количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for k in cfg.currency.keys():
        text = '\n'.join((text, k, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ext.ConvertionException('Слишком много параметров.\nНужно ввести 3 параметра')

        quote, base, amount = values
        total_base = ext.Exchange.get_price(quote, base, amount)

    except ext.ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так с {e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {round(total_base, 2)}'
        bot.send_message(message.chat.id, text)


bot.polling()