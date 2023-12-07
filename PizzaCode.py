#The math module is used to perform math.ceil() later.
import math
#pizza_prices is created so that the code can later recognize which pizza is the most optimal choice to order.
pizza_prices = []
global inputting_prices
inputting_prices = True
#This calculating the price of pizza continues through this loop.
while inputting_prices == True:
 #Stops some code from repeating.
 def calculate():
  def calculate_for_pizza():
   #Allows for the user to view past pizza prices for pizzas they've inputted into the code before.
    question = input("Do you want to view pizza prices?\n[Y]YES\n[N]NO\n > ")
    #Pizza prices are viewed if and only if Y is input in question.upper().
    if "Y" in question.upper():
        print(pizza_prices)
        #This code displays the most optimal pizza(s) to buy through total price and cost per square inch of pizza.
        if len(pizza_prices) > 0:
            best_price = pizza_prices[0][0]
            best_size = pizza_prices[0][1]
            for price in pizza_prices:
                if price[0] < best_price:
                    best_price = price[0]
                    print("\nTHE MOST OPTIMAL CHOICE (IN TERMS OF COST) IS: " + str(best_price) + " .\n")
                elif price[1] < best_size:
                    best_price = price[1]
                    print("\nTHE MOST OPTIMAL CHOICE (IN TERMS OF SIZE) IS " + str(best_size) + "dollars per square inch.\n")       
    elif "N" in question.upper():
        pass
    else:
        #Code runs as if "N" was input by the user.
        print("You didn't put Y or N in your answer.")
    #Try and except function is present in order to make sure that the user isn't inputting anything that can't be converted into an integer or a float.
    try:
        #Allows user to input diameter of the pizza.
        enter_diameter = float(input("What is the diameter of the pizza you're going to order? > "))
        #Calculates the area of a circular pizza: 3.14 * r^2
        pizza_area = ((enter_diameter / 2) ** 2) * 3.14
        #Allows user to input cost of the pizza.
        cost_of_pizza = float(input("What is the cost for one pizza? > "))
        #Allows user to input the tax percentage. Start of Challenge A.
        tax_amount = input("What percentage is the tax? If there is no percentage, type 0. > ")
        #Allows user to input a tip amount. Start of Challenge B.
        tip_amount = float(input("How much are you planning to tip? > "))
        #Allows user to input topping prices.
        price_of_toppings = float(input("What are the prices of the toppings? > "))
        #Allows user to input number of slices of the pizza they want to have.
        slice_number = int(input("How many slices do you want of this pizza? > "))
        #Cost per square inch of pizza is rounded to six decimal places if cost per square inch of pizza can't be rounded to three decimal places.
        try:
          cost_per_area = round(cost_of_pizza / pizza_area, 3)
        except ZeroDivisionError:
          cost_per_area = round(cost_of_pizza / pizza_area, 6)
        #Variable where tax percentage is going to be stored.
        multiply_by = 0
        #Checks if tax_amount is one or two digits long and assigns what the total cost of pizza has to be multiplied by for the tip.
        if len(tax_amount) == 1:
          multiply_by = '1.0' + str(int(tax_amount))
        elif len(tax_amount) == 2:
        #Makes sure tax percentage can be approximated if the tax percentage is a decimal value.
          try:
            multiply_by = '1.' + str(int(tax_amount))
          except ValueError:
            multiply_by = '1.0' + str(round(float(tax_amount), 2))
        #Makes sure cost per square inch of pizza can be rounded to three decimal places.
        #After the try and except function, if the tip percentage is still invalid, then the print statement: "Invalid tip percentage." will appear.
        else:
            print("Invalid tax percentage.")
        #Calculates for any pizza diameter lengths that are less than the ones in the "size" section of the "Extra Small" section of the pizza_sizes dictionary.
        range_list = [i for i in range(1, 4)]
        #Calculates for any pizza diameter lengths that are greater than the ones in the "size" section of the "Large" section of the pizza_sizes dictionary.
        range_list_2 = [i for i in range(19, 999)]
        #Combines both of the above lists into one giant list.
        combined_lists = range_list + range_list_2
        #Compiles uncalculable, Extra Small, Small, Medium, and Large pizzas' average diameters and average slice counts.
        pizza_sizes = {
              "Uncalculable" : {
                  "size" : [number for number in combined_lists],
              },
              "Extra Small" : {
                  "size" : [number for number in range(5, 8)],
                  "slice_count" : 4,
              },
              "Small" : {
                  "size" : [number for number in range(8, 11)],
                  "slice_count" : 6, 
              },
              "Medium" : {
                  "size" : [number for number in range(11, 14)],
                  "slice_count" : 8,
              },
              "Large" : {
                  "size" : [number for number in range(14, 19)],
                  "slice_count" : 10,
              },
        }
        #Grabs both the keys and values from pizza_sizes.
        for sizes, value in pizza_sizes.items():
            slices = 0
            cost_per_slice = 0
            #Grabs "size" from Uncalculable, Extra Small, Small, Medium, and Large.
            for diameter in value["size"]:
                #Makes sure diameter user inputted isn't in the "Uncalculable" section of pizza_sizes.
                if diameter == enter_diameter and sizes != "Uncalculable":
                    #Takes the slice count in pizza_slices if the user's input diameter aligns with one of the diameter sizes in Extra Small, Small, Medium, or Large.
                    slices = value["slice_count"]
                    #Rounds number of pizzas up since a user my end up with 1.4 pizzas, which needs to be rounded up to 2.
                    number_of_pizzas = math.ceil(slice_number / slices)
                    #Cost of pizzas: pizza cost times number of pizzas times the tax percentage plus the tip amount and price of toppings.
                    total_cost_of_pizzas = (cost_of_pizza * number_of_pizzas) * float(multiply_by) + (float(tip_amount) + price_of_toppings)
                    #Calculates total number of slices from all of the pizzas.
                    total_slices = slices * number_of_pizzas
                    #Calculates cost per slice.
                    cost_per_slice = round(total_cost_of_pizzas / total_slices, 2)
                    #Compiles all necessary data for the user to see.
                    message = "You're ordering a(n) " + sizes + " pizza. The cost of all the pizzas are " + str(total_cost_of_pizzas) + ". " +  str(number_of_pizzas) + " pizza(s) are needed. Since this is so, The cost per slice is around " + str(cost_per_slice) + " dollars. The cost per square inch of one of the type of pizza you ordered is around " + str(cost_per_area) + " dollars.\n"
                    print(message)
                    #All necessary data and total cost are appended to pizza_prices as a list.
                    pizza_prices.append([total_cost_of_pizzas, cost_per_area])
                elif diameter == enter_diameter and sizes == "Uncalculable":
                    #Ensures that data won't be shown to the user if the pizza, given its diameter from the user, is too small or large to be calculated. 
                    print("Your pizza is too small or large to be calculated.")
    except ValueError:
        #Tells user to input a number if they catch any non-integer or non-float convertable inputs. The user is sent back to entering the pizza's diameter if the code catches any non-integer or non-float convertable inputs.
        print("Please input a valid answer.")
        calculate()
  calculate_for_pizza()
 calculate()
 #Asks if the user is done calculating for pizza prices.
 continue_or_end = input("Are you finished calculating pizza prices?\n[Y]YES\n[N]NO\n > ")
 if "N" in continue_or_end.upper():
    #Code keeps going if "N" in response from user.
    pass
 elif "Y" in continue_or_end.upper():
    #Code terminates if "Y" in response from user. Break is declared outside of the function since it doesn't function when inside the function.
    break
 else:
    #Code acts as if "N" was in user's response.
    print("You didn't put Y or N in your answer.")
