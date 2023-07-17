
TT_INT="INT"
TT_FLOAT="FLOAT"
TT_PLUS="PLUS"
TT_MINUS="MINUS"
TT_MUL="MUL"
TT_DIV="DIV"
TT_LPAREN="LPAREN"
TT_RPAREN="RPAREN"
DIGITS="0123456789."









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
    def __init__(self,op_token,node):
        self.op_token=op_token
        self.node=node
    def __repr__(self):
        return f"({self.op_token},{self.node})"

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

        # if tok.type in (TT_INT,TT_PLUS):
        #     self.advance()
        #     return UnaryOperationNode()
        
        if tok.type in (TT_INT,TT_FLOAT):
            self.advance()
            return NumberNode(tok)
    
    
    

    ###This is  a reccursive approach :
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