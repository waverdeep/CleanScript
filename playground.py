import fileOI


dev_dataset = './dataset/dev.trn'
data_list = fileOI.read_txt_file(dev_dataset)

print(data_list[0])
