from PIL import Image, ImageDraw, ImageFont
from datetime import datetime as d

def generateCertificate(userid, finalscore):
    year, month, day = str(d.now()).split('.')[0].split(' ')[0].split('-')
    date = "-".join([day, month, year])

    sql = "SELECT cast(avg(testscore)as decimal(10,2)) as final FROM `scores` where userid = 1"
    signature = "{}-DC/Cert/SCR/{}".format(userid, finalscore)

    name = sys.argv[1]
    if len(name) <= 18:
        namelength = (len(name) / 1.3)
    else:
        namelength = len(name) * 2.6

    img = Image.open('award.jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("BrushScript.otf", 32)

    # Generating Title
    draw.text((220, 200), "Completing Diving Course", (50, 50, 50), font=font)

    # Generating Date
    draw.text((175, 370), date, (50, 50, 50), font=ImageFont.truetype("BrushScript.otf", 22))

    # Generating Signature
    draw.text((450, 370), signature, (50, 50, 50), font=ImageFont.truetype("consolai.ttf", 20))

    # Generating Name
    if len(name) <= 15:
        draw.text((260 + namelength, 300), name, (50, 50, 50), font=font)
    else:
        draw.text((260 - namelength, 300), name, (50, 50, 50), font=font)

    filename = '{}_Cert.jpg'.format(userid)
    img.save(filename)
    return filename
