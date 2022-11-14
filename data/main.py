import csv

with open ("poi.csv", "a") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)


class point_of_interest():
    def __init__(self):
        self.MAX = 10
        self.arr = [None for x in range(self.MAX)]

    def get_poi(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    