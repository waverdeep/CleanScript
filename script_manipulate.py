import re


# 이중으로 들어간 공백을 수정해주는 함수
def remove_double_blank(line):
    temp = ' '.join(line.split())
    return temp


def get_only_script(lines, split_keyword='::'):
    path_lines = []
    script_lines = []
    for line in lines:
        temp = line.split(split_keyword)
        path_lines.append(temp[0])
        script_lines.append(temp[1].strip()) # 앞뒤 공백 제거

    return path_lines, script_lines


# 특정 감탄사만 제거하는 함수
def remove_interjection(line, keyword='아/ '):
    temp = line.replace(keyword, '')
    temp = remove_double_blank(temp)
    return temp


# 여러개의 감탄사를 제거하는 함수
def remove_interjections_in_list(lines, *args):
    dataset = []
    for line in lines:
        temp = line
        for arg in args:
            temp = temp.replace(arg, '')
        temp = remove_double_blank(temp)
        dataset.append(temp)
    return dataset


# 여러 형태의 잡음에 대한 스크립트 아이디를 제거하는 함수
def remove_noise_id_in_list(lines, *args):
    dataset = []
    for line in lines:
        temp = line
        for arg in args:
            temp = temp.replace(arg, '')
        temp = remove_double_blank(temp)
        dataset.append(temp)
    return dataset


# 숫자의 경우는 발음전사로 처리애햐 하기 때문에 해당 부분을 수정하는 함수
# 정규식으로 처리하는 것이 좋을지에 대한 부분은 생각을 해보아야 할 듯 함
def change_number_to_pron_in_list(lines):
    dataset = []
    for line in lines:
        if detect_numeric(line):
            modified_temp = numeric_to_pron(line)
            dataset.append(modified_temp)
        else:
            dataset.append(line)
    return dataset


# 숫자일 경우 발음전사를 선택하는 부분
def numeric_to_pron(line):
    temp = line
    pattern = re.compile(r"\((.*?)\)")
    find = re.findall(pattern, line)
    for s in range(0, len(find), 2):
        temp = temp.replace(find[s], '')
    temp = remove_bracket_pair(temp)
    temp = remove_slash(temp)
    temp = remove_double_blank(temp)
    return temp


def remove_slash(line):
    temp = line.replace('/', '')
    return temp


# 소괄호를 제거하는 함수
# 괄호 형태를 조절할 수 있음
def remove_bracket_pair(line, type_size='small'):
    if type_size == 'small':
        temp = re.sub('[()]', '', line)
    elif type_size == 'middle':
        temp = re.sub('[{}]', '', line)
    elif type_size == 'large':
        temp = re.sub('[[]]', '', line)
    return temp


# 문장 내에서 숫자를 검출하는 함수
# 만약 문장 내에 숫자가 있다면 True
# 만약 문장 내에 숫자가 없다면 False
def detect_numeric(line):
    temp = re.findall('\d', line)
    if len(temp) is 0:
        return False
    else:
        return True


# 문장 내에서 이중전사로 처리된 부분을 철자전사로 변경하는 함
def change_pron_to_dic_in_list():
    pass

