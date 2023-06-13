"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from dotenv import dotenv_values

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Set higher logging level for httpx to avoid all
# GET and POST requests being logged.
logging.getLogger('httpx').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
config = dotenv_values('.env')

def main() -> None:
    """Run the bot."""
    logging.info('Config: %s' % config)
    # TODO: Implement bot main loop.


if __name__ == '__main__':
    main()
