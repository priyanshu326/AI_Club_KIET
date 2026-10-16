purchase_amount = float(input("Enter the purchase amount: "))
membership = input("Enter membership type (Gold, Silver, Regular): ")
payment_method = input("Enter payment method (Online or Cash): ")

if membership == "Gold":
    discount = purchase_amount * 0.20
elif membership == "Silver":
    discount = purchase_amount * 0.10
else:
    discount = 0  
    
remaining_amount = purchase_amount - discount
total_discount = discount


if remaining_amount >= 5000:
    extra_discount = remaining_amount * 0.05
    remaining_amount = remaining_amount - extra_discount
    total_discount = total_discount + extra_discount


if payment_method == "Online" and remaining_amount >= 2000:
    remaining_amount = remaining_amount - 200
    total_discount = total_discount + 200

final_amount = remaining_amount


if final_amount < 1000:
    category = "Small Order"
elif final_amount <= 5000:
    category = "Standard Order"
else:
    category = "Premium Order"


print("\n--- BILL DETAILS ---")
print("Total Discount Given:", total_discount)
print("Final Payable Amount:", final_amount)
print("Order Category:", category)