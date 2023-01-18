from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def add_to_inventory(self):
        return self.quantity_on_hand + 2

    def method1(self):
       x =  self.add_to_inventory
       print("do something again")

    def method1(self):
       x =  self.add_to_inventory
       print("do something again again")

    def method1(self):
       x =  self.add_to_inventory
       print("do something again again again again")

    def method1(self):
       x =  self.add_to_inventory
       print("do something again again again again again ")

    def method1(self):
       x =  self.add_to_inventory
       print("do something but not again")

    def method1(self):
       x =  self.add_to_inventory
       print("do something but not again")

    def method1(self):
       x =  self.add_to_inventory
       print("do something but not again")
