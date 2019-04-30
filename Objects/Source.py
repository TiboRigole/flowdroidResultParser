class Source:
    def __init__(self, line):

        index_a = line.find('<')
        index_b = line.find('>')

        relevant_piece = line[index_a+1 : index_b]

        pieces = relevant_piece.split(" ")

        self.class_type = pieces[0][:-1]
        self.return_type = pieces[1]
        self.method_name = pieces[2]

    def __str__(self):
        return (self.class_type + " " + self.return_type + " " + self.method_name)

    def equals(self, sourceFromDict):

        if(self.method_name == sourceFromDict.methodName and self.return_type == sourceFromDict.returnType):
            return True
            # todo probleem : mag k hier laten van te vergelijken op classType ?
        else:
            return False