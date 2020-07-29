'''编写程序并测试，有一个汽车类Vehicle，类中的私有数据成员为车轮个数wheels和车重weight；小车类Car是汽车类vehicle派生类，其中包含载客人数passenger_load，默认4人；卡车类Truck是汽车类vehicle派生类，其中包含载客人数passenger_load和载重量payload。
提示：编写类时要使用get和set方法，Vehicle类定义display()显示车轮和重量，Car和Truck中要对display()进行同名覆盖。'''

class Vehicle(object):
    def  __init__(self,wheels,weight):   #车轮个数wheels和车重weight
        self.__wheels=wheels
        self.__weight=weight

    def setWheels(self,wheels):
        self.__wheels=wheels

    def setWeight(self, weight):
        self.__weight=weight

    def display(self):
        print('车轮个数为：',self.__wheels)
        print('车重为：',self.__weight)

class Car(Vehicle):
    def __init__(self,wheels,weight,passenger_load=4):
        super(Car, self).__init__(wheels,weight)
        self.setPassenger_load(passenger_load)

    def setPassenger_load(self,passenger_load):
        self.__passenger_load=passenger_load

    def display(self):
        super(Car, self).display()
        print('小车载客人数为：', self.__passenger_load)

class Truck(Vehicle):
    def __init__(self, wheels, weight, passenger_load,payload):
        super(Truck,self).__init__(wheels,weight)
        self.setPassenger_load(passenger_load)
        self.setPayload(payload)

    def setPassenger_load(self, passenger_load):
        self.__passenger_load=passenger_load

    def setPayload(self,payload):
        self.__payload=payload


    def display(self):
        super(Truck, self).display()
        print("卡车载客人数为：", self.__passenger_load)
        print("卡车载重为：", self.__payload)

if __name__=='__main__':
    vehicle=Vehicle(4,5)
    vehicle.display()
    print('=' * 30)

    car=Car(4,45,5)
    car.display()
    print('=' * 30)

    truck=Truck(1,2,3,4)
    truck.display()
    print('=' * 30)
