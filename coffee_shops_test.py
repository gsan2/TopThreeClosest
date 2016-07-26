import unittest
from coffee_shops import CoffeeShop

class CoffeeShopTests(unittest.TestCase):

    def testThreeClosestShops(self):
        print "running testThreeClosestShops"
        test_coffee = CoffeeShop()
        C1, C2, C3 = test_coffee.get_three_closest_shops(47.6,-122.4,'TestCoffeeShops.csv')
        assert(C1[0] == 'Starbucks Seattle2' and C1[1] == 0.0645)
        assert(C2[0] == 'Starbucks Seattle' and C2[1] == 0.0861)
        assert(C3[0] == 'Starbucks SF' and C3[1] == 10.0793)

    def testListValidity(self):
        print "running testListValidity"
        test_coffee = CoffeeShop()
        data1 = ['seattle',None,'90.02']
        data2 = ['seattle',40.2,'90.02']
        self.assertEqual(test_coffee.check_validity(data1),0)
        self.assertEqual(test_coffee.check_validity(data2),1)

    def testHandleEquiDistantShops(self):
        print "running testHandleEquiDistantShops"
        test_coffee = CoffeeShop()
        C1, C2, C3 = test_coffee.get_three_closest_shops(2.0,2.0,'TestEquiCoffeeShops.csv')


    #def testAtLeastThreeEntriesInCoffeeShopsList(self):

if __name__ == '__main__':
    unittest.main()
