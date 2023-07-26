import os
import regex as re
import json
import copy


class Processer():
    def __init__(self, file="") -> None:
        self.file = file
        self.content = []
        self.date_re = "\\d{4}-\\d{2}-\\d{2}"
        self.student_re = re.compile("^[Bb]{1}\d{2}[a-zA-Z]{4}\d{3}$")
        self.stu_code = []
        self.data_dict = []
        self.file_type = {
            'txt': 'nTxtFile',
            'wav': 'nWavFile'
        }

    def get_content(self):
        self.content = open(self.file, 'r').readlines()
        # print(self.content[15:20])

    def process_student(self, data=[]):
        # skip if path is folder
        if not data[-1][-3:] in ['txt', 'wav']:
            return

        # init student dict if not present
        if data[0] not in self.stu_code and self.student_re.match(data[0]):
            self.stu_code.append(data[0])
            self.data_dict.append({
                'nWavFile': 0,
                'nTxtFile': 0
            })

        # change student info according to data
        if self.student_re.match(data[0]):
            try:
                self.data_dict[self.stu_code.index(
                    data[0])][self.file_type[data[-1][-3:]]] += 1
            except:
                pass

        # create dir if not exists
        _root = data[0]
        _dir = data[-1]
        if not os.path.exists(_root):
            os.makedirs(_root)
        if data[-1][-3:] == 'txt':
            f = open(_root + '/' + _dir, 'w')
            f.write(str(self.data_dict[self.stu_code.index(
                data[0])][self.file_type[data[-1][-3:]]]))
            f.close()

    def process_raw(self):
        for in_str in self.content[15:]:
            in_str = in_str.replace('\t', ' ')
            # process string
            temp = ''
            cnt = 0
            for i in range(len(in_str) - 1):
                if in_str[i] == ' ' and in_str[i + 1] != ' ':
                    pass
                elif in_str[i] == ' ' and cnt == 0:
                    temp += ' '
                    cnt = 1
                elif in_str[i] == ' ' and cnt != 0:
                    pass
                elif in_str[i] != ' ':
                    temp += in_str[i]
                    cnt = 0
            in_str = temp
            splt_str = in_str.split(' ')
            try:
                # this is a list
                proc_str = splt_str[-1].replace(' ', '').split('\\')
                # print(proc_str)
                # break
            except:
                # catching empty string
                pass
            self.process_student(proc_str)
        pass

    def print_processed(self):
        print(list(self.stu_code))
        print(list(self.data_dict))

    def dump_json(self, path=""):
        export = {}
        for code in self.stu_code:
            export[code] = self.data_dict[self.stu_code.index(code)]
        jStr = json.dumps(export)
        if path != "":
            jFile = open(path, 'w')
        else:
            jFile = open('listData.json', 'w')
        jFile.write(jStr)
        jFile.close()


if __name__ == "__main__":
    proc = Processer("bai2\G18LogAllDownload202210142034ForProcess.txt")
    proc.get_content()
    proc.process_raw()
    # proc.print_processed()
    proc.dump_json('bai2/listData.json')
