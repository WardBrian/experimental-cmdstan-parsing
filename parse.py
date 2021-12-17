def parse_subtree(filehandle, data, spaces=2):
    pos = filehandle.tell()
    line = filehandle.readline()
    while line.startswith("#"):
        n = len(line)
        stripped = line.lstrip("# ")
        n_spaces = n - len(stripped)
        if n_spaces < spaces:
            # dedent means we need backtrack
            filehandle.seek(pos)
            return
        # default = '(Default)' in line
        result = stripped.replace(" (Default)", "").split("=")
        if len(result) == 1:
            # no =, this begins a sub-block
            key = stripped.strip()
            # sometimes the sub block really began above, such as:
            # algorithm = hmc
            #   hmc
            last_key, item = data.popitem()
            if item == key:
                data[last_key] = {key: {}}
                parse_subtree(filehandle, data[last_key][key], spaces + 4)
            else:
                # if that wasn't the case, like with adapt, just proceed
                data[last_key] = item
                data[key] = {}
                parse_subtree(filehandle, data[key], spaces + 2)
        else:
            data[result[0].strip()] = result[1].strip()
        pos = filehandle.tell()
        line = filehandle.readline()

    filehandle.seek(pos)


def parse_csv(file):
    with open(file, "r") as f:
        header_data = {"filename": file}
        parse_subtree(f, header_data, 2)
    return header_data
