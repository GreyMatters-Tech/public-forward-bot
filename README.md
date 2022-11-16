# Public-Forward-Bot

# Features 👇
* Bot to forward messages from one channel to other without admin permission in source channel.
* Can only be used for Public channels.
* Can also be used for Public Restricted Channels.
* Bot Index message from channel and saves to database, further forwards and deletes each messages from database. Use of database was to Remove duplicacy of files.
* For Public Channels Bot is used to forward.

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://github.com/Greymattersbot/public-forward-bot)



### Variables

* `API_HASH` API Hash from my.telegram.org
* `API_ID` API ID from my.telegram.org
* `BOT_TOKEN` Bot token from @BotFather
* `OWNER_ID` Telegram Id of Owner.
* `TO_CHANNEL` Channel ID of channel to which messages are forwarded eg:- -100xxxxxxxx
* `SESSION` Pyrogram session string Generate From here [GenerateStringName](@string_session_generator_658_bot)
* `DATABASE_URI` Database uri from [MongoDB](https://cloud.mongodb.com/)
* `DATABASE_NAME` Database Cluster name
* `COLLECTION_NAME` Database Collection name.


### Credits
* [DⱥℝkAngel](https://github.com/Jijinr)
* [Rahul](https://github.com/rahulps1000)
* [Subinps](https://github.com/subinps)
