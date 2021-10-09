import os
import numpy

def main():

    i = 0
    max_length = 0

    file = 'db.txt'

    # check if db.txt exists
    if os.path.exists(file):
        # save last iteration and length calculated to i and max_length for a starting point
        with open(file, 'r') as f:
            db = f.readlines()
            db = db[-1].split(', ')
            i = int(db[0]) + 1
            max_length = int(db[1])
    else:
        # create file to write observations to
        with open(file, 'w') as f:
            f.write('iteration, length, pos_polarity_count, neg_polarity_count, summation, avg, variance, deviation\n')

    while i > -1:
        x = i
        occurrence = []

        # if x in occurrence, exit endless loop
        while x not in occurrence:
            occurrence.append(x)

            pos_polarity_count = 0
            neg_polarity_count = 0

            # if x is zero, binary calculations below won't work properly, so 3*0+1 = 1
            if x == 0:
                x = 1

            # if num is even divide by two
            if x % 2 == 0:
                x = x>>1

                pos_polarity_count += 1

            # else multiply by three add one
            else:
                x = (x<<1) + x + 1

                neg_polarity_count += 1

        length = len(occurrence)

        # if sequence's length is greater than max_length, write variables to file
        if length >= max_length:
            max_length = length
            summation = sum(occurrence)
            avg = summation/length
            variance = numpy.var(occurrence)
            deviation = numpy.std(occurrence)
            values = f'{i}, {max_length}, {pos_polarity_count}, {neg_polarity_count}, {summation}, {avg}, {variance}, {deviation}'

            with open(file, 'a') as f:
                f.write(f'{values}\n')

        print(i)

        i += 1

if __name__== "__main__":
   main()