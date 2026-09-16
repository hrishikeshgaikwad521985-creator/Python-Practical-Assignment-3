from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount, user_info=None):
        pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount, user_info=None):
        print(f"Paid ₹{amount} using Credit Card ending with {user_info.get('card_number')[-4:]}")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount, user_info=None):
        print(f"Paid ₹{amount} using PayPal account: {user_info.get('email')}")

class UpiPayment(PaymentStrategy):
    def pay(self, amount, user_info=None):
        print(f"Paid ₹{amount} using UPI ID: {user_info.get('upi_id')}")

# Step 3: Context Class
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount, user_info=None):
        self._strategy.pay(amount, user_info)

# Step 4: User Interaction
if __name__ == "__main__":
    print("Welcome to Configurable Payment System")
    print("Choose Payment Method:")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. UPI")

    choice = int(input("Enter choice (1/2/3): "))
    amount = float(input("Enter amount to pay: ₹"))

    if choice == 1:
        card_number = input("Enter Credit Card Number: ")
        processor = PaymentProcessor(CreditCardPayment())
        processor.process_payment(amount, {"card_number": card_number})

    elif choice == 2:
        email = input("Enter PayPal Email: ")
        processor = PaymentProcessor(PayPalPayment())
        processor.process_payment(amount, {"email": email})

    elif choice == 3:
        upi_id = input("Enter UPI ID: ")
        processor = PaymentProcessor(UpiPayment())
        processor.process_payment(amount, {"upi_id": upi_id})

    else:
        print("Invalid choice. Please try again.")