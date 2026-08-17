class Product:
    def __init__(self,product,price,qty):
        self.product=product
        self.price=price
        self.qty=qty

    def __str__(self):
        return f"{self.product} - ₹{self.price} - Quantity: {self.qty}"


class Customer:
    def __init__(self,name,shop):
        self.name=name
        self.shop=shop
        self.cart=[]

    def __str__(self):
        return "\n".join(f"{c[0].title()} - Quantity: {c[1]}" for c in self.cart)
    
    
    def check_product(self):
        for p in self.shop.product:
            print(p)
    
    
    def add_to_cart(self):
        try:
            prd = input("Enter the product = ")
    
            for p in self.shop.product:
                if p.product.lower() == prd.lower():
    
                    amount = int(input("Enter the amount = "))
    
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        return
    
                    if amount <= p.qty:
    
                        for item in self.cart:
                            if item[0].lower() == prd.lower():
                                item[1] += amount
                                p.qty -= amount
                                return
    
                        self.cart.append([prd, amount])
                        p.qty -= amount
                        return
    
                    else:
                        print("Not enough quantity available")
                        return

            print(prd, "is not available")

        except ValueError:
            print("Please enter a valid number.")


    def remove_from_cart(self):
        try:
            prd = input("Enter the product to be removed = ")
            amount = int(input("Enter the amount = "))
    
            if amount <= 0:
                print("Amount must be greater than 0.")
                return
    
            for i in self.cart:
                if i[0].lower() == prd.lower():
    
                    if amount > i[1]:
                        print("You don't have that much in the cart.")
                        return
    
                    # Return the removed quantity to the shop
                    for p in self.shop.product:
                        if p.product.lower() == i[0].lower():
                            p.qty += amount
                            break
    
                    if amount == i[1]:
                        self.cart.remove(i)
                    else:
                        i[1] -= amount
    
                    return
    
            print(prd, "is not in your cart.")
    
        except ValueError:
            print("Please enter a valid number for amount.")
    
    
    def check_cart(self):
        return self.cart
    



class Shop:
    def __init__(self):
        self.product=[Product(product="Bread",price=50,qty=45000),
                      Product(product="Egg",price=5,qty=12),
                      Product(product="Milk",price=76,qty=14)]

class Checkout:
    def __init__(self,customer,shop):
        self.customer=customer
        self.shop=shop

    def total_bill (self):
        bill=0
        print("____________________________________________________________")
        print("\n                         THE BILL       \n")
        print("____________________________________________________________")
        for p in self.shop.product:
            for c in self.customer.cart:
                if p.product.lower() == c[0].lower():
                    bill=bill+(c[1]*p.price)
                    
        
        print(self.customer)
        print("____________________________________________________________")
        print("\n")
        print("The Total Amount - ",bill)
        print("Customer name - ",self.customer.name)
        print("____________________________________________________________")
        
print("\n                           PyMarket                                  \n")                 
name=input("Enter your name = ")
print("Welcome to PyMarket",name)
b=Shop()     
a=Customer(name,b)
c=Checkout(a,b)
while True:
    t=int(input("\n Enter your choice - \n \n 1 : Check the shop \n 2 : Start shopping \n 3 : Remove item from cart \n 4 : Check your cart \n 5 : Get bill \n 6 : Exit the menu \n Your choice - "))
    if t== 1:
        print("\nThe product available in the store  \n")
        a.check_product()
    elif t == 2:
        while True:
            q=input("Want to shop (Y/N) = ")
            if q.lower() == "y":
                a.add_to_cart()
            elif q.lower() == "n":
                break
            else:
                print("Enter valid input")
    elif t==3:
        a.remove_from_cart()
    elif t==4:
        print("\n")
        for p in a.check_cart():
            print(p[0].title(),"-",p[1])
    elif t==5:
        c.total_bill()
    elif t == 6:
        print("\nThanking for visiting the store")
        break
    else:
        print("Enter a valid number (1,2,3,4,5,6)")
