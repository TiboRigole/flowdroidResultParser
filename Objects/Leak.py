import xml.etree.ElementTree as ET

from Objects.Sink import Sink
from Objects.Source import Source

class Leak:

    # attributes
    #
    # sink : Sink
    # sources: array < Source >
    #
    # sink_category : category of the sink
    # sources_categories : array < Categories > : categories of the sources
    #

    def __init__(self, result):

        # parsing of sink in result
        xml_sink = result.find('Sink')
        sink_line = xml_sink.attrib["Statement"]
        self.sink = Sink(sink_line)


        self.sources = []

        # parsing in sources in result
        xml_sources = result.find('Sources')
        for source in xml_sources.iter('Source'):

            source_line = source.attrib["Statement"]
            this_source = Source(source_line)
            self.sources.append(this_source)


        self.sink_category = None
        self.sources_categories = []

    def calculate_categories(self, sinks_dict, sources_dict):

        # sink categorie
        self.sink_category = calculate_sink_cat(self.sink, sinks_dict)

        # sources categories
        for source in self.sources:
            category = calculate_source_cat(source, sources_dict)
            self.sources_categories.append(category)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def calculate_sink_cat(sink, sinksDict):

    for key in sinksDict:
        if(sink.equals(key)):
            #return its category
            return sinksDict[key]

    print("probleem in Leak::calculateSinkCat : sink not found in dict")
    return None


def calculate_source_cat(source, sourcesDict):

    for key in sourcesDict:
        if(source.equals(key)):
            return sourcesDict[key]

    print("probleem in Leak::calcultaeSourceCat : source not found in dict")
    return None
