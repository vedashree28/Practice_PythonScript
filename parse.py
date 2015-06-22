# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = "E:\DataWranglingUdacity"
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    temp = []
    keys = []
    count = 0
    with open(datafile, "r") as f:
        for line in f:
            if count == 0 :
                keys.append(line)
            elif count>0 and count<11 :
                temp.append(line)
            else:
                break
            count += 1
        item = {}
        keys = keys[0].replace('\n','').split(',')
        for i in range(0,10,1):
            value = temp[i].replace('\n','').split(",")
            for j in range(0,len(keys)):
                if j == 3 or j == 4:
                    if not value[j].isdigit():
                        value[j] = '-'
                item[keys[j]] = value[j]
            data.append(item)
            print item
            item = {}
        f.close()
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()