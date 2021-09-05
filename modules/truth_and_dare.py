import random
from helpers.filters import command
from telegram import Update
from telegram.ext import CallbackContext, run_async
from config import BOT_USERNAME
import modules.truth_and_dare_string as truth_and_dare_string
from pyrogram import Client

@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

import random
from helpers.filters import command
from telegram import Update
from telegram.ext import CallbackContext, run_async
from config import BOT_USERNAME
import modules.truth_and_dare_string as truth_and_dare_string
from pyrogram import Client

@Client.on_message(command(["t", f"t@{BOT_USERNAME}"]))
def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


@Client.on_message(command(["d", f"d@{BOT_USERNAME}"]))
def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


# by @addyxd
