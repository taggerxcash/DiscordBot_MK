import os
import requests
from PIL import Image

imgs = {
    "vs_bg": "./img/vs_bg.jpg",
    
}

async def vs_create(url1:str, url2:str):
    vs_bg = Image.open(os.path.join(imgs["vs_bg"]))
    
    size = (175, 175)

    f1 = Image.open(requests.get(url1, stream = True).raw).resize(size)
    f2 = Image.open(requests.get(url2, stream = True).raw).resize(size)

    pos1 = (vs_bg.width//2 - f1.width*2, vs_bg.height//2 - f1.height//2)
    pos2 = (vs_bg.width//2 + f2.width, vs_bg.height//2 - f1.height//2)

    vs_bg.paste(f1, pos1)
    vs_bg.paste(f2, pos2)

    vs_bg.save(os.path.join("./img", "result.png"))