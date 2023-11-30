#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n == 1:
	print("0 arguments.")
    elif n > 1:
        print(f"{n} arguments:")
	for i in range(1, n + 1):
                print({i}: {sys.argv[i]})
