from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

import requests
import random
import linecache
from lxml import etree


wordpa='/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/a[1]/div/text()'
brepa='/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/span[2]/div[1]/span/text()'
amepa='/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/span[2]/div[2]/span/text()'
definpa='//span[@class="def"]/text()'
ranwopa='//*[@class="top-g"]/li'

baseurl="https://www.oxfordlearnersdictionaries.com/definition/english/"

headers = {
    	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
	}
baseurl="https://www.oxfordlearnersdictionaries.com/"

def dayword():
	#寻找今日单词
	
	res1 = requests.get(url=baseurl,headers=headers).text
	word = str(etree.HTML(res1).xpath(wordpa))
	wordurl= baseurl + word.split("'")[1]
	#获取单词页
	res2 = requests.get(url=wordurl,headers=headers).text
	#英音
	phonbre = etree.HTML(res2).xpath(brepa)
	#美音
	phoname = etree.HTML(res2).xpath(amepa)
	#词义
	defin = etree.HTML(res2).xpath(definpa)
	final = "单词:{0}\n带不列颠发音:{1}\n阿美利卡发音:{2}\n释义:{3}".format(word,phonbre,phoname,defin)
	return final

word = on_command("word", aliases={'单词', 'word'}, priority=5)

@word.handle()
async def handle_receive(bot: Bot, event: Event):

	dayout = dayword()
	await word.finish(Message(f'{dayout}'))