import requests
import os
import sys
import numpy


class Triangle(object):

    def __init__(self, link):
        self.link = link
        self.main_arr = []
        self.exit_way = []


    def tria_search(self):
        tree = requests.get(self.link)
        arr = tree.text.split("\n")
        if arr[-1] == "":
            arr = arr[:-1]
        
        for ar in arr:
            self.main_arr.append(ar.split(" "))
        '''
        for i in range(len(main_arr)):
           print(main_arr[i])
           _=input("Break ...") 
        '''

        for i in range(len(self.main_arr)):
            line_list = []
            for j in range(len(self.main_arr[i])):
                if i - 1 < 0:
                    first_dickt = {"sum": int(
                        self.main_arr[i][j]), "path": [j]}
                    line_list.append(first_dickt)

                else:
                    elem_dict = {}
                    r_sum = None
                    r_ind = None
                    for k in range(len(self.main_arr[i - 1])):
                        if abs(j - k) <= 1:
                            if r_sum is None and r_ind is None:
                                r_sum = int(
                                    self.exit_way[i - 1][k]["sum"]) + int(self.main_arr[i][j])
                                r_ind = k

                            if r_sum is not None and r_ind is not None:
                                if int(self.exit_way[i - 1][k]["sum"]) + int(self.main_arr[i][j]) > r_sum:
                                    r_sum = int(
                                        self.exit_way[i - 1][k]["sum"]) + int(self.main_arr[i][j])
                                    r_ind = k

                    r_path = self.exit_way[i - 1][r_ind]["path"].copy()
                    r_path.append(j)
                    next_dict = {"sum": r_sum, "path": r_path}
                    line_list.append(next_dict)

            self.exit_way.append(line_list)

        final_sum = None
        final_ind = None
        for i in range(len(self.exit_way[-1])):
            if final_sum is None:
                final_sum = int(self.exit_way[-1][i]["sum"])
                final_ind = i

            if final_sum is not None:
                if final_sum < int(self.exit_way[-1][i]["sum"]):
                    final_sum = int(self.exit_way[-1][i]["sum"])
                    final_ind = i

        return self.exit_way[-1][final_ind]["path"]


print("Number of element is the level in piramid")

tria = Triangle("https://dl.dropboxusercontent.com/u/28873424/tasks/triangle.txt")
way = tria.tria_search()


for i in range(len(way)):
    print(i, way[i])



print("\r\n\r\n")
tria = Triangle("https://dl.dropboxusercontent.com/u/28873424/tasks/simple_triangle.txt")
way = tria.tria_search()

for i in range(len(way)):
    print(i, way[i])


