from fileOI import filename_script_pair_tolist
from script_manipulate import remove_noise_id


def merge_script_like_libris(file_list, divider=' ', encoding='euc-kr'):
    # step 01 : 파일리스트를 통해서 스크립트 읽기
    for file in file_list:
        temp = filename_script_pair_tolist(file, encoding)
        temp[1] = remove_noise_id(temp[1], 'b/', 'i/', 'o/', 'n/')
        print(temp)