from interpreter import Interpreter
import string



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
    name="if_Node"
    def __init__(self,cases,else_case):
        self.cases=cases
        self.else_case=else_case
    # def __repr__(self):
    #     return (f"{self.cases} and {self.else_case}")


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
        
        print(cases)
        print(else_case)
        return IfNode(cases,else_case)

            



    
    def expr(self):

        if self.curr_Token.matches("KEYWORD","if"):
            if_expr=self.if_expr()
            return if_expr()

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