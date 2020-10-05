import fileOI
import script_manipulate

dev_dataset = './dataset/dev.trn'
data_list = fileOI.read_txt_file(dev_dataset)

print(data_list[0])

_, script_lines = script_manipulate.get_only_script(data_list)
print(script_lines[10])


print(script_manipulate.remove_interjection(script_lines[0]))

reformat_script_lines = script_manipulate.remove_interjections_in_list(script_lines, '아/', '그/', '어/')
print(reformat_script_lines[10])
