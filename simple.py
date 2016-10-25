from math import sqrt
import re
import time


class SimpleNumb(object):
    """
    Some about this class
    """

    def __init__(self, n):
        self.n = n

    def s_num(self):
        """
        Search all simple numbers to the number 
        you input in class identification
        """
        lst = [2]
        for i in range(3, self.n + 1, 2):
            if (i > 10) and (i % 10 == 5):
                continue

            for j in lst:
                if j * j - 1 > i:
                    lst.append(i)
                    break
                if (i % j == 0):
                    break
            else:
                lst.append(i)
        return lst

    def circle(self, s):
        """
        Construct circle simple numbers
        to the s number 
        """
        if len(s) == 1:
            return [s]

        if len(s) > 1:
            arr_s = []
            new_s = s + s
            for s_i in range(len(s)):
                arr_s.append(new_s[s_i:s_i + len(s)])

            for i in range(len(arr_s)):
                pattern = re.match("(0+)?(\d+)", arr_s[i])
                arr_s[i] = pattern.group(2)

            return arr_s

    def ci_num(self, lst):
        """
        check is the simple numbers is the
        circle simple and return list of it
        """
        ci_arr = []
        i = 0
        while True:
            if i == len(lst):
                break

            w_num = False
            for n in ["0", "2", "4", "5", "6", "8"]:
                if n in str(lst[i]) and 1 < len(str(lst[i])):
                    w_num = True
                    i += 1
                    break
            if w_num:
                continue

            lst_cir = self.circle(str(lst[i]))
            is_all = False
            for c_el in lst_cir:
                if int(c_el) in lst:
                    is_all = True

                if int(c_el) not in lst:
                    is_all = False
                    i += 1
                    break

            if is_all:
                for c in set(lst_cir):
                    ci_arr.append(c)

                for c_el in set(lst_cir):
                    if int(c_el) not in lst:
                        _ = input("\r\nWTF error ?!")

                    if int(c_el) in lst:
                        lst.remove(int(c_el))

        return ci_arr

start_time = time.time()

simple = SimpleNumb(1000000)
list_numb = simple.s_num()
ci_numb = simple.ci_num(list_numb)


print("Elapsed time: {:.3f} sec".format(time.time() - start_time))

for n in ci_numb:
    print(n)
