
from Objects.Category import Category
from Objects.Sink import Sink
from Objects.Source import Source

def setupFromTxt(path_to_file, ssType):

    currentCategory = " "
    currentSS = "" # current source or sink, dependant form ssType

    # mapping : source -> categorie
    ssDict = dict()



    with open(path_to_file) as fp:

        line = fp.readline()
        cnt = 1

        # iterate over overy line
        while line:
            # hier elk van de 3 gevallen

            if(not line.startswith("%")):
                # dan is het geen commentaar

                if(line.startswith("@")):
                    # nieuwe categorie
                    currentCategory = Category(line)

                elif(line.startswith("<")):
                    # nieuwe source of sink gevonden
                    if(ssType == "SINKS"):
                        currentSS = Sink(line)

                    elif(ssType == "SOURCES"):
                        currentSS = Source(line)

                    # add to dictionary
                    ssDict[currentSS] = currentCategory


            # read next line
            line = fp.readline()
            cnt += 1

    return ssDict