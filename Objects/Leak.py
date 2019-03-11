from Objects.Sink import Sink
import xml.etree.ElementTree as ET

from Objects.Source import Source


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



class Leak:

    def __init__(self, sink, sources):
        print("")
        print("")

        sinkLine = sink.attrib["Statement"]

        self.sink = Sink(sinkLine)
        self.sources = []

        self.sinkCategory = None
        self.sourceCategories = []

        for source in sources.iter('Source'):

            sourceLine = source.attrib["Statement"]
            source = Source(sourceLine)
            self.sources.append(source)

        print("done")

    def calculateCategories(self, sinksDict, sourcesDict):

        # set sinkCategory : only one
        self.sinkCategory = calculateSinkCat(self.sink, sinksDict)

        # set sourceCategoies : list of sources
        # work with indices
        print("start")
        for i in range(len(self.sources)):
            category = calculateSourceCat(self.sources[i], sourcesDict)
            self.sourceCategories.append(category)
        print("hey")