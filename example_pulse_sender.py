from dispatchers.utils import ZmqSender
import time
import base64
from pprint import pprint 


with open("example_image.png", "rb") as image_file:
	img = base64.b64encode(image_file.read())
	img = img.decode("utf-8")
	img = "data:image/png;base64,"+img


data = [
	{     
		'title': 'Test title, uid {}'.format(time.time_ns()),    
		'content': 'Test content, uid {}'.format(time.time_ns()),   
		'isPublic': 1, 
		'isPin': 0, 
		'attachments': [img]
		# 'attachments': []
	},     
]

z = ZmqSender( 'bfxpulse' )

# Send Data
for d in data:
	z.send_msg( d )
