from Expression import *


class Context:
    def __init__(self):
        self.str_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.str_mini_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        self.str_huge_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.Expression_num = TerminalExpression(self.str_num)
        self.Expression_mini_alpha = TerminalExpression(self.str_mini_alpha)
        self.Expression_huge_alpha = TerminalExpression(self.str_huge_alpha)
        self.information = NonTerminalExpression(self.Expression_num, self.Expression_mini_alpha, self.Expression_huge_alpha)

    def Express(self, info):
        ok = self.information.interpret(info)
        if ok:
            print(f'The Expression is correct, Expression is: {info}')
        else:
            print(f'The Expression is incorrect, Expression is: {info}')
