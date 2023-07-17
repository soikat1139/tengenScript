



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
    def __init__(self,pos_start,pos_end,details):
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
    def make_tokens(self):
        tokens=[]

        while self.current_char !=None:
            if self.current_char in " ":
                self.advance(self.current_char)

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
            elif self.current_char in DIGITS:
                tokens.append(self.makeDigits())
                
            else:
                pos_start=self.pos.copy()
                char=self.current_char
                self.advance()

                return [],IllegalCharError(pos_start,self.pos,char).as_string()
       
        return tokens,None
    
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
        



###Nimber Node

class NumberNode:
    def __init__(self,token):
        self.token=token
    def __repr__(self):
        return f"{self.token}"
class BinOperationNode:
    def __init__(self,leftNode,OpsNode,rightNode):
        self.leftNode=leftNode
        self.rightNode=rightNode
        self.OpsNode=OpsNode
    def __repr__(self):
        return f"({self.leftNode},{self.OpsNode},{self.rightNode})"

class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.token_pos=-1
        self.curr_Token=None
        
        self.advance()
    def advance(self):
        self.token_pos+=1

        if self.token_pos<len(self.tokens):
            self.curr_Token=self.tokens[self.token_pos]
            
            
            
        return self.curr_Token
    


    def factor(self):
        tok=self.curr_Token
        
        if tok.type in (TT_INT,TT_FLOAT):
            self.advance()
            return NumberNode(tok)
    
    
    
    def term(self):
        return self.BinaryOps(self.factor,(TT_DIV,TT_MUL))
    
    def expr(self):
        return self.BinaryOps(self.term,(TT_PLUS,TT_MINUS))

    def BinaryOps(self,func,Operator):
        left=func()

        while self.curr_Token.type in Operator:
            op_Node=self.curr_Token
            self.advance()
            right=func()
            left=BinOperationNode(left,op_Node,right)
        return left
    
    def parse(self):
        
        
        res=self.expr()
        
        return res

    


