import json
from PIL import Image, ImageDraw, ImageFont
import os
import os.path
from pathlib import Path
import textwrap
#read file

thefile= open('Placement/jsonfiles/aathicudi.json','rb')
jsondata= thefile.read()

#parse

object = json.loads(jsondata)

mylist = object['athisudi']

#image_path = "Placement/images"


thislist = []
thislist = thislist.sort()
for i in range(len(mylist)):
    poem = mylist[i].get("poem")
    print(poem)
    paraphrase = mylist[i].get("paraphrase")
    translation = mylist[i].get("translation")
    # thislist.append(mylist[i].get("state"))

    img = Image.open('Placement/aathichoodi_template.png')
    width = img.width
    height = img.height
    #print("Image width: ", width)

    draw = ImageDraw.Draw(img)
    #fnt = ImageFont.truetype("st_024.tff",90, layout_engine=ImageFont.LAYOUT_RAQM)
    #fnt2 = ImageFont.truetype("latha.ttf", 50, layout_engine=ImageFont.LAYOUT_RAQM)
    # fnt = ImageFont.truetype("Arial", 15)
    fnt = ImageFont.truetype("Placement/akshar.TTF", 50)
    margin = offset = 40
    for line in textwrap.wrap(poem, width=900):
        draw.text((margin, offset), line,(width/2,height/4), poem, font= fnt, fill = (0,0,0), anchor="ma")
        offset += fnt.getsize(line)[1]
    for line in textwrap.wrap(paraphrase, width=900):
        draw.text((margin, offset), line,(width / 2, height / 2), paraphrase, font= fnt, fill=(0, 0, 0), anchor="ma")
        offset += fnt.getsize(line)[1]
    for line in textwrap.wrap(translation, width=900):
        draw.text((margin, offset), line,(width / 2, height*0.75), translation, font= fnt,fill=(0, 0, 0), anchor="ma")
        offset += fnt.getsize(line)[1]
    img.save("Placement/images/new%s.png" % i)

    if i == 4:
        my_file = Path("Placement/images/new%s.png") 
        if my_file.is_file():
            print("replace")
        else:
            print("okay")
        break

    print(i+1)
    
print("done")



