# Creating the image for our tweets
from PIL import Image, ImageFont, ImageDraw
import textwrap


def imagify_tweet(tweets):
	for index, tweet in enumerate(tweets):

		#Open the image, set the font, and ready for edits.
		img = Image.open('trump_exec_order.jpg')
		font = ImageFont.truetype("./Arial.ttf", 18)
		draw = ImageDraw.Draw(img)

		#Define textwrap and set axis settings for placement
		lines = textwrap.wrap(tweet['text'], width=20)
		x_axis = 380
		y_axis = 290

		#Hacky thing to get write text wrap (bad library design). Iterates through and writes each line.
		for line in lines:
			width, height = font.getsize(line)
			draw.text((x_axis,y_axis), line, font = font, fill = (0,0,0,1))
			y_axis += height

		#Apply changes and write to disk.
		draw = ImageDraw.Draw(img)
		img.save('trump_exec_order_{0}.jpg'.format(index))
