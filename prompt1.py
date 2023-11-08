import random

#generate a random transaction ID
transaction_ID=''.join(random.choice('0123456789ABCDEF')for i in range(8)) 

#prompt user payment details
print("Welcome to my payment system")
print(f"your transaction ID is:{transaction_ID}")
#get payment from the user
while True:
  try:
       payment_amount=float(input("Entert the payment amount:ksh"))
       break
  except ValueError:
      print("Invalid input.please enter a valid amount.")
      
print("please choose a payment method:")
print("1.Credit Card")
print("2.mobile wallet")
payment_method=input("Enter the number of your choice:")

if payment_method=="1":
    # payment with credit card
    card_number=input("Enter you credit card number")
    expiration_date=input("Enter the expiration date (MM/YY):")
    cvv=input("Enter cvv:")
    print(f"processing of payment of ksh{payment_amount}....")
    # you would intergrate with payment gate way here to process the payment.
    
elif payment_method=="2":
     #payment with mobile wallet.
     mobile_number=input("Enter your mobile wallet number")
     pin=input("Enter your mobile wallet pin")
     print(f"processing of payment of ksh{payment_amount}")
     # You would integrate with a mobile wallet API here to process the payment.
     
else:
     print("Invalid choice.please select a valid payment method (1 or 2).")
     
print(f"thank you for payment of ksh{payment_amount}")
     
     
    
        