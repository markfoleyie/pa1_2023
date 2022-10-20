FILENAME = "hnr1.abc"

try:
    with open(FILENAME, "r") as fh:
        file_contents = fh.read()

    for line in file_contents:
        print(line, end="")
except Exception as e:
    print(f"{e}")
    quit()