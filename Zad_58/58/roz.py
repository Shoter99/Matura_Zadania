import os


def main():
    file1 = readFromFile("dane_systemy1.txt", 2)
    file2 = readFromFile('dane_systemy2.txt', 4)
    file3 = readFromFile('dane_systemy3.txt', 8)
    print(find_lowest(file1))
    print(find_lowest(file2))
    print(find_lowest(file3))


def readFromFile(filename, sys):
    with open(filename, 'r') as f:
        output = []
        for line in f:
            l = line.strip().split(' ')
            output.append({
                'time': int(l[0], sys),
                'temp': int(l[1], sys)
            })

        return output


def find_lowest(list):
    r1 = 100
    for record in list:
        if record['temp'] < r1:
            r1 = record['temp']
    return format(r1, 'b')


if "__main__" == __name__:
    main()
