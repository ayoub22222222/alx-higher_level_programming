#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    i = 0
    lenght = len(sys.argv)
    for i in range (0, lenght):
        if i != 0:
            sum +=  int(sys.argv[i])
    print("{}".format(sum))
