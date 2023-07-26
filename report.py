import pandas as pd


class Processeor():
    def __init__(self, jPath="listData.json", rPath="report.txt") -> None:
        self.content = pd.read_json(jPath)
        self.report = open(rPath, 'w')

    def write_report(self, key='', wav=0, txt=0):
        self.report.write('===============================' + '\n')
        self.report.write(key + '\n')
        self.report.write(' ---> ' + str(wav) + ' wav file (s)' + '\n')
        self.report.write(' ---> ' + str(txt) + ' text file (s)' + '\n')

    def get_content(self, key=""):
        # wavF = self.content.loc[self.content.key == key, 'nWavFile'].item()
        wavF = self.content[key]['nWavFile']
        # txtF = self.content.loc[self.content.key == key, 'nTxtFile'].item()
        txtF = self.content[key]['nTxtFile']
        self.write_report(key, wavF, txtF)

    def process_json(self):
        for key, value in proc.content.items():
            self.get_content(key)


if __name__ == "__main__":
    proc = Processeor("bai2/listData.json", 'bai2/report.txt')
    proc.process_json()
