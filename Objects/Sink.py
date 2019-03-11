import re

class Sink:
    def __init__(self, line):

        index_a = line.find('<')
        index_b = line.find('>')

        relevant_piece = line[index_a+1 : index_b]

        pieces = relevant_piece.split(" ")

        self.classType = pieces[0][:-1]
        self.returnType = pieces[1]
        self.methodName = pieces[2]


    def __str__(self):
        return (self.classType +" "+ self.returnType +" " + self.methodName)

    def equals(self, sinkFromDict):

        if(self.methodName == sinkFromDict.methodName and self.returnType == sinkFromDict.returnType):
            return True
            # probleem : mag k hier laten van te vergelijken op classType ?
        else:
            return False