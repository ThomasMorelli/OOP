import CarClass as c

def main():
    my_car = c.Car(2022, "Toyota")

  
    print("Accelerating...")
    for i in range(5):
        my_car.accelerate()
        print("Current Speed:", my_car.get_speed())


    print("Braking...")
    for i in range(5):
        my_car.brake()
        print("Current Speed:", my_car.get_speed())

main()