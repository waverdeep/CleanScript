def get_only_script(lines, split_keyword='::'):
    path_lines = []
    script_lines = []
    for line in lines:
        temp = line.split(split_keyword)
        path_lines.append(temp[0])
        script_lines.append(temp[1].strip()) # 앞뒤 공백 제거

    return path_lines, script_lines


def remove_interjection(line, keyword='아/ '):
    temp = line.replace(keyword, '')
    temp = ' '.join(temp.split())
    return temp


def remove_interjections_in_list(lines, *args):
    datasets = []
    for line in lines:
        temp = line
        for arg in args:
            temp = temp.replace(arg, '')
        temp = ' '.join(temp.split())
        datasets.append(temp)
    return datasets

