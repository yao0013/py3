import csv
class ReadCsv():
    def read_csv(self):
        item = []
        r = csv.reader(open("D:\\listtest\\风变\\test_case.csv","r"))
        for i in r:
            item.append(i)
        return item[1:]
