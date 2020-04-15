import time
list_file = []

with open("file", "r+") as f:
    for line in f:
        list_file.append(line)
    count = len(list_file)
    while True:
        count += 1
        f.write(str(count) + ". " + time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))
        f.flush()
        time.sleep(2)

