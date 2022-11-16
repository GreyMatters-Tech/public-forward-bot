# Forward_2.0

* Bot to forward messages from one channel to other without admin permission in source channel.
* Can be used for both private and Public channels.
* Bot Index message from channel and saves to database, further forwards and deletes each messages from database.Use of database was to Remove duplicacy of files.
* For Private channels User account is used to copy messages, hence will be slow, to avoid ban.
* For Public Channels Bot is used to forward , Thanks to [DⱥℝkAngel](https://github.com/Jijinr) for his [Frwdit](https://github.com/Jijinr/Frwdit).

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/subinps/Forward_2.0)



### Variables

* `API_HASH` API Hash from my.telegram.org
* `API_ID` API ID from my.telegram.org
* `BOT_TOKEN` Bot token from @BotFather
* `OWNER_ID` Telegram Id of Owner.
* `TO_CHANNEL` Channel ID of channel to which messages are forwarded eg:- -100xxxxxxxx
* `SESSION` Pyrogram session string Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://repl.it/@subinps/getStringName)
* `DATABASE_URI` Database uri from [MongoDB](https://cloud.mongodb.com/)
* `DATABASE_NAME` Database Cluster name
* `COLLECTION_NAME` Database Collection name.


### Credits
* [DⱥℝkAngel](https://github.com/Jijinr) for his [Frwdit](https://github.com/Jijinr/Frwdit)
* [Rahul](https://github.com/rahulps1000) for his [ForwardBot](https://github.com/rahulps1000/ForwardBot)

