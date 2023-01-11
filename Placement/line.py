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

object = json.loads(athisudi)

if "peom" in object:
    print("Key exist in JSON data")
   
else:
    print("Key doesn't exist in JSON data")

mylist = object['athisudi']

for i in range(len(mylist)):

    def draw_text_to_image(image,width,text, font,text_colour, text_start_height, stroke_colour):
        draw = ImageDraw.Draw(img)
        image_width, image_height = image.size
        y_text = text_start_height
        lines = textwrap.wrap(text, width=15)
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text(((image_width - line_width) / 2, y_text), line, font=font, 
            fill = text_colour, stroke_width=2,stroke_fill=stroke_colour)
            y_text += line_height
        
    ###### Retrieving the text from the json file ######

    peom = mylist[i].get("poem")
    paraphrase = mylist[i].get("paraphrase")
    translation = mylist[i].get("translation")
    
    

    if peom == "":
        peom = "No text provided"
    if paraphrase == "":
        paraphrase = "No text provided"
        
        

    print("length: ",len(paraphrase))

    fontsize= 120

    if len(paraphrase) >80:
        fontsize=80

    ###### opening the image template ######

    img = Image.open('Placement/aathichoodi_template.png')
    width = img.width
    height = img.height
    #print("Image width: ", width)

    ###### Setting the colours ######

    peom_text_colour = "#7A0026"
    peom_stroke_colour = "#7A0026"
    paraphrase_text_colour = "#FCD92B"
    paraphrase_stroke_colour = "#7A0026"

    ###### setting the fonts ######

    #fnt = ImageFont.truetype("st_024.tff",90, layout_engine=ImageFont.LAYOUT_RAQM)
    #fnt2 = ImageFont.truetype("latha.ttf", 50, layout_engine=ImageFont.LAYOUT_RAQM)
    # fnt = ImageFont.truetype("Arial", 15)

    fnt_peom = ImageFont.truetype("Placement/akshar.TTF", 120)
    fnt_paraphrase = ImageFont.truetype("Placement/akshar.TTF", fontsize)
    
    ###### Drawing the text onto the image ######

    # draw.text((width/2,height/4), peom, font= fnt, fill = (0,0,0), anchor="ma") 
    # draw.text((width / 2, height / 2), paraphrase, font= fnt, fill=(0, 0, 0), anchor="ma") 
    # draw.text((width / 2, height*0.75), translation, font= fnt,fill=(0, 0, 0), anchor="ma")

    draw_text_to_image(img,width,peom,fnt_peom,peom_text_colour,height/4,paraphrase_stroke_colour )
    draw_text_to_image(img,width,paraphrase,fnt_paraphrase,paraphrase_text_colour,height/2.5, paraphrase_stroke_colour)
    #draw_text_to_image(img,translation,fnt,height*0.75)

    ###### Saving the image ######
    img.save("Placement/images/new%s.png" % i)

    # if i == 5:
    #     my_file = Path("Placement/images/new%s.png") 
    #     if my_file.is_file():
    #         print("replace")
    #     else:
    #         print("okay")
    #     break

    print(i+1)
    
print("Images Successfully created")



