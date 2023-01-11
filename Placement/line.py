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

image_path = "Placement/images"

for i in range(len(mylist)):

    def draw_text_to_image(image, text, font,text_colour, text_start_height, stroke_colour):
        draw = ImageDraw.Draw(img)
        image_width, image_height = image.size
        y_text = text_start_height
        lines = textwrap.wrap(text, width=15)
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text(((image_width - line_width) / 2, y_text), line, font=font, 
            fill = text_colour, stroke_width=2,stroke_fill=stroke_colour)
            y_text += line_height
        

    peom = mylist[i].get("poem")
    paraphrase = mylist[i].get("paraphrase")
    translation = mylist[i].get("translation")
    # thislist.append(mylist[i].get("state"))

    img = Image.open('Placement/aathichoodi_template.png')
    width = img.width
    height = img.height
    #print("Image width: ", width)

    peom_text_colour = "#7A0026"
    peom_stroke_colour = "#7A0026"
    paraphrase_text_colour = "#FCD92B"
    paraphrase_stroke_colour = "#7A0026"

   
    #fnt = ImageFont.truetype("st_024.tff",90, layout_engine=ImageFont.LAYOUT_RAQM)
    #fnt2 = ImageFont.truetype("latha.ttf", 50, layout_engine=ImageFont.LAYOUT_RAQM)
    # fnt = ImageFont.truetype("Arial", 15)
    fnt_peom = ImageFont.truetype("Placement/akshar.TTF", 120)
    fnt_paraphrase = ImageFont.truetype("Placement/akshar.TTF", 120)

    # draw.text((width/2,height/4), peom, font= fnt, fill = (0,0,0), anchor="ma") 
    # draw.text((width / 2, height / 2), paraphrase, font= fnt, fill=(0, 0, 0), anchor="ma") 
    # draw.text((width / 2, height*0.75), translation, font= fnt,fill=(0, 0, 0), anchor="ma")

    draw_text_to_image(img,peom,fnt_peom,peom_text_colour,height/4,paraphrase_stroke_colour )
    draw_text_to_image(img,paraphrase,fnt_paraphrase,paraphrase_text_colour,height/2.5, paraphrase_stroke_colour)
    #draw_text_to_image(img,translation,fnt,height*0.75)

    img.save("Placement/images/new%s.png" % i)

    # if i == 0:
    #     my_file = Path("Placement/images/new%s.png") 
    #     if my_file.is_file():
    #         print("replace")
    #     else:
    #         print("okay")
    #     break

    print(i+1)
    
print("done")



