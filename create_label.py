# create label in script
import script_preprocess
import script_manipulate
import fileOI


def extract_singular_labels(filelist, divider=' ', encoding='euc-kr'):
    phn_list = []
    for file in filelist:
        temp = fileOI.filename_script_pair_tolist(file, encoding)
        if script_manipulate.is_remove_line(temp[1]):
            break
        temp[1] = script_preprocess.remove_options(temp[1])

        for word in temp[1]:
            if word not in phn_list:
                phn_list.append(word)
    return phn_list



