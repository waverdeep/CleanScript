import fileOI
import script_preprocess
import sys
import create_label

# dev_dataset = './dataset/dev.trn'
# data_list = fileOI.read_txt_file(dev_dataset)
#
# print(data_list[0])
#
# _, script_lines = script_manipulate.get_only_script(data_list)
# for i in range(20, 40):
#     print('{} :: {}'.format(i, script_lines[i]))
#
# # 스르립트에 포함된 감탄사 관련 내용 제거 ( 감탄사 관련 부분도 충분히 인식할 수 있을 정도로 판단하여 수정이 필요)
# # reformat_script_lines = script_manipulate.remove_interjections_in_list(script_lines, '아/', '그/', '어/')
# # for i in range(20, 40):
# #     print('{} :: {}'.format(i, reformat_script_lines[i]))
#
# # 스크립트에 포함된 잡음 아이디 코드 제거
# reformat_script_lines = script_manipulate.remove_noise_id_in_list(script_lines, 'b/', 'i/', 'o/', 'n/')
#
# # remove numeric type
# reformat_script_lines = script_manipulate.change_number_to_pron_in_list(reformat_script_lines)




input_dir = './dataset/Kspon_dataset/KsponSpeech_01'
input_dir = '/data/Kspon_dataset/wav'
dataset = fileOI.get_divided_script(input_dir=input_dir)
print(len(dataset))
# dataset_merge = script_preprocess.merge_script_like_libris(dataset)
# fileOI.write_csv_file(dataset_merge, './dataset', 'filelist.csv')
# fileOI.read_csv_file('./dataset', 'filelist.csv')
# label_list = create_label.extract_singular_labels(dataset)
# fileOI.write_label('.', 'labels.txt', label_list)
# print(label_list)
json_list = script_preprocess.merge_script_like_clova_call(dataset, encoding='utf8')
fileOI.write_json_file(json_list, './output_jso_20201020_1.json')
output_filepath = './output_jso_20201020_1.json'
train_list, test_list = script_preprocess.split_train_test_dataset_with_json(json_list, split_rate=0.2, encoding='utf8')
# fileOI.write_json_file(train_list, './output_train.json')
# fileOI.write_json_file(test_list, './output_test.json')



script_preprocess.create_small_json(train_list)