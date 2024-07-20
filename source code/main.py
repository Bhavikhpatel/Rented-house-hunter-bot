from graphicCode import GUI
from propertyDealerWebsite import propertyWebsiteBot
from beautifulSoupFunc import scrapperBot
from sheetyBot import uploaderBot

gui = GUI()
gui.buildGUI()

bot = propertyWebsiteBot(gui.budget, gui.bhk, gui.location)
bot.openWebsite()
bot.fillInDetails()

scrapper = scrapperBot(bot.filledWebsiteTabURL)
scrapper.startScrapping()

uploader = uploaderBot(scrapper.areaList, scrapper.ownerList, scrapper.amountList, gui.websiteEntry)
uploader.initiateUploading()


bot.exitWebsite()
