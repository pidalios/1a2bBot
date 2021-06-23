import random as rd
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

token = '1889030668:AAEI-EWca833U-x8yFI7PRZIODGbPPYP01E'
FILE_NAME = 'answer.txt'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def myRandom() -> None:
    real = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, 10):
        k = rd.randint(0, 9)
        real[i], real[k] = real[k], real[i]
    f = open(FILE_NAME, 'w')
    f.write('{:s}{:s}{:s}{:s}'.format(real[0], real[1], real[2], real[3]))
    f.close()
    print('The answer is {:s}{:s}{:s}{:s}'.format(real[0], real[1], real[2], real[3]))

def myGuess(update: Update, context: CallbackContext) -> None:
    counterA = 0
    counterB = 0
    f = open(FILE_NAME, 'r')
    ans = f.read()
    realNum = list(ans)
    f.close()
    
    guess = list(update.message.text)
    for i in range(0, 4):
        if realNum[i]==guess[i]:
            counterA+=1
        for j in range(0, 4):
            if realNum[i]==guess[j] and i!=j:
                counterB+=1
    update.message.reply_text('{:s}{:s}{:s}{:s}   {:d}A{:d}B'.format(guess[0], guess[1], guess[2], guess[3], counterA, counterB))
    print(('{:s}{:s}{:s}{:s}   {:d}A{:d}B'.format(guess[0], guess[1], guess[2], guess[3], counterA, counterB)))

    if counterA==4:
        update.message.reply_text('Congratulations! You win!')
        update.message.reply_text('Enter /start to start another game.')
        return

def startGame(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!')
    update.message.reply_text('Let the game start!')
    update.message.reply_text('Please enter 4 digits of numbers to begin.')
    myRandom()

def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', startGame))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, myGuess))

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()
