# Telegram parser
It's a project to parse messages from telegram chats. Main task it to create some unified CLI for telegram "Data mining"
Some NLP cases, where you can use this interface over Telethon library: 
1) Message summarization over some time period
2) Text stylization by some author at Telegram
3) Creating dataset for other task like some sentiment analysis, sentence similarity and translation

# How to use
1) Create .env file from example.env (it's used to get information about your telegram channels)
2) Run --help for other instructions

`python main.py --help`

You can use get-dialogs method to get all channels id:

`python main.py get-dialogs`

Or use parse-channel to get .csv file with all messages from it

`python main.py parse-channel --output-file=some_channel_messages.csv -- -1001754702845`

where -1001754702845 is some channel_id 
