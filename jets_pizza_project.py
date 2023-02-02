#define our pricing function
def pizza_price():
    
    base_price = 15
    tax_percent = 0.0625
    
    toppings = input("What Toppings? (Use all caps)\n").upper()
    calculated_toppings_list = []
    
    for character in toppings:
    
        if character in calculated_toppings_list:
            continue
        
        if character == "T":
            base_price = base_price + 1.50
        
        if character == "O":
            base_price = base_price + 1.25
        
        if character == "P":
            base_price = base_price + 3.50
        
        if character == "M":
            base_price = base_price + 3.75
        
        if character == "A":
            base_price = base_price + 0.40
            
        calculated_toppings_list.append(character)
    if base_price >= 20.00:
        base_price = base_price * 0.95
    sub_total = base_price
    tax_price = sub_total * tax_percent
    total_price = sub_total + tax_price
    total_price = round(total_price, 2)
    tax_price = round(tax_price, 2)
    sub_total = round(sub_total, 2)
    
    print("Subtotal: " + str(sub_total))
    print("Tax(6.25%):" + str(tax_price))
    print("Total:" + str(total_price))
    
pizza_price()
