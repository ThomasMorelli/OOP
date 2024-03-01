import InsectClass as i

def main():
    housefly = i.Insect()
    mosquito = i.Insect()

    housefly.calc_flight()
    mosquito.calc_flight()

    print(f"The fly can fly {housefly.get_miles()} miles")
    print(f"The mosquito can fly {mosquito.get_miles()} miles")

main()