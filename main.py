import requests
import json
import asyncio
import discord
import threading
import random
from discord_hooks import Webhook
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
from stockxsdk import Stockx
import os
from chatterbot import ChatBot
import hastebin
import names
import time
from random import choice, randint

ignoreList = [
    '!',
    '@',
    '#',
    '$',
    '$',
    '%',
    '^',
    '&',
    '*',
    '()',
    '(',
    ')',
    '-',
    'nigger',
    'fuck',
    'shit',
    'nigga',
    'is',
    'a',
    'it',
    'porn',
    '>',
    '<',
    '/',
    '\/',
    '[',
    ']',
    '`',
    '~',
    ';',
    ':',
    '*',
    'cock',
    '?',
    '0x'
]
chatbot = ChatBot(
    'OX',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.train("chatterbot.corpus.english")
stockx = Stockx()

colorArray = [0xff00ff, 0x15ff09, 0xf40006, 0x28ffff]

with open("botconfig.json") as file:
    config = json.load(file)
    file.close()

globalHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}


token = config['token']

stockxemail = config['stockxemail']
stockxpass = config['stockxpass']

client = discord.Client()



@client.event
async def on_message(message):
    prefix = config['prefix']
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'ping'):
        await client.send_message(message.channel, "Pong")

    if message.content.startswith(prefix + 'CreateATC'):
        if len(message.content.split(" ")) != 3:
            await client.send_message(message.channel, "Invalid number of arguments")
        else:
            site = message.content.split(" ")[1]
            variant = message.content.split(" ")[2]
            atclink = "{}/cart/{}:1".format(site, variant)
            await client.send_message(message.channel, atclink)

    if message.content.startswith(prefix + 'Choose'):
        if len(message.content.split(" ")) != 2:
            await client.send_message(message.channel, "Invalid Number Of Arguments")
        else:
            options = message.content.split(" ")[1]
            opl = []
            optionsl = options.split(",")
            for op in optionsl:
                opl.append(op)

            opnum = randint(0, len(opl) - 1)
            option = opl[opnum]
            await client.send_message(message.channel, "I Choose {}".format(option))

    if message.content.startswith(prefix + 'ATC'):
        try:
            if len(message.content.split(" ")) != 2:
                await client.send_message(message.channel, "Invalid Number Of Arguments")
            else:
                produrl = message.content.split(" ")[1]
                s = requests.session()
                prodobjr = s.get(produrl)
                prodobj = prodobjr.text.split("var meta = ")[1]
                prodobj = prodobj.split(";")[0]
                prodobj = json.loads(prodobj)
                soup = bs(prodobjr.text, "html.parser")
                actionheaders = {
                    'Authorization': 'Bot {}'.format(token),
                    'User-Agent': 'XO Discord Bot (https://xobots.io, v0.1)',
                    'Content-Type': 'application/json'
                }
                actionlink = "https://discordapp.com/api/channels/{}/webhooks".format(message.channel.id)

                actiondata = {
                    "name": "XO Discord Bot Creator Hook",
                }
                createwh = s.post(actionlink, headers=actionheaders, data=json.dumps(actiondata))
                webhookObject = json.loads(createwh.text)
                whid = webhookObject['id']
                whtoken = webhookObject['token']
                webhookurl = "https://discordapp.com/api/webhooks/{}/{}".format(whid, whtoken)
                colornum = randint(0, len(colorArray) - 1)
                color = colorArray[colornum]
                embed = Webhook(webhookurl, color=color)
                embed.set_author(name='XO Discord Bot | BY XO')
                embed.set_footer(text='Discord Bot By XO Dev | Twitter @ehxohd | Discord XO#0001', ts=True)
                prodsiteLink = produrl.split("/")[2]
                prodsiteLink = "https://{}".format(prodsiteLink)
                for pid in prodobj['product']['variants']:
                    embed.add_field(name=str(pid['public_title']), value="{}/cart/{}:1".format(prodsiteLink, pid['id']))

                embed.post()
                actionurl = "https://discordapp.com/api/webhooks/{}".format(whid)
                s.delete(actionurl, headers=actionheaders)
        except:
                await client.send_message(message.channel, "Error Executing Scraper")

    if message.content.startswith(prefix + "Creator"):
        s = requests.session()
        colorNum = randint(0, len(colorArray) - 1)
        color = colorArray[colorNum]

        actionheaders = {
            'Authorization': 'Bot {}'.format(token),
            'User-Agent': 'XO Discord Bot (https://xobots.io, v0.1)',
            'Content-Type': 'application/json'
        }
        actionlink = "https://discordapp.com/api/channels/{}/webhooks".format(message.channel.id)

        actiondata = {
            "name": "XO Discord Bot Creator Hook",
        }
        createwh = s.post(actionlink, headers=actionheaders, data=json.dumps(actiondata))
        webhookObject = json.loads(createwh.text)
        whid = webhookObject['id']
        whtoken = webhookObject['token']
        webhookurl = "https://discordapp.com/api/webhooks/{}/{}".format(whid, whtoken)
        embed = Webhook(webhookurl, color=color)
        embed.set_author(name='OX Discord Bot')
        embed.set_desc('This Is A Discord Bot Focused Around Sneakers Made By XO')
        embed.add_field(name="XO's Github URL", value='https://github.com/TCWTEAM')
        embed.add_field(name="This Projects Github Repo", value='https://github.com/TCWTEAM/OX-Discord-Bot')
        embed.set_thumbnail('https://i.gyazo.com/b6c555781abae4b1c6719242589c7f50.png')
        embed.add_field(name="XO's Twitter", value='https://twitter.com/ehxohd')
        embed.add_field(name="Want To Buy Me Lunch?", value="https://www.paypal.me/EHXOH")
        embed.set_footer(text='XO Discord Bot | 2018', ts=True)
        embed.post()

        actionurl = "https://discordapp.com/api/webhooks/{}".format(whid)
        s.delete(actionurl, headers=actionheaders)

    if message.content.startswith(prefix + "IsShopify"):
        if len(message.content.split(" ")) != 2:
            await client.send_message(message.channel, "Invalid Number Of Arguemts")
        elif "http" not in message.content.split(" ")[1]:
            await client.send_message(message.channel, "Invalid Url")
        else:
            try:

                s = requests.session()
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
                }
                sitesource = s.get(message.content.split(" ")[1], headers=headers, timeout=15)
                if "Shopify" not in sitesource.text:
                    await client.send_message(message.channel, "{} Is Not Shopify".format(message.content.split(" ")[1]))
                else:
                    await client.send_message(message.channel, "{} IS PROBABLY SHOPIFY".format(message.content.split(" ")[1]))
            except:
                await client.send_message(message.channel, "Error Checking Site, Probably Rejected The Request")


    if message.content.startswith(prefix + "getproducts"):
        if len(message.content.split(" ")) < 2:
            await client.send_message(message.author, "Invalid Number Of Arguments")
        elif "http" not in message.content.split(" ")[1]:
            await client.send_message(message.author, "The URL You Gave Isnt Valid")
        else:
            url = message.content.split(" ")[1]
            s = requests.session()
            pagesource = s.get(url, headers=globalHeaders, timeout=20)
            if "shopify" not in pagesource.text.lower():
                await client.send_message(message.author, "The Site Requested Doesnt Seem To Be Shopify")
            else:
                testUrlr = s.get(url + "products.json", headers=globalHeaders, timeout=30)

            testUrlInfo = testUrlr.text
            productObject = json.loads(testUrlInfo)
            savefilenum = str(randint(111, 333))
            fnamee = "{}_{}.txt".format(url.split("://")[1].split(".")[0], savefilenum)
            f = open(fnamee, "w+")
            f.close()
            f = open(fnamee, "a+")
            f.write("SCRAPED BY XOS DISCORD BOT\n")
            f.write("Twitter: @ehxohd | Discord: XO#0001 | Paypal: https://paypal.me/ehxoh\n")
            f.write("=========================================\n")
            f.write("Info: \nSite Url:{}\nProduct Object URL:{}\n".format(url, url + "products.json"))
            f.write("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            sitebaseurl = url.split("/")[2]
            for product in productObject['products']:
                f.write("=====================\n")
                name = product['title']
                f.write("Product Name: {}\n".format(name))
                f.write("Sizes And ATCS:\n")
                for variant in product['variants']:
                    f.write("----------------\n")
                    variantid = variant['id']
                    varname = variant['title'].replace("\/", "")
                    atclink = "{}/cart/{}:1".format(sitebaseurl, variantid)
                    f.write("VariantID: {}\n".format(variantid))
                    f.write("Size/Style: {}\n".format(varname))
                    f.write("ATC Link: {}\n".format(atclink))
                    f.write("----------------\n")
                f.write("=====================\n")

            f.write("END OF FILE\n")
            f.close()
            fc = open(fnamee, "r")
            fcc = fc.read()
            fc.close()


            textURL = hastebin.post(fcc)
            await client.send_message(message.author, "I Finished Scraping Your Sites. Heres What I Got\n{}".format(textURL))
            os.remove(fnamee)


    if message.content.startswith(prefix + "help"):
        helpf = open("helpMessage.xo", "r")
        helpMessage = helpf.read()
        helpf.close()
        await client.send_message(message.author, "Hi Heres Some Help\nPrefix:{} (Goes Before All Commands){}".format(prefix, helpMessage))
        await client.send_message(message.channel, "@{} I Sent Help To Your DM's".format(message.author))

    if message.content.startswith(prefix + "randomquote"):
        lines = open('quotes.xo', encoding="utf8").read().splitlines()
        myline = random.choice(lines)
        await client.send_message(message.channel, myline)

    if message.content.startswith(prefix + "online?"):
        if len(message.content.split(" ")) != 2:
            await client.send_message(message.channel, "Invalid Amount Of Arguments")
        elif "http" not in message.content.split(" ")[1]:
            await client.send_message(message.channel, "Invalid Url")
        else:
            try:
                r = requests.get(message.content.split(" ")[1], timeout=30)
                if str(r.status_code).startswith("20"):
                    await client.send_message(message.channel, "{} Is Online".format(message.content.split(" ")[1]))
                else:
                    await client.send_message(message.channel, "{} Is Offline Or Not Found".format(message.content.split(" ")[1]))
            except:
                await client.send_message(message.channel, "{} Is Offline Or Not Found".format(message.content.split(" ")[1]))

    if message.content.startswith(prefix + "SupremeWeek"):
        pageSource = requests.get("https://www.supremecommunity.com/season/spring-summer2018/droplists/")
        pageSource = pageSource.content
        soup = bs(pageSource, "html.parser")
        links = soup.find_all('a', {'class':'block'})[0]
        link = "https://www.supremecommunity.com" + str(links).split('href="')[1].split('">')[0]
        await client.send_message(message.channel, "Hey My Supreme Features Arent Finished But I Found The Link Of The Latest Stuff {}".format(link))

    if message.content.startswith(prefix + "SupremeProducts"):
        url = "http://www.supremenewyork.com/mobile_stock.json"
        s = requests.session()
        supremeStock = s.get(url)
        print(supremeStock.text)
        so = supremeStock.text.encode('UTF-8')
        supremeObject = json.loads(so)
        fnameu = "supreme_{}.txt".format(str(randint(111, 999)))
        f = open(fnameu, "w+")
        f.close()
        f = open(fnameu, "a+")
        f.write("SUPREME PRODUCT SCRAPER\n")
        f.write("OX Discord Bot BY XO\n")
        f.write("Github https://github.com/TCWTEAM/OX-Discord-Bot | Twitter: @ehxohd\n")
        f.write("=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=\n")
        f.write("Release Date: {} | Release Week: {}\n".format(supremeObject['release_date'], supremeObject['release_week']))
        f.write("\n")
        f.write("\n")
        f.write("==================\n")
        f.write("[Bags]\n")
        for item in supremeObject['products_and_categories']['Bags']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")
        f.write("\n")
        f.write("[Accessories]\n")
        for item in supremeObject['products_and_categories']['Accessories']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")
        f.write("\n")
        f.write("[Skate]\n")
        for item in supremeObject['products_and_categories']['Skate']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")
        f.write("\n")
        f.write("[Shirts]\n")
        for item in supremeObject['products_and_categories']['Shirts']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")

        f.write("\n")
        f.write("[Pants]\n")
        for item in supremeObject['products_and_categories']['Pants']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")

        f.write("\n")
        f.write("[Jackets]\n")
        for item in supremeObject['products_and_categories']['Jackets']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")

        f.write("\n")
        f.write("[Shorts]\n")
        for item in supremeObject['products_and_categories']['Shorts']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")
        f.write("\n")
        f.write("[Sweatshirts]\n")
        for item in supremeObject['products_and_categories']['Sweatshirts']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")

        f.write("\n")
        f.write("[Tops/Sweaters]\n")
        for item in supremeObject['products_and_categories']['Tops/Sweaters']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")
        f.write("\n")
        f.write("[Hats]\n")
        for item in supremeObject['products_and_categories']['Hats']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")

        f.write("\n")
        f.write("[new]\n")
        for item in supremeObject['products_and_categories']['new']:
            name = item['name']
            id = item['id']
            imageURL = item['image_url_hi'].split("//")[1]
            price = "${}".format(int(item['price'])/100)
            f.write("------------\n")
            f.write("Name: {}\n".format(name))
            f.write("PID: {}\n".format(id))
            f.write("Price: {}\n".format(price))
            f.write("Image URL: http://{}\n".format(imageURL))
            f.write("-------------\n")

        f.close()
        f = open(fnameu, "r")
        uploadURL = hastebin.post(f.read())
        f.close()
        await client.send_message(message.channel, "I Finished Looking At Supreme. This Season Sucks But Here Are The Products On The Site {}".format(uploadURL))




@client.event
async def on_ready():

    print("BOT LAUNCHED")
    print("By XO")
    lines = open('quotes.xo', encoding="utf8").read().splitlines()
    myline = random.choice(lines)
    await client.change_presence(game=discord.Game(name=myline, url="https://twitch.tv/twitch", type=1))
    with open('img\zodis.png', 'rb') as f:
        await client.edit_profile(avatar=f.read())
    f.close()





client.run(token)
