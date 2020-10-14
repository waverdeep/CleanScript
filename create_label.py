# create label in script
import script_preprocess
import script_manipulate
import fileOI
from tqdm import tqdm


def extract_singular_labels(filelist, divider=' ', encoding='cp949'):
    phn_list = []
    for file in tqdm(filelist):
        temp = fileOI.filename_script_pair_tolist(file, encoding)
        if script_manipulate.is_remove_line(temp[1]):
            break
        original = temp[1]
        temp[1] = script_preprocess.remove_options(temp[1])

        for word in temp[1]:
            if word not in phn_list:
                phn_list.append(word)
            if word in ['Q','A','Z','W','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','M','I','K','O','L','P']:
                print(temp[0], temp[1], original)
    return phn_list



