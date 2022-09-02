import telebot
import random


API_TOKEN = '2001513902:AAG8aziYmhikVTFlVrHK_AECMPKo7x76zRU'

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['rivarossa', 'Rivarossa'])
def send_welcome(message):
    bot.reply_to(message, """\
ASPETTA.\
""")
    bot.reply_to(message, """\
    Ma lei è di Rivarossa\
    """)
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao cosa vuoi??\
""")
    bot.reply_to(message, """\
Non hai proprio nulla da fare...\
""")
    bot.reply_to(message, """\
Se vuoi una lista dei comandi devi chiedere a gino\
""")
@bot.message_handler(commands=['sandra', 'Sandra', 'SANDRA', 'Vai sandra'])
def send_welcome(message):
    bot.reply_to(message, """\
Buona notte e sogni d'oro!\
""")
@bot.message_handler(commands=['lista'])
def send_welcome(message):
    bot.reply_to(message, """\
Ecco una lista di comandi utili:\
""")
    bot.reply_to(message, """\
Sandra, Ciao e altro...\
""")
    bot.reply_to(message, """\
Per maggiori dettagli consultare il nostro sito oppure chiedete a gino\
""")
@bot.message_handler(commands=['guglielminetti', 'Guglielminetti', 'GSB', 'GBS'])
def send_welcome(message):
    bot.reply_to(message, """\
Ma salve signor G...\
""")
    bot.reply_to(message, """\
Volevamo informarla che le stiamo aggiungendo nuovi comandi\
""")
    bot.reply_to(message, """\
Per maggiori dettagli basta che digiti la barra laterale+lista\
""")
    bot.reply_to(message, """\
Arrivederla\
""")
@bot.message_handler(commands=['Chi siamo', 'chi', 'chisiamo'])
def send_welcome(message):
    bot.reply_to(message, """\
La nostra missione è GARANTIRLE il nostro supporto quando non sa cosa fare e non vuole saperne di studiare Chimica.
In oltre, può usufruire di tale servizio anche quando dovrebbe seguire la lezioni.
Le ricordiamo che il servizio è gratuito\
""")
    bot.reply_to(message, """\
Se vuoi però dammi pure 5 euro  \
""")
    bot.reply_to(message, """\
Grazie.\
""")
    bot.reply_to(message, """\
Arrivederla\
""")
@bot.message_handler(commands=['st'])
def send_sticker(message):
    bot.reply_to(message, message.reply.photo('http://thecatapi.com/api/images/get'))
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    N = ['Ma salve!', 'Buon salve', 'Buon giorno!', 'Eccolo']
    random_num = random.choice(N)
    if message.text=='Sandra':
        bot.reply_to(message, 'Buona notte!')
    elif message.text=='Ciao':
        bot.reply_to(message, random_num)

    else:
        bot.reply_to(message, 'Aspetta...')
        bot.reply_to(message, 'Non credo di aver capito...')
        bot.reply_to(message, 'Se vuoi una lista dei comandi disponibili chiedi a gino')

bot.infinity_polling()