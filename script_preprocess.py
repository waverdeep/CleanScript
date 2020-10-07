from fileOI import filename_script_pair_tolist
import script_manipulate


def merge_script_like_libris(file_list, divider=' ', encoding='euc-kr'):
    # step 01 : 파일리스트를 통해서 스크립트 읽기
    for file in file_list:
        temp = filename_script_pair_tolist(file, encoding)
        # step 02 : 잡음 제거하기
        temp[1] = script_manipulate.remove_noise_id(temp[1], 'b/', 'i/', 'o/', 'n/')
        # step 03 : 구두점 제거하기
        temp[1] = script_manipulate.remove_punctuation_rules(temp[1], '.', ',', '?', '!')
        print(temp)