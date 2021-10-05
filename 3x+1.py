import os
import numpy

def main():

    max = 0
    file = 'db.txt'
    i = 0

    # assign 'starting num' in file to iterator
    if os.path.exists(file):
        with open(file) as f:
            entries = f.readlines()
            i = int(entries[-1][14:]) + 1
            print(i)
    # create file if file does not exist
    else:
        with open(file, 'x') as f:
            f.writelines('num, count, positive polarity count, negative polarity count, summation, average, variance, standard deviation\n')
            f.writelines(f'starting num: {i}')

    while i < 1000000001:
        occurrence = []
        num = i
        pos_polarity_count = 0
        neg_polarity_count = 0

        while num not in occurrence:
            occurrence.append(num)

            # if num is even divide by two
            if num % 2 == 0:
                pos_polarity_count += 1
                num = num>>1
            # else multiply by three add one
            else:
                neg_polarity_count += 1
                num = (num<<1) + num + 1

        count = len(occurrence)
        replace = f'starting num: {i + 1}'

        # store file contents to a list to rewrite file using write_to_file()
        with open(file, 'r') as f:
                db = f.readlines()

        # if sequence length is greater than max, write variables to file
        if count > max:
            max = count
            summation = sum(occurrence)
            avg = summation/count
            variance = numpy.var(occurrence)
            deviation = numpy.std(occurrence)
            s = f'{i}, {count}, {pos_polarity_count}, {neg_polarity_count}, {summation}, {avg}, {variance}, {deviation}\n'

            write_to_file(file, db, replace, s)

        # else write last num calculated to file to be assigned to iterator when program resumes
        else:
            write_to_file(file, db, replace)

        i += 1

        print(i)

def write_to_file(file, content, replace, s = ''):
    with open(file, 'w') as f:
                for item in content[:-1]:
                    f.write(item)
                if len(s) != 0:
                    f.writelines(s)
                f.write(replace)

if __name__== "__main__":
   main()