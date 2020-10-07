import os
import glob
import natsort


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def open_file(file_path):
    f = open(file_path)
    return f

def get_pure_filepath(filename):
    temp = filename.split('/')
    del temp[-1]
    temp = '/'.join(temp)
    return temp


def get_pure_filename(filename):
    temp = filename.split('.')
    del temp[-1]
    temp = ' '.join(temp)
    temp = temp.split('/')
    temp = temp[-1]
    return temp


def read_txt_file(file_path, encoding='utf8'):
    lines = []
    f = open(file_path, 'r', encoding=encoding)
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)
    f.close()
    return lines


def read_text_file_one_line(file_path, encoding='utf8'):
    f = open(file_path, 'r', encoding=encoding)
    line = f.readline()
    f.close()
    return line


# by kspon
def get_divided_script(input_dir, file_extension='txt'):
    temp = get_all_file_path(input_dir, file_extension)
    temp = natsort.natsorted(temp)
    return temp


def filename_script_pair_tolist(filename, encoding):
    line = read_text_file_one_line(filename, encoding)
    pure_filename = get_pure_filename(filename)
    temp = [pure_filename, line]
    return temp


def merge_script_like_libris(file_list, divider=' ', encoding='euc-kr'):
    # step 01 : 파일리스트를 통해서 스크립트 읽기
    for file in file_list:
        temp = filename_script_pair_tolist(file, encoding)
        print(temp)