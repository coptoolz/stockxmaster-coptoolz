# OX Discord Bot
### By XO
##### Right Now This Only Supports Windows. It is a work in progress and im adding more soon. If you have any suggestions just DM on twitter @ehxohd

### License
- There is no specific license on this bot. You are free to modify and add yourself to credits but removing my credits, selling, or defacing the bot and redistributing as your own is not allowed.

### Requirements
- Python 3.6.4+
+ Pip Modules
	+ Names
	+ Requests
	+ Discord.py
	+ StockXSdk
	+ bs4
	+ Chatterbot 
	+ Hastebin

### Installation
- Run Installer.bat

- Go To https://discordapp.com/developers/applications/me/create and create a bot user

- Scroll down and create a bot user

- Find Your Bots ClientID and fill in this link https://discordapp.com/api/oauth2/authorize?client_id=CLIENTID&permissions=8&scope=bot

- Visit That Link And Add The Bot To Your Server

- Find your bot user token

- Open botconfig.json in notepad or a text editor

- Set the value of token as the bot user token

- Set the value of prefix as your desired call prefix (e.x. ! or ?)

- Set The Value Of stockxemail as your stockx email and stockxpass as your stockxpassword

- Save This Cd into the folder and type "python main.py"

### Commands And Usage
where i say (prefix) it should be replaced with your prefix e.x if my prefix is ! then (prefix) = !
When filling in () values do not include ()
+ ping
	+ Command: (prefix)ping
		+ This pings the bot to see if its online

+ CreateATC
	+ Command: (prefix)CreateATC (siteurl) (variantID)
		+ Creates An ATC Link For An Item On A Shopify Site Given The Url And Variant

+ Choose
	+ Command: (prefix)Choose (option1,option2,supportsinfiniteoptions)
		+ Chooses A Random Option From List

+ ATC
	+ Command: (prefix)ATC (producturl)
		+ Creates ATC Links for item on a shopify site

+ Creator
	+ Command: (prefix)Creator
		+ Returns Info About Me

+ IsShopify
	+ Command: (prefix)IsShopify (site url)
		+ Tells If A Website Runs On Shopify

+ getproducts
	+ Command: (prefix)getproducts (pageurl)
		+ Scrapes products off shopify site creats atc links and everything

+ help
	+ Command: (prefix)help
		 + Pretty much dms a user this

+ randomquote
	+ Command: (prefix)randomquote
		 + Just says a random quote

+ online?
	+ Command: (prefix)online? (site link)
		 + Tells if a website is online

+ SupremeWeek
	+ Command: (prefix)SupremeWeek
		+ Returns the items of the latest supreme week

Alot more soon just want to perfect these first

### Support
- Support IS offered on this product to an extent. If you encounter constant issues please pm me on twitter ONLY AFTER YOU GOOGLE THE ERRORS.

### Contact
- Twitter @ehxohd
- Discord XO#0001
