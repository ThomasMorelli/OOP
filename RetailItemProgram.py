import RetailItemClass as ri


item1 = ri.RetailItem("Jacket", 12, 59.95)
item2 = ri.RetailItem("Designer Jeans", 40, 34.95)
item3 = ri.RetailItem("Shirt", 20, 24.95)


print("Item 1:", item1.description, "-", item1.units_in_inventory, "units - $", item1.price)
print("Item 2:", item2.description, "-", item2.units_in_inventory, "units - $", item2.price)
print("Item 3:", item3.description, "-", item3.units_in_inventory, "units - $", item3.price)