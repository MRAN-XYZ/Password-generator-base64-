import base64
import random

text = input("Text to password: ")
print(text)
dijit = int(input("Digit: "))
print(dijit)

available_chars = "ajoenxDO790"

yn = False

while len(text) < dijit:
    textplus = ''.join(random.sample(available_chars, 1))
    text += textplus
    yn = True

if len(text) > dijit:
    text = text[:dijit]
    yn = True

text_b = text.encode('utf-8')

base64_b = base64.b64encode(text_b)

base64_txt = base64_b.decode('utf-8')

base64_txtn = base64_txt.replace('=', '1').replace('&', 'q').replace(' ', '').replace('.', '').replace('V', 'k').replace('-', '_').replace('*', '').replace('m', '0')

base64_txtne = base64_txtn[:dijit]

print('')
print("text", text)
print('')
if yn:
    print("           ∆ modified ∆")

print('')
if yn:
    print('The name is modified because the number of characters is different from the desired digit')

print('')

print("Password (modified base64):", base64_txtne)
