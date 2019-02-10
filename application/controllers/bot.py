from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # importa la libreria para la porgramacion del bot 
import logging # almacena sucesos con el bot(logs)
import web 


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) # formato del historial
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'bat_bot',
    user = 'batman',
    pw = 'batman.2019',
    port = 3306
    )

#Neoxerbot
token = '789611773:AAHcRiiyDtDov6pi7cT0HtUtFkqY6lcp3YU'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username # atrapa el comando del usuario 
    update.message.reply_text('Hola {} usa este comando:\n/info para saber que comandos usar'.format(username)) # Saludo de bienvenvida

def help(bot, update): # 
    username = update.message.from_user.username
    update.message.reply_text('Hola {} escribe \n/bat # para ver la info de un batman'.format(username)) 
    update.message.reply_text('O {} escribe \n/ro # para ver la info de un robin'.format(username))

def search_b(update):
    text = update.message.text.split() # speracion de texto por espacio en blanco
    username = update.message.from_user.username # username 
    try:
        id_batman = int(text[1]) # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(id_batman)
        result = db.select('batmans', where='id_batman=$id_batman', vars=locals())[0]
        print result
        respuesta =  "\n Habilidades:" + str(result.descripcion) + "\n \n Version:"+ str(result.version) + "\n \n Aparicion:" + str(result.aparicion)
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hey {}\nEsta es la informacion que buscas:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_batman))


def search_r(update):
    text = update.message.text.split() # speracion de texto por espacio en blanco
    username = update.message.from_user.username # username 
    try:
        id_robin = int(text[1]) # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(id_robin)
        result = db.select('robins', where='id_robin=$id_robin', vars=locals())[0]
        print result
        respuesta =  "\n Nombre:" + str(result.nombre_robin) + "\n \n Habilidades:"+ str(result.habilidades) + "\n \n Armas:" + str(result.armas)
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hey {}\nEsta es la informacion que buscas:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_robin))


def batman(bot, update):
    search_b(update)

def robin(bot,update):
    search_r(update)
def info(bot,update):
    username = update.message.from_user.username # atrapa el comando del usuario 
    update.message.reply_text('Hola {} escribe \n/bat # para saber la lista de los batmans'.format(username)) 
    update.message.reply_text('O {} escribe \n/ro # para saber la lista de los robins'.format(username))


def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'NEOXER init token'
        
        updater = Updater(token) # conexion con el bot

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'NEOXER init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("info", info))
        dp.add_handler(CommandHandler('bat',batman))
        dp.add_handler(CommandHandler('ro',robin))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'NEOXER ready'
        updater.idle() # esperando respuesta del usuario
    except Exception as e:
        print "Error 100: ", e.message

#if __name__ == '__main__':
#    main()
