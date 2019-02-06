class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total=0
        self.employee_discount=emp_discount
        self.items=[]

    def add_item(self, name, price, quantity=1):
        for item in range(quantity):
            self.items.append(price)
            self.total+=price
        return self.total
        
    def mean_item_price(self):
        print (self.items)
        return self.total/len(self.items)

    def median_item_price(self):
        itemized=sorted(self.items)
        if len(itemized)%2==1:
            return itemized[len(itemized)//2]
        else:
            return sum(itemized[len(itemized)//2:(len(itemized)//2+1)])/2

    def apply_discount(self):
        if self.employee_discount != None:
            discount=self.total*(100-self.employee_discount)/100
            return discount
        else:
            return "Sorry, there is no discount to apply to your cart:("
    def void_last_item(self):
        if len(self.items)==0:
            return "There are no items in your cart!"
        self.total-=self.items[-1]
        self.items.pop(-1)
        return self.total