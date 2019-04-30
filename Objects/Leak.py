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


