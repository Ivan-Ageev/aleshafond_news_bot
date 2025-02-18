Telegram Bot for Charity Foundation "Alyosha"
Welcome to the official Telegram bot of the Charity Foundation "Alyosha"! This bot is designed to keep you informed about the foundation's activities, share inspiring stories of beneficiaries, and provide an easy way to support our cause.

Features

1. News About Beneficiaries

Stay updated on the latest stories of children and families we support.
Learn about their challenges, progress, and dreams.
Search for specific children by entering their last name.
2. General Information About the Foundation

Discover our mission, values, and the impact we’ve made over the years.
Learn about our ongoing projects and campaigns.
3. Make a Donation

Support our cause directly through the bot.
Click the "Help Now!" button to contribute.
How to Use the Bot

Start the Bot:
Type /start to begin interacting with the bot.
You'll receive a welcome message with a menu of options.
Search for News About Beneficiaries:
Click the "О детях 👨‍👧" button or type a child's last name to search for updates.
Learn About the Foundation:
Click the "О фонде 🏢" button to get general information about our mission and work.
Make a Donation:
Click the "Помочь сейчас! ❤️" button to visit the donation page.
Technical Details

Dependencies

python-telegram-bot (v20+)
urllib
logging
os
Environment Variables

TOKEN: Your Telegram bot token (e.g., ).
LOGO_PATH: Path to the logo image used in the bot (e.g., /Users/ivan/Downloads/bear3.png).
Commands

/start: Start the bot and display the main menu.
/search: Search for news about a specific child by entering their last name.
/about: Get information about the foundation.
Handlers

CommandHandler: Handles /start and other commands.
CallbackQueryHandler: Handles button clicks (e.g., "О детях", "О фонде").
MessageHandler: Processes text messages for searching news.
Web App Integration

The bot uses Telegram's WebApp feature to display search results directly from the foundation's website.
Setup Instructions

Install Dependencies:
pip install python-telegram-bot

Set Environment Variables:
Replace the TOKEN and LOGO_PATH values in the script with your actual bot token and logo path.

Run the Bot:
python bot.py

Interact with the Bot:
Open Telegram and search for your bot.
Use the /start command to begin.

Code Structure

get_main_keyboard(): Generates the main menu with inline buttons.
start(): Handles the /start command and sends the welcome message.
button(): Handles button clicks (e.g., "О детях", "О фонде").
search_news(): Processes text messages to search for news about beneficiaries.
main(): Initializes and runs the bot.
License

This project is open-source and available under the MIT License.
