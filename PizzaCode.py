def calculate_for_pizza():
    pizza_prices = []
    enter_diameter = int(input("What is the diameter of the pizza you're going to order? > "))
    cost_of_pizza = int(input("What is the cost of the pizza? > "))
    pizza_area = ((enter_diameter / 2) ** 2) * 3.14
    cost_per_area = cost_of_pizza / pizza_area
    pizza_sizes = {
        "Small" : {
            "size" : [8, 9, 10],
            "slice_count" : 6, 
        },
        "Medium" : {
            "size" : [11, 12, 13],
            "slice_count" : 8,
        },
        "Large" : {
            "size" : [14, 15, 16, 17, 18],
            "slice_count" : 10,
        },
    }
    pizza_size = int(enter_diameter)
    slice_number = int(input("How many slices do you want in the pizza? > "))
    for value in pizza_sizes.values():
        slices = 0
        cost_per_slice = 0
        for diameter in value["size"]:
            if diameter == enter_diameter:
                slices = value["slice_count"]
                cost_per_slice = cost_of_pizza / slices
                number_of_pizzas = slice_number / slices
                print(str(slice_number % slices))
                if slice_number % slices != 0:
                    print(round(number_of_pizzas, 0))     
    print(str(round(cost_per_area)))
    print(str(round(pizza_area)))
calculate_for_pizza()
