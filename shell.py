import lexer
from pyfiglet import Figlet
from parser_1 import Parser
from interpreter import Interpreter


RED = '\033[91m'
RESET = '\033[0m'
GREEN = '\033[92m'
 
f = Figlet(font='slant')
einstein = f.renderText('TengenScript')
print(einstein)
print("")
print(f">This project is just to Learn  {RED}OOP{RESET}")
print("")

print(GREEN +"Why so serious!!" + RESET)
print("")

while True:
    text=input("TengenScript >")
    if not text:
        continue
    newLexer=lexer.Lexer("<Terminal>",text)
    tokens,error=newLexer.make_tokens()
    if error:
        print(F"{RED} {error} {RESET}")
    else:
        print(tokens)
  
        # print(lexer.Parser(tokens).parse())
        print(Parser(tokens).parse())
        parsedRes=Parser(tokens).parse()
        res=Interpreter().recursive_Calc(parsedRes)
        print(res)

