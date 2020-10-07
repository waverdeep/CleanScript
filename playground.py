import fileOI
import script_manipulate

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
dataset = fileOI.get_divided_script(input_dir=input_dir)
print(dataset)