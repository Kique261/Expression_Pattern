from abc import ABC, abstractmethod


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, info):
        pass


class TerminalExpression(AbstractExpression):
    def __init__(self, str_array):
        self.set = set()
        for item in str_array:
            self.set.add(item)

    def interpret(self, info):
        if info in self.set:
            return True
        return False


def Split(info):
    split = info.split('-')
    if len(split) > 3:
        split = [split[0], split[1], '-'.join(split[2:])]
    return split


class NonTerminalExpression(AbstractExpression):
    def __init__(self, address, name, id):
        self.address = address
        self.name = name
        self.id = id

    def interpret(self, info):
        split = Split(info)
        if len(split) == 1:
            return self.address.interpret(split[0])
        if len(split) == 2:
            return self.address.interpret(split[0]) and self.name.interpret(split[1])
        if len(split[2]) > 3:
            return self.address.interpret(split[0]) and self.name.interpret(split[1]) and self.interpret(split[2])
        return self.address.interpret(split[0]) and self.name.interpret(split[1]) and self.id.interpret(split[2])