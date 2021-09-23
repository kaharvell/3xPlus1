import os
import numpy

def main():

    max = 0
    file = 'db.txt'
    i = 0

    if os.path.exists(file):
        with open(file) as f:
            entries = f.readlines()
            i = int(entries[-1][14:]) + 1
            print(i)
    else:
        with open(file, 'x') as f:
            f.writelines('num, count, positive polarity count, negative polarity count, summation, average, variance, standard deviation\n')
            f.writelines(f'starting num: {i}')

    while i > -1:
        occurrence = []
        num = i
        pos_polarity_count = 0
        neg_polarity_count = 0

        while num not in occurrence:
            occurrence.append(num)

            if num % 2 == 0:
                pos_polarity_count += 1
                num = num>>1
            else:
                neg_polarity_count += 1
                num = (num<<1) + num + 1

        count = len(occurrence)
        replace = f'starting num: {i + 1}'

        if count > max:
            max = count
            summation = sum(occurrence)
            avg = summation/count
            variance = numpy.var(occurrence)
            deviation = numpy.std(occurrence)

            with open(file, 'r') as f:
                db = f.readlines()
                with open(file, 'w') as f:
                    for item in db[:-1]:
                        f.write(item)
                    f.writelines(f'{i}, {count}, {pos_polarity_count}, {neg_polarity_count}, {summation}, {avg}, {variance}, {deviation}\n')
                    f.write(replace)
        else:
            with open(file, 'r') as f:
                db = f.readlines()
                with open(file, 'w') as f:
                    for item in db[:-1]:
                        f.write(item)
                    f.write(replace)


        i += 1

        print(i)


if __name__== "__main__":
   main()