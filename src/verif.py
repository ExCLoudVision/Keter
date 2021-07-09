from gtts import gTTS
from io import BytesIO
from discord import File
from random import choice
from string import ascii_lowercase, digits
from asyncio import sleep
import threading
import time
import asyncio
codeuser = ""
chars = []
for a in ascii_lowercase:
    chars.append(a)
def generate_code():
    buf = ""
    for x in range(6):
        buf += " "
        buf += choice(str(digits))
        buf += " "
    return buf
delet = []
async def code_verify(channel):
    code = generate_code()
    f = BytesIO()
    code_file = gTTS(text=code.lower() lang='fr', slow=True)
    code_file.write_to_fp(f)
    f.seek(0)
    fichier_say = File(f, "captcha.mp3")
    msg = await channel.send(file=fichier_say)
    codeuser = code.replace(".", "")
    print(codeuser)
    delet.append(msg)
    return code.replace(" ","")
def get_code():
    return codeuser
async def delete():
    for x in delet:
        await x.delete()
        delet.remove(x)
