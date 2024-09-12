def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount if discount_percent is 20% or higher.
           Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

def main():
    # Get user input for price and discount percentage
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Call the calculate_discount function
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price or the original price
        if discount_percent >= 20:
            print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${price:.2f}")
    
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
