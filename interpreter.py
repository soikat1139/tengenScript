



TT_INT="INT"
TT_FLOAT="FLOAT"
TT_PLUS="PLUS"
TT_MINUS="MINUS"
TT_MUL="MUL"
TT_DIV="DIV"
TT_LPAREN="LPAREN"
TT_RPAREN="RPAREN"
DIGITS="0123456789."


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
                return node.token.token.value
            else:
                return -node.token.token.value

       
        
        if node.OpsNode.type==TT_PLUS:
            return self.recursive_Calc(node.leftNode) + self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_MUL:
            return self.recursive_Calc(node.leftNode) * self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_DIV:
            return self.recursive_Calc(node.leftNode) / self.recursive_Calc(node.rightNode)
        if node.OpsNode.type==TT_MINUS:
            return self.recursive_Calc(node.leftNode) - self.recursive_Calc(node.rightNode)

