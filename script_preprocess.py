from fileOI import filename_script_pair_tolist
import script_manipulate


def merge_script_like_libris(file_list, divider=' ', encoding='euc-kr'):
    dataset = []
    # step 01 : 파일리스트를 통해서 스크립트 읽기
    for file in file_list:
        temp = filename_script_pair_tolist(file, encoding)
        # step 01 -01 : u/ 이 삽입된 문장은 삭제
        if script_manipulate.is_remove_line(temp[1]):
            break
        # step 02 : 잡음 제거하기
        temp[1] = script_manipulate.remove_noise_id(temp[1], 'b/', 'i/', 'o/', 'n/', 'l/')
        # step 03 : 구두점 제거하기
        temp[1] = script_manipulate.remove_punctuation_rules(temp[1], '.', ',', '?', '!', '+', '*')
        # step 04 : 이중전사 처리하기
        temp[1] = script_manipulate.change_number_to_pron(temp[1])
        # step 05 : 이중전사 처리하기 (철자전사, 발음전사)
        temp[1] = script_manipulate.change_pron_to_dic(temp[1])
        dataset.append(temp)
        print(temp)
    return dataset
