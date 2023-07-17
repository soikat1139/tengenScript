# from art import *
 
# einstein = text2art("Einstein")
# print(einstein)


# from art import *
 
# einstein = text2art("Einstein")

# print(einstein)
from pyfiglet import Figlet
 
f = Figlet(font='slant')
einstein = f.renderText('TengenScript')
print(einstein)

class Token:
    name="Token"
    def __init__(self,value):

        self.value=value

tok=Token()

print(tok)