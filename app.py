import os, sys
from flask import Flask, request
from utils import wit_response, get_news_elements
from utils2 import wit_response2, get_ms_elements
from pymessenger import Bot
import random

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAACRykAYGRYBAOsm3BZBPL1PHNMjl6DNWyLW45CBIO47qvAG47RhhWFt9Ma9shOrq1S65u892SBw5p227UMZBEIzrgbfiSCOF0ZCnJzEV4vNsVzHmqNXZCCoAl91MVuEZBb0wvg6yMgwZAOGsj0f1LxaUY55u1gsPHcWhG15B52jxk59yv3tW5"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "ready":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'


					entity, value = wit_response2(messaging_text)
					if entity == 'hello':
						response="你可以輸入 __(地區)密室 來找尋地方密室逃脫工作室的資訊"
						response1="輸入 其它 了解其它功能或是輸入 抽正咩 來抽一張正咩圖!哈哈"
						bot.send_text_message(sender_id, messaging_text)
						bot.send_text_message(sender_id, response)
						bot.send_text_message(sender_id, response1)
					if entity == 'msaction':
						response = "請依照格式輸入揪團內容"
						response1 = "範例：主題,時間,人數"						
						bot.send_text_message(sender_id, response)
						bot.send_text_message(sender_id, response1)
					if entity == 'mstype':
						response = "這是 {} 的資訊.".format(str(value))
						elements2 = get_ms_elements(value)
						bot.send_generic_message(sender_id, elements2)
						if (value == "抽正咩"):
							picture = ["https://i.imgur.com/qKkE2bj.jpg","https://i.imgur.com/QjMLPmx.jpg",
           								"https://i.imgur.com/HefBo5o.jpg","https://i.imgur.com/AjxWcuY.jpg",
										"https://i.imgur.com/3vDRl4r.jpg","https://i.imgur.com/3qSGcKT.jpg",
										"https://i.imgur.com/ZbdV9Nz.jpg","https://i.imgur.com/oAkIJmH.jpg",
										"https://i.imgur.com/MtcwDtD.jpg","https://i.imgur.com/qre60t1.jpg",
										"https://i.imgur.com/Yrvc7LV.jpg","https://i.imgur.com/4wJXl4D.jpg",
										"https://i.imgur.com/71suURR.jpg","https://i.imgur.com/2cdURNa.jpg",
										"https://i.imgur.com/fHBf685.jpg"]
							c=random.choice(picture)
							bot.send_image_url(sender_id,c)
					elif entity == 'newstype':
						response = "這是 {} 新聞".format(str(value))
						categories = wit_response(messaging_text)
						elements = get_news_elements(categories)
						bot.send_generic_message(sender_id, elements)
					else:
						print(messaging_text[0])

				elif messaging_event.get("postback"):
					if messaging_event['postback'].get('payload'):
						messaging_text = messaging_event['postback']['payload']
					else:
						messaging_text = 'no text'
					categories = wit_response(messaging_text)
					elements = get_news_elements(categories)
					bot.send_generic_message(sender_id, elements)
	
	return "ok", 200
					

	


def log(message):
	print(message)	
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)
