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


class Interpreter:
    def __init__(self):
        pass


    def recursive_Calc(self,node):
        # print(node.leftNode.token.value)
        # print(node.OpsNode)
        if not node:
            return
        
        if node.name=="funcNode":
            return node
        
        if node.name=="number":
            return node.token.value
        
        if node.name=="string":
            response=""

            if len(node.token)==1:
                return node.token[0].value

            for nodes in node.token:
                response+=nodes.value
                response+=" "


            return response
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
            
          
            if node.else_case:
                else_value=self.recursive_Calc(node.else_case)
                return else_value
            
            return "Nothing to show"

       
        
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
        
        

