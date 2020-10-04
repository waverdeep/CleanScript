import os
import glob


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def open_file(file_path):
    f = open(file_path)
    return f


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
