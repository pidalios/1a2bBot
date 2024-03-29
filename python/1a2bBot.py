# @File      : 1a2bBot.py
# @Author     : Hsuan Tsai
# @Date       : 2021-07-07
# @Python Version: python 3.9

import random as rd
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

token = 'Your token'
FILE_NAME = 'answer.txt'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Generate the answer
def ansGenerate() -> None:
    real = list('0123456789')
    for i in range(10):
        k = rd.randint(0, 9)
        real[i], real[k] = real[k], real[i]
    with open(FILE_NAME, 'w') as f:
        f.write('{:s}{:s}{:s}{:s}'.format(real[0], real[1], real[2], real[3]))
    print('The answer is {:s}{:s}{:s}{:s}'.format(real[0], real[1], real[2], real[3]))

# Guess the answer
def myGuess(update: Update, context: CallbackContext) -> None:
    counterA = 0
    counterB = 0
    with open(FILE_NAME, 'r') as f:
        ans = f.read()
    realNum = list(ans)

    guess = list(update.message.text)
    for i in range(4):
        if realNum[i]==guess[i]:
            counterA+=1
        for j in range(4):
            if realNum[i]==guess[j] and i!=j:
                counterB+=1
    update.message.reply_text('{:s}{:s}{:s}{:s}   {:d}A{:d}B'.format(guess[0], guess[1], guess[2], guess[3], counterA, counterB))
    print(('{:s}{:s}{:s}{:s}   {:d}A{:d}B'.format(guess[0], guess[1], guess[2], guess[3], counterA, counterB)))

    if counterA==4:
        update.message.reply_text('Congratulations! You win!')
        update.message.reply_text('Enter /start to start another game.')
        return

# Initialize the game
def gameInit(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hello {user.mention_markdown_v2()}\!')
    update.message.reply_text('Game Start!')
    update.message.reply_text('Please enter 4 digits of numbers to begin.')
    ansGenerate()

def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', gameInit))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, myGuess))

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()
