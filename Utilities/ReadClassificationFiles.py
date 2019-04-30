from Objects.Category import Category
from Objects.Sink import Sink
from Objects.Source import Source


def setupFromTxt(path_to_file, type):

    # key = source or sink
    # value = category
    ss_dict = dict()

    # read lines of the txt file
    with open(path_to_file) as fp:
        lines = fp.readlines()

    # allocation of variables
    current_category = " "
    current_ss = " "


    # iterate over every line
    for line in lines:

        # if line is category
        if(line.startswith('@')):
            current_category = Category(line)

        # if line is source or sink
        elif(line.startswith('<')):

            # format the line
            if( type == 'SINKS'):
                current_ss = Sink(line)

            elif( type == 'SOURCES'):
                current_ss = Source(line)

            # add to the dicionary
            ss_dict[current_ss] = current_category

    return  ss_dict