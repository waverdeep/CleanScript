def get_only_script(lines, split_keyword='::'):
    path_lines = []
    script_lines = []
    for line in lines:
        temp = line.split(split_keyword)
        path_lines.append(temp[0])
        script_lines.append(temp[1].strip()) # 앞뒤 공백 제거

    return path_lines, script_lines
