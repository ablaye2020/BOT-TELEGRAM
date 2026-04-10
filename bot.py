import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# -- ICI TU PROGRAMMES CE QUE LE BOT RÉPOND --
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salut ! Je suis vivant grâce à Render 🚀')

async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Commandes : /start , /aide')

# -- NE PAS TOUCHER EN DESSOUS (SAUF SI TU SAIS CE QUE TU FAIS) --
def main():
    # Récupère le mot de passe (Token) que Render va lui donner
    token = os.environ.get('TELEGRAM_TOKEN')
    app = Application.builder().token(token).build()
    
    # Lie les commandes tapées par l'utilisateur aux fonctions du dessus
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aide", aide))

    # Allume le bot
    app.run_polling()

if __name__ == '__main__':
    main()
