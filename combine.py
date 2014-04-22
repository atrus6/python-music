import sys

def main():
    f = open(sys.argv[1],'r')
    out = open(sys.argv[2], 'a')
    size = int(sys.argv[3])

    previous = ''
    count = 0

    for line in f:
        lineparts = line.split()

        gram = lineparts[:size]
        count = count + int(lineparts[len(lineparts)-1])

        if gram != previous:
            out.write(' '.join(previous) + ' ' + str(count) + '\n')
            previous = gram
            count = 0;

if __name__ == '__main__':
    main()

