def version_increase(mms):
    try:
        filev = open("data//version.txt", "r+")
    except:
        try:
            filev = open("data//version.txt", "w+")
        except:
            print("\n(version_handler): Unable to find data directory. Version not set or increased\n")
            return
    line = filev.readline()
    filev.seek(0)
    filev.truncate()
    if len(line) < 1:
        line = "0.0.0"
    line_list = line.split(".")
    print(line)
    if mms == 0:
        line_list[2] = int(line_list[2])
        line_list[2] += 1
        line_list[2] = str(line_list[2])
    if mms == 1:
        line_list[1] = int(line_list[1])
        line_list[1] += 1
        line_list[1] = str(line_list[1])
        line_list[2] = "0"
    if mms == 2:
        line_list[0] = int(line_list[0])
        line_list[0] += 1
        line_list[0] = str(line_list[0])
        line_list[1] = "0"
        line_list[2] = "0"
    line = '.'.join(line_list)
    filev.write(line)
    filev.close()

def version_read():
    try:
        filev = open("data//version.txt", "r")
    except:
        try:
            filev = open("data//version.txt", "r+")
        except:
            print("\n(version_handler): Unable to find data directory. Version unkown.\n")
            return "0.0.0"
    line = filev.readline()
    if len(line) < 1:
        line = "0.0.0"
    filev.close()
    return line
