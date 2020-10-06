import re


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
    temp = ' '.join(temp.split())
    return temp


# 여러개의 감탄사를 제거하는 함수
def remove_interjections_in_list(lines, *args):
    dataset = []
    for line in lines:
        temp = line
        for arg in args:
            temp = temp.replace(arg, '')
        temp = ' '.join(temp.split())
        dataset.append(temp)
    return dataset


# 여러 형태의 잡음에 대한 스크립트 아이디를 제거하는 함수
def remove_noise_id_in_list(lines, *args):
    dataset = []
    for line in lines:
        temp = line
        for arg in args:
            temp = temp.replace(arg, '')
        temp = ' '.join(temp.split())
        dataset.append(temp)
    return dataset


# 숫자의 경우는 발음전사로 처리애햐 하기 때문에 해당 부분을 수정하는 함수
# 정규식으로 처리하는 것이 좋을지에 대한 부분은 생각을 해보아야 할 듯 함
def change_number_pron_in_list(lines):
    for line in lines:
        detect_numeric(line)


# 문장 내에서 숫자를 검출하는 함수
# 만약 문장 내에 숫자가 있다면 True
# 만약 문장 내에 숫자가 없다면 False
def detect_numeric(line):
    temp = re.findall('\d', line)
    print(temp)
    if len(temp) is 0:
        return False
    else:
        return True


# 문장 내에서 이중전사로 처리된 부분을 철자전사로 변경하는 함
def change_pron_to_dic_in_list():
    pass

