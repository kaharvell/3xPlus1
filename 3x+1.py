import os
import numpy
from numpy.core.numerictypes import maximum_sctype

# Write iterator and max to starting_num file
def write_to_file(file, i, m):
    with open(file, 'w') as f:
        f.write(f'{i}\n')
        f.write(m)

# If file does not exist, create and write arguments to file
def file_exists(file, s, m=''):
    if not os.path.exists(file):
        with open(file, 'x') as f:
            f.write(f'{s}\n')
            if len(m) != 0:
                f.write(m)

def main():

    i = 0
    max_count = 0

    db = 'db.txt'
    starting_num = 'starting_num.txt'
    header = 'num, count, positive polarity count, negative polarity count, summation, average, variance, standard deviation'

    # Check if files exist
    file_exists(db, header)
    file_exists(starting_num, str(i), str(max_count))

    # Save iterator and highest_length from starting_num.txt to i and max_count
    with open(starting_num, 'r') as f:
        entries = f.readlines()
        i = int(entries[0]) + 1
        max_count = int(entries[1])

    while i > -1:
        occurrence = []
        num = i
        pos_polarity_count = 0
        neg_polarity_count = 0

        while num not in occurrence:
            occurrence.append(num)

            # if num is even divide by two
            if num % 2 == 0:
                num = num>>1

                pos_polarity_count += 1

            # else multiply by three add one
            else:
                num = (num<<1) + num + 1

                neg_polarity_count += 1

        count = len(occurrence)

        # if sequence's length is greater than max, write variables to file
        if count > max_count:
            max_count = count
            summation = sum(occurrence)
            avg = summation/count
            variance = numpy.var(occurrence)
            deviation = numpy.std(occurrence)
            s = f'{i}, {count}, {pos_polarity_count}, {neg_polarity_count}, {summation}, {avg}, {variance}, {deviation}\n'

            with open(db, 'a') as f:
                f.write(s)

            write_to_file(starting_num, str(i), str(max_count))

        # else write iterator and max_count to file to be assigned to iterator when program resumes
        else:
            write_to_file(starting_num, str(i), str(max_count))

        i += 1

        print(i)

if __name__== "__main__":
   main()