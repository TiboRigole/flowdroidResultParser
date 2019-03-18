from Objects.Sink import Sink
import xml.etree.ElementTree as ET

from Objects.Source import Source

class Leak:

    def __init__(self, sink, sources):

        sinkLine = sink.attrib["Statement"]

        self.sink = Sink(sinkLine)
        self.sources = []

        self.sinkCategory = None
        self.sourceCategories = []

        for source in sources.iter('Source'):

            sourceLine = source.attrib["Statement"]
            source = Source(sourceLine)
            self.sources.append(source)


    def calculateCategories(self, sinksDict, sourcesDict):

        # set sinkCategory : only one
        self.sinkCategory = calculateSinkCat(self.sink, sinksDict)

        # set sourceCategoies : list of sources
        # work with indices
        for i in range(len(self.sources)):
            category = calculateSourceCat(self.sources[i], sourcesDict)
            self.sourceCategories.append(category)

    def getSink(self):
        return self.sink

    def getSinkCat(self):
        return self.sinkCategory

    def getSourcesCatDict(self):

        returnDict = dict()

        for index, item in enumerate(self.sources):
            returnDict[item] = self.sourceCategories[index]

        return returnDict

    def getSources(self):
        return self.sources

#_______________________________________________________________________
#_______________________________________________________________________

def calculateSinkCat(sink, sinksDict):

    for key in sinksDict:
        if(sink.equals(key)):
            #return its category
            return sinksDict[key]

    print("probleem in Leak::calculateSinkCat : sink not found in dict")
    return None


def calculateSourceCat(source, sourcesDict):

    for key in sourcesDict:
        if(source.equals(key)):
            return sourcesDict[key]

    print("probleem in Leak::calcultaeSourceCat : source not found in dict")
    return None
