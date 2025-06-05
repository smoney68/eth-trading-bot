import os
from telegram.ext import Updater, CommandHandler
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(f"https://arb-mainnet.g.alchemy.com/v2/{os.getenv('ALCHEMY_KEY')}"))
wallet_address = os.getenv("WALLET_ADDRESS")
private_key = os.getenv("WALLET_PRIVATE_KEY")

def start(update, context):
    update.message.reply_text("🤖 Bot de trading ETH actif !")

updater = Updater(os.getenv("BOT_TOKEN"), use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
