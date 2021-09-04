import random
from helpers.filters import command
from telegram import Update
from telegram.ext import CallbackContext, run_async

import modules.truth_and_dare_string as truth_and_dare_string


@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

