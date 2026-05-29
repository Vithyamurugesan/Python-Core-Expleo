from typing import Protocol
class PaymentMethod(Protocol):
    def authorize_payment(self,amount:float)->bool:
        ...
    def process_payment(self,amount:float)->bool:
        ...
class CreditPayment:
    def authorize_payment(self,amount:float)->bool:
        print(f"Authorizing credit card payment of ${amount}")
        return True
    def process_payment(self,amount:float)->bool:
        print(f"Processing credit card payment of ${amount}")
        return True
class PayPalPayment:
    def authorize_payment(self,amount:float)->bool:
        print(f"Authorizing Paypal payment of ${amount}")
        return True
    def process_payment(self,amount:float)->bool:
        print(f"Processing Paypal payment of ${amount}")
        return True
def process_order(payment:PaymentProtocol,amount:float):
    if payment.authorize_payment(amount):
        print("payment successful")
    else:
        print("payment authorization failed")
credit_card_payment=CreditPayment()
paypal_payment=PayPalPayment()

process_order(credit_card_payment,100.0)
process_order(paypal_payment,200.0)
















