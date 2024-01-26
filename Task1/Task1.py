def calculate_price(num_pizzas, delivery_required, is_tuesday, used_BPP_app):
    # Constants
    Pizza_Price = 12
    Delivery_Cost = 2.50
    Tuesday_Discount_Percentage = 50
    BPP_App_Discount_Percentage = 25

    # Calculate pizza price
    pizza_total = num_pizzas * Pizza_Price

    # Apply Tuesday discount
    if is_tuesday.upper() == 'Y':
        pizza_total -= pizza_total * (Tuesday_Discount_Percentage / 100)
    

    # Apply delivery cost
    if delivery_required.upper() == 'Y' and num_pizzas < 5:
        pizza_total += Delivery_Cost
    

    # Apply BPP app discount
    if used_BPP_app.upper() == 'Y':
        pizza_total -= pizza_total * (BPP_App_Discount_Percentage / 100)

    return pizza_total

def main():
    BPP = "\nBPP Pizza Price Calculator"
    print(BPP)
    print(len(BPP) * "=")
    
   # Get user input for number of pizzas
    num_pizzas = input("\nHow many pizzas ordered? ")
    while not num_pizzas.isdigit() or int(num_pizzas) <= 0:
        if not num_pizzas.isdigit():
            print("Please enter a number!")
        else:
            print("Please enter a positive integer!")
        num_pizzas = input("How many pizzas ordered? ")
    num_pizzas = int(num_pizzas)

    # Get user input for delivery required
    delivery_required = input("Is delivery required? (Y/N) ")
    while delivery_required not in ['Y', 'N']:
        print('Please answer "Y" or "N".')
        delivery_required = input("Is delivery required? (Y/N) ")

    # Get user input for tuesday
    is_tuesday = input("Is it Tuesday? (Y/N) ")
    while is_tuesday not in ['Y', 'N']:
        print('Please answer "Y" or "N".')
        is_tuesday = input("Is it Tuesday? (Y/N) ")

    # Get user input for app usage
    used_bpp_app = input("Did the customer use the app? (Y/N) ")
    while used_bpp_app not in ['Y', 'N']:
        print('Please answer "Y" or "N".')
        used_bpp_app = input("Did the customer use the app? (Y/N) ")

    # Calculate total price
    total_price = calculate_price(num_pizzas, delivery_required, is_tuesday, used_bpp_app)

    # Display the result
    print("\nTotal Price: £{:.2f}.".format(total_price))


if __name__ == "__main__":
    main()
