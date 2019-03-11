class Category:

    def __init__(self, line):

        lineSplitted = line[12:-1].split(" - ")

        self.mainTag = lineSplitted[0]

        if(len(lineSplitted) == 2):
            self.subTag = lineSplitted[1]
        else:
            self.subTag = None

    def __str__(self):
        if( self.subTag is None):
            return self.mainTag
        else:
            return self.mainTag +" - " + self.subTag