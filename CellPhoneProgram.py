import CellPhoneClass as c

def main():
    
    # Create a cell phone object
    cellphone = c.Cellphone("Apple", "iPhone 15", 1099)

    # Change the retail price
    cellphone.set_retail_price(999)

    # Display phone information
    print("Manufacturer:", cellphone.get_manufact())
    print("Model:", cellphone.get_model())
    print("Retail Price:", cellphone.get_retail_price())

   
main()