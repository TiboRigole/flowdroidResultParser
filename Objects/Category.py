class Category:

    # attributes:
    # -> main_tag = hoofdcategorie

    def __init__(self, line):

        lineSplitted = line[12:-1].split(" - ")

        self.main_tag = lineSplitted[0]

        if (len(lineSplitted) == 2):
            self.sub_tag = lineSplitted[1]
        else:
            self.sub_tag = None



    def __str__(self):
        if (self.sub_tag is None):
            return self.main_tag
        else:
            return self.main_tag + " - " + self.sub_tag