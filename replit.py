## Introduction About This Programming Language:


























































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
    "creator"
]

LETTERS=string.ascii_letters
LETTERS_DIGITS=LETTERS+DIGITS

memory={}


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
        





class Test:
    def __init__(self,type,value):
        self.type=type
        self.value=value


class NumberNode:
    name="number"
    def __init__(self,token):
        self.token=token
        self.leftNode=None
        self.rightNode=None
        
    def __repr__(self):
        return f"({self.token})"
class BinOperationNode:
    name="Binary"
    def __init__(self,leftNode,OpsNode,rightNode):
        self.leftNode=leftNode
        self.rightNode=rightNode
        self.OpsNode=OpsNode
    def __repr__(self):
        return f"({self.leftNode},{self.OpsNode},{self.rightNode})"
class UnaryOperationNode:
    name="UnaryOpNode"
    def __init__(self,op_token,node):
        self.op_token=op_token
        self.token=node
    def __repr__(self):
        return f"({self.op_token},{self.token})"
    
class IfNode:
    name="IfNode"
    def __init__(self,cases,else_case):
        self.cases=cases
        self.else_case=else_case
    def __repr__(self):
        return (f"{self.cases} and {self.else_case}")


class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.token_pos=-1
        self.curr_Token=None
        self.memory={}
        self.curr_ID=None
        self.visit=1
        self.advance()
    def advance(self):
        self.token_pos+=1

        if self.token_pos<len(self.tokens):
            self.curr_Token=self.tokens[self.token_pos]
            
            
            
        return self.curr_Token
    


    def factor(self):
        tok=self.curr_Token

        if tok.type==TT_IDENTIFIER:
            digit=memory[tok.value]
            tok2=Test("INT",digit)
            self.advance()
            return NumberNode(tok2)

        if tok.type==TT_LPAREN:
            self.advance()
            exppr=self.expr()
            if self.curr_Token.type==TT_RPAREN:
                self.advance()
                return exppr
            else:
                pass

        if tok.type in (TT_MINUS,TT_PLUS):
            ops_token=tok
            self.advance()
            factor=self.factor()
            return UnaryOperationNode(ops_token,factor)
        
        if tok.type in (TT_INT,TT_FLOAT):
            self.advance()
            return NumberNode(tok)
    
    
    

    ###This is  a reccursive approach :
    def term(self):
        return self.BinaryOps(self.factor,(TT_DIV,TT_MUL))
    

    def arith_expr(self):
        return self.BinaryOps(self.term,(TT_PLUS,TT_MINUS))
    


    def comp_expr(self):
        return self.BinaryOps(self.arith_expr,(TT_EE,TT_GT,TT_GTE,TT_LT,TT_LTE,TT_NE))
    

    def if_expr(self):
        cases=[]
        else_case=None
        self.advance()

        condition=self.expr()

        if not self.curr_Token.matches("KEYWORD","then"):
            print("Look's Like you haven't included 'then' keyword this may end up in an unexpected result")
        self.advance()
        expr=self.expr()

        cases.append((condition,expr))

        while self.curr_Token.matches(TT_KEYWORD,"elif"):
            self.advance()
            condition=self.expr()
            if not self.curr_Token.matches("KEYWORD","then"):
                print("Look's Like you haven't included 'then' keyword this may end up in an unexpected result")
            self.advance()

            expr=self.expr()

            cases.append((condition,expr))
        if self.curr_Token.matches(TT_KEYWORD,"else"):
            self.advance()

            expr=self.expr()

            else_case=expr
        
        # print(cases)
        # print(else_case)
        return IfNode(cases,else_case)

            



    
    def expr(self):

        if self.curr_Token.matches("KEYWORD","if"):
            if_expr=self.if_expr()
            return if_expr

        if self.curr_Token.type==TT_IDENTIFIER:
            return self.BinaryOps(self.term,(TT_PLUS,TT_MINUS))
        
        if self.curr_Token.matches("KEYWORD","save"):
            self.advance()
            if self.curr_Token.type==TT_IDENTIFIER:
                self.curr_ID=self.curr_Token.value
                memory[self.curr_ID]=0
                self.advance()
                self.advance()
                self.visit+=1
                expr=self.expr()
                memory[self.curr_ID]=Interpreter().recursive_Calc(expr)

                
                return expr



        
        return self.BinaryOps(self.comp_expr,((TT_KEYWORD,"and"),(TT_KEYWORD,"or")))

    def BinaryOps(self,func,Operator):
        left=func()

        while self.curr_Token.type in Operator or (self.curr_Token.type,self.curr_Token.value) in Operator:
            op_Node=self.curr_Token
            self.advance()
            right=func()
            left=BinOperationNode(left,op_Node,right)
        return left
    



###This is a much simpler version .Here I was actually trying to make it a lot more simpler that's all by the way:

    # def term(self):
    #     left=self.factor()

    #     while self.curr_Token.type in (TT_DIV,TT_MUL):
    #         op_Node=self.curr_Token
    #         self.advance()
    #         right=self.factor()
    #         left=BinOperationNode(left,op_Node,right)
    #     return left
    

    # def expr(self):
    #     left=self.term()

    #     while self.curr_Token.type in (TT_PLUS,TT_MINUS):
    #         op_Node=self.curr_Token
    #         self.advance()
    #         right=self.term()
    #         left=BinOperationNode(left,op_Node,right)
    #     return left
    
    def parse(self):   
        res=self.expr()
        
        return res
    


class Interpreter:
    def __init__(self):
        pass


    def recursive_Calc(self,node):
        # print(node.leftNode.token.value)
        # print(node.OpsNode)
        if node.name=="number":
            return node.token.value
        # if node.leftNode==None and node.rightNode==None:
        #     return node.token.value
        if node.name=="UnaryOpNode":
            if node.op_token=="PLUS":
                return self.recursive_Calc(node.token)
            else:
                return -self.recursive_Calc(node.token)
            
        
        if node.name=="IfNode":

            for condition,expr in node.cases:
                condition_value=self.recursive_Calc(condition)

                if condition_value==True:
                    expr_value=self.recursive_Calc(expr)
                    return expr_value
                
            if node.else_cases:
                else_value=self.recursive_Calc(node.else_case)
                return else_value
            
            return None

       
        
        if node.OpsNode.type==TT_PLUS:
            return self.recursive_Calc(node.leftNode) + self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_MUL:
            return self.recursive_Calc(node.leftNode) * self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_DIV:
            return self.recursive_Calc(node.leftNode) / self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_MINUS:
            return self.recursive_Calc(node.leftNode) - self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_GT:
            return self.recursive_Calc(node.leftNode) > self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_LT:
            return self.recursive_Calc(node.leftNode) < self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_LTE:
            return self.recursive_Calc(node.leftNode) <= self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_GTE:
            return self.recursive_Calc(node.leftNode) >= self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_EE:
            return self.recursive_Calc(node.leftNode) == self.recursive_Calc(node.rightNode)
        if node.OpsNode.value=="and":
            return self.recursive_Calc(node.leftNode) and self.recursive_Calc(node.rightNode)
        if node.OpsNode.value=="or":
            return self.recursive_Calc(node.leftNode) or self.recursive_Calc(node.rightNode)
        
        

RED = '\033[91m'
RESET = '\033[0m'
GREEN = '\033[92m'
from pyfiglet import Figlet
 
f = Figlet(font='slant')
name = f.renderText('TengenScript')
print(name)
print("")
print(f">This project is just to Learn  {RED}OOP{RESET}")
print("")

print(GREEN +"Why so serious!!" + RESET)
print("")

while True:
    text=input("TengenScript >")
    if not text:
        continue
    newLexer=Lexer("<Terminal>",text)
    tokens,error=newLexer.make_tokens()
    if error:
        print(f"{RED} {error} {RESET}")
    else:
        print(tokens)
        # print(Parser(tokens).parse())
        parsedRes=Parser(tokens).parse()
        res=Interpreter().recursive_Calc(parsedRes)
        print(res)

    