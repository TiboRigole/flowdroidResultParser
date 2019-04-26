import xml.etree.ElementTree as ET
from Objects.Leak import Leak

class App:

    def __init__(self, filename, path_to_file):
        self.name = filename
        self.leaks = []
        self.num_of_leaks = 0 # = aantal Results in de xml
        self.sourceCount = 0
        self.sinkCount = 0

        try:
            root = ET.parse(path_to_file).getroot()

            print(root.tag)
            for child in root:
                print(child.tag)


            for result in root.iter('Result'):

                sink = result.find('Sink')
                sources = result.find('Sources')

                # make leak with sink and sources
                leak = Leak(sink, sources)

                # add leak to leaklist from this app
                self.leaks.append(leak)

                self.num_of_leaks += 1

            print('test')
        except ET.ParseError:
            print("app had no entry points")
            self.num_of_leaks = -1



    def setCategories(self, sinksDict, sourcesDict):
        for leak in self.leaks:
            leak.calculateCategories(sinksDict, sourcesDict)
            # print("klaar met een leak")

    def getNumOfLeaks(self):
        return self.num_of_leaks

    def getLeaks(self):
        return self.leaks