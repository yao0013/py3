import csv
class ReadCsv():
    def read_csv(self):
        item = []
        r = csv.reader(open("D:\\listtest\\风变\\test_case.csv","r"))
        for i in r:
            item.append(i)
        return item[5:6]
re = ReadCsv()
q = re.read_csv()
