# import csv
import sys
import math

class CoffeeShop(object):

    def __init__(self):
        self.output = [(" ",float("inf")),(" ",float("inf")),(" ",float("inf"))]

    def get_three_closest_shops(self, y1,x1,fname):
        '''
        calculates the three nearest coffeeshop location for a user

        Args:  coordinates of user
               filename of the coffee shop list
        '''

        f = open(fname,'r')
        lines = f.readlines()
        if len(lines) < 3:
            print "INSUFFICIENT INPUT LIST"
            sys.exit(1)

        for line in lines:
            data = line.strip('\n').split(',')
            valid = self.check_validity(data)
            if not valid:
               print "MISSING DATA"
               sys.exit(1)

            dist = round(math.sqrt(math.pow((float(y1) - float(data[1])),2) + math.pow((float(x1)-float(data[2])),2)),4)
            if dist < self.output[0][1] :
                self.output[2] = self.output[1]
                self.output[1] = self.output[0]
                self.output[0] = (data[0],dist)

            elif ((self.output[0][1] <  dist)  and (dist < self.output[1][1])):
                self.output[2] = self.output[1]
                self.output[1] = (data[0],dist)

            elif (dist < self.output[2][1]):
                self.output[2] = (data[0],dist)

        return self.output[0],self.output[1],self.output[2]


    def check_validity(self,data):
        '''
        validates that the data columns are missing
        can be expanded to check validity of datatypes/attributes of each column value
        '''
        if (data[0] == None or data[1] == None  or data[2] == None):
            return 0
        else:
            return 1


if __name__ == '__main__':
    cmdargs = sys.argv
    if (len(cmdargs) != 4):
        print "USAGE:python coffee_shops.py <user y coordinate> <user x coordinate> <'CoffeeShops.csv'>"
        sys.exit(1)

    coffeelist = CoffeeShop()
    C1,C2,C3 = coffeelist.get_three_closest_shops(cmdargs[1],cmdargs[2],cmdargs[3])
    print '{},{}'.format(C1[0],C1[1])
    print '{},{}'.format(C2[0],C2[1])
    print '{},{}'.format(C3[0],C3[1])
