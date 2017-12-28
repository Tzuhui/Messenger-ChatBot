from wit import Wit 
import random

wit_access_token = "YOUR_WIT.AI_TOKEN"
client = Wit(access_token = wit_access_token) 

def wit_response2(message_text):
	resp = client.message(message_text)
	
	entity = None
	value = None

	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass

	return (entity, value)
def get_ms_elements(value):
	elements2 = []
	if (value == "台南密室"):
		ms_items=[
		{'title':'神不在場密室逃脫工作室','link':'http://www.taog-game.com/','img':'https://pic.pimg.tw/khushi/1472318186-3647719915.jpg?v=1472318964','link2':'http://www.taog-game.com/booking/'},
		{'title':'密室逃脫許多門實境解謎團體動力工作坊','link':'http://www.doorsss.com/','img':'https://accupassv3storage.blob.core.windows.net/userupload/cdfe1477b9f1476d95e1202124157a66.jpg','link2':'https://www.facebook.com/TCDOORSSS/'}
		]
		
		for item in ms_items:
			element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "官方網站",
								'url': item['link2']
					},{
								'type': 'web_url',
								'title': "點我預約",
								'url': item['link2']
					}],	
					'image_url': item['img']
			}
			elements2.append(element)
	if (value == "高雄密室"):
		ms_items=[
		{'title':'夢罟密室逃脫工作室','link':'https://dreamcatcher311313.wixsite.com/mysite','img':'https://simplybook.asia/uploads/dreamcatcher0721/image_files/original/9e307f3d9ce3b423eec3673262e3d7f3.jpg','link2':'https://dreamcatcher311313.wixsite.com/mysite/booking'},
		{'title':'canpass密室逃脫','link':'http://canpass.com.tw/','img':'https://goo.gl/MEspCT','link2':'http://canpass.com.tw/book.html'},
		{'title':'逃出香港!台灣高雄站','link':'http://www.freeing.tw/','img':'http://common1.qyerstatic.com/bbs/remoteimages/92/929cdfb160541b999b44205d2798bbb0.jpg','link2':'http://booking.freeing.tw/'},
		{'title':'羊逃真人密室逃脫','link':'http://www.runsheepsrun.com/','img':'https://pic.pimg.tw/roger5050/1505371300-3674825204.jpg','link2':'http://www.runsheepsrun.com/activity.php?lang=tw'}
		]
		
		for item in ms_items:
			element = {
					'title': item['title'],
					'buttons': [{
								'type': 'web_url',
								'title': "官方網站",
								'url': item['link2']
					},{
								'type': 'web_url',
								'title': "點我預約",
								'url': item['link2']
					}],	
					'image_url': item['img']
			}
			elements2.append(element)
	if (value == "其它"):
		element = {
					'title': "可以看看新聞喔!!!",
					'buttons': [{
								'type': 'postback',
								'title': "娛樂新聞",
								'payload': '娛樂新聞'
					},{
								'type': 'postback',
								'title': "體育新聞",
								'payload': '體育新聞'
					},{
								'type': 'postback',
								'title': "科技新聞",
								'payload': '科技新聞'
					}]	
			}
		elements2.append(element)
	return elements2
	
	
