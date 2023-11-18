#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount =0):
    self.discount = discount
    self.total = 0
    self.items=[]

  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.items.extend([title] * quantity)

  def apply_discount(self) :
    if self.discount > 0:
      discount_amount = (self.discount / 100)  * self.total
      self.total = round(self.total - discount_amount)
      print(f"After the discount, the total comes to ${self.total}.") 
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
      if self.items:
          last_item_price = self.price_of_item(self.items[-1])
          print(f"Before void: total = {self.total}, items {self.items}")
          self.total -= last_item_price
          self.items.pop()
          print(f"After void: total = {self.total},items= {self.items}")
      else:
          print("No transactions to void.")

  def price_of_item(self, item):
    return 0

  def reset_register_totals(self):
    self.cash_register.total = 0
    self.cash_register.items = []
    self.cash_register_with_discount.total = 0
    self.cash_register_with_discount.items = []