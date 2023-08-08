import string


####tHIS Projecct is great to learn Object Oriented Programming:::

#Variables:

TT_INT="INT"
TT_FLOAT="FLOAT"
TT_PLUS="PLUS"
TT_MINUS="MINUS"
TT_MUL="MUL"
TT_DIV="DIV"
TT_LPAREN="LPAREN"
TT_RPAREN="RPAREN"
DIGITS="0123456789."
TT_IDENTIFIER="IDENTIFIER"
TT_EQ="EQUAL"
TT_KEYWORD="KEYWORD"
TT_EE="EE"
TT_GT="GT"
TT_LT="LT"
TT_GTE="GTE"
TT_LTE="LTE"
TT_NE="NE"
TT_QUOTE="QUOTE"

KEYWORDS=[
    "Yuji",
    "yuji",
    "save",
    "and",
    "or",
    "if",
    "then",
    "elif",
    "else",
    "display",
    "tengen",
    "creator",
    "copyright",
    "Display"
]

LETTERS=string.ascii_letters
LETTERS_DIGITS=LETTERS+DIGITS


class Error:
    def __init__(self,pos_start,pos_end,errorName,details):
        self.pos_start=pos_start
        self.pos_end=pos_end
        self.errorName=errorName
        self.details=details
    def as_string(self):
        result=f"There might be an .Here Is the error Name : {self.errorName} and here Is the details: '{self.details}'"
        result+=f"File Name : {self.pos_start.fn} line :{self.pos_start.ln +1}"
        return result

class IllegalCharError(Error):
    def __init__(self,pos_start=1,pos_end=5,details=' '):
        super().__init__(pos_start,pos_end,"illegalCharError",details)
class IllegalSyntexError(Error):
    def __init__(self,pos_start=1,pos_end=5,details=''):
        super().__init__(pos_start,pos_end,"illegalCharError",details)


class Position:
    def __init__(self,idx,ln,col,fn,fctx):
        self.idx=idx
        self.ln=ln
        self.col=col
        self.fn=fn
        self.fctx=fctx
    def advance(self,current_char):
        self.idx+=1
        self.col+=1

        if current_char=='\n':
            self.ln+=1
            self.col=0
        return self
    def copy(self):
        return Position(self.idx,self.ln,self.col,self.fn,self.fctx)



class Token:
    def __init__(self,type_,value=None):
        self.type=type_
        self.value=value
    def matches(self,keyword,value):
        return keyword==self.type and self.value==value
    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        else:
            return f"{self.type}"

class Lexer:
    def __init__(self,fn,text):
        self.fn=fn
        self.text=text
        self.pos=Position(-1,0,-1,fn,text)
        self.current_char=None
        self.advance()
    

    def advance(self):
        self.pos.advance( self.current_char)
        self.current_char=self.text[self.pos.idx] if self.pos.idx<len(self.text) else None
    def bounceback(self):
        self.pos.idx-=1
        self.current_char=self.text[self.pos.idx]
    def make_tokens(self):
        tokens=[]

        while self.current_char !=None:
            if self.current_char in " ":
                self.advance()

            elif self.current_char=="+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char=="-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char=="*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char=="/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char=="(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char==")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char=='"':
                tokens.append(Token(TT_QUOTE))
                self.advance()
            elif self.current_char=="=":
                tokens.append(self.eq_maker())
                self.advance()
            elif self.current_char=="<":
                tokens.append(self.lt_maker())
                self.advance()
            elif self.current_char==">":
                tokens.append(self.gt_maker())
                self.advance()
            elif self.current_char=="!":
                tokens.append(self.not_maker())
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.makeDigits())
            elif self.current_char in LETTERS:
                tokens.append(self.makeIdentifier())
                
            else:
                pos_start=self.pos.copy()
                char=self.current_char
                self.advance()

                return [],IllegalCharError(pos_start,self.pos,char).as_string()
       
        return tokens,None
    

    def eq_maker(self):
        tok_type=TT_EQ

        self.advance()

        if self.current_char=="=":
            tok_type=TT_EE
        else:
            self.bounceback()

        return Token(tok_type)
    
    def not_maker(self):
        self.advance()

        if self.current_char=="=":
            return Token(TT_NE)
        
    def lt_maker(self):
        tok_type=TT_LT

        self.advance()

        if self.current_char=="=":
            tok_type=TT_LTE
        else:
            self.bounceback()

        return Token(tok_type)
    def gt_maker(self):
        tok_type=TT_GT

        self.advance()

        if self.current_char=="=":
            tok_type=TT_GTE
        else:
            self.bounceback()
        return Token(tok_type)
    


    def makeIdentifier(self):
        str=""

        while self.current_char!=None and self.current_char in LETTERS_DIGITS:
            str+=self.current_char
            self.advance()
        
        tok_type=TT_KEYWORD if str in KEYWORDS else TT_IDENTIFIER

        return Token(tok_type,str)

    
    def makeDigits(self):
        nums=""
        dots=0

        while self.current_char!=None and self.current_char in DIGITS:
            if self.current_char==".":
                if dots==1:break
                else:
                    dots+=1
                    nums=nums+"."
                    self.advance()
            else:
                nums=nums+self.current_char
                self.advance()
        if dots==1:
            return Token(TT_FLOAT,float(nums))
        else:
            return Token("INT",int(nums))
        


