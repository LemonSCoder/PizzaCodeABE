import math
from decimal import Decimal
pizza_prices = []
global inputting_prices
inputting_prices = True
while inputting_prices == True:
 def calculate():
  def calculate_for_pizza():
    question = input("Do you want to view pizza prices?\n[Y]YES\n[N]NO\n > ")
    if "Y" in question.upper():
        print(pizza_prices)
        if len(pizza_prices) > 0:
            best_price = pizza_prices[0][1]
            for price in pizza_prices:
                if price[1] < best_price:
                    best_price = price[1]
            print("\nTHE MOST OPTIMAL CHOICE (SO FAR) IS: " + str(best_price) + ".\n")
    elif "N" in question.upper():
        pass
    else:
        print("You didn't put Y or N in your answer.")
    try:
        enter_diameter = float(input("What is the diameter of the pizza you're going to order? > "))
        cost_of_pizza = float(input("What is the cost for one pizza? > "))
        tax_amount = float(input("What percentage is the tax? Answer with a whole number. If there is no percentage, type 0. > "))
        tip_amount = float(input("How much are you planning to tip? > "))
        price_of_toppings = float(input("What are the prices of the toppings? > "))
        slice_number = int(input("How many slices do you want of this pizza? > "))
    except TypeError:
        print("Please input an actual number.")
        calculate()
    pizza_area = ((enter_diameter / 2) ** 2) * 3.14
    try:
        cost_per_area = round(cost_of_pizza / pizza_area, 2)
    except ZeroDivisionError:
        cost_per_area = 0
    multiply_by = 0
    if len(tax_amount) == 1:
        multiply_by = '1.0' + str(int(tax_amount))
    elif len(tax_amount) == 2:
        try:
            multiply_by = '1.' + str(int(tax_amount))
        except TypeError:
            multiply_by = '1.0' + str(round(tax_amount))
    else:
        print("Invalid tip percentage.")
    range_list = [i for i in range(1, 4)]
    range_list_2 = [i for i in range(19, 999)]
    combined_lists = range_list + range_list_2
    pizza_sizes = {
        "Uncalculable" : {
            "size" : [number for number in combined_lists],
        },
        "Extra Small" : {
            "size" : [5, 6, 7],
            "slice_count" : 4,
        },
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
    for sizes, value in pizza_sizes.items():
        slices = 0
        cost_per_slice = 0
        for diameter in value["size"]:
            if diameter == enter_diameter and sizes != "Uncalculable":
                slices = value["slice_count"]
                number_of_pizzas = math.ceil(slice_number / slices)
                total_cost_of_pizzas = (cost_of_pizza * number_of_pizzas) * float(multiply_by) + (float(tip_amount) + price_of_toppings)
                total_slices = slices * number_of_pizzas
                cost_per_slice = total_cost_of_pizzas / total_slices
                message = "You're ordering a(n) " + sizes + " pizza. The cost of all the pizzas are " + str(total_cost_of_pizzas) + ". " +  str(number_of_pizzas) + " pizza(s) are needed. Since this is so, The cost per slice is " + str(cost_per_slice) + " dollars. The cost per square inch of one of the type of pizza you ordered is around " + str(cost_per_area) + " dollars.\n"
                print(message)
                pizza_prices.append([message, total_cost_of_pizzas])
            elif diameter == enter_diameter and sizes == "Uncalculable":
                print("Your pizza is too small or large to be calculated.")
  calculate_for_pizza()
 calculate()
 continue_or_end = input("Are you finished calculating pizza prices?\n[Y]YES\n[N]NO\n > ")
 if "N" in continue_or_end.upper():
    pass
 elif "Y" in continue_or_end.upper():
    break
 else:
    print("You didn't put Y or N in your answer.")
