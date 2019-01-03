#-*-coding:UTF-8-*-


import os
import os
import json


def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

if __name__ == '__main__':
    ss = scan_files("./TESTreport/",postfix=".html")
    #aa = json.loads(ss)
    aa = "".join(ss)
    json.dumps(aa)
   # cc = json.loads(aa)
    print(ss)
    print(type(aa))
  #  print(cc)
