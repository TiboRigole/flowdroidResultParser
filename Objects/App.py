import xml.etree.ElementTree as ET

from Objects.Leak import Leak


class App:

    # attributes
    #
    # name = name of the app
    #
    #
    #

    def __init__(self, filename, path_to_file):

        self.name = filename
        self.leaks = []
        self.num_of_leaks = 0
        self.source_count = 0
        self.sink_count = 0

        # aantal gevonden, niet aantal dat leidt tot leaks
        self.num_of_discovered_sources = 0
        self.num_of_discovered_sinks = 0

        try:
            root = ET.parse(path_to_file).getroot()

            for result in root.iter('Result'):

                self.num_of_leaks += 1

                leak = Leak(result)

                self.leaks.append(leak)

            # die extra values derin meepakken

        except ET.ParseError:
            print("fout bij inladen van de xml")
            self.num_of_leaks = -1

    def set_categories(self, sinks_dict, sources_dict):
