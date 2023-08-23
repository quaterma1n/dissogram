import requests
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

USER_MAP = {
    "telegram_user1": "discord_id1",
    "telegram_user2": "discord_id2",
    # ... add more mappings as needed
}


def check_meeting(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Please provide the meeting ID.")
        return

    meeting_id = context.args[0]
    headers = {
        'Authorization': f'Bot {DISCORD_TOKEN}'
    }

    # Fetch voice channel members
    response = requests.get(
        url=f'https://discord.com/api/v10/guilds/YOUR_GUILD_ID/voice-channels/{meeting_id}/members',
        headers=headers
    )
    data = response.json()
    if 'message' in data:
        update.message.reply_text("Failed to check the meeting. Ensure your Discord bot has proper permissions.")
        return

    member_ids = {member['user']['id'] for member in data}
    late_members = [tg for tg, disc in USER_MAP.items() if disc not in member_ids]

    if not late_members:
        update.message.reply_text("Everyone is present!")
        return

    mentions = ', '.join(f"@{user}" for user in late_members)
    update.message.reply_text(f"The following members are late: {mentions}")


def main():
    updater = Updater(token=TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("check_meeting", check_meeting, pass_args=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
