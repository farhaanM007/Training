import sys


class Productcatalog:
    def __init__(self,name,price,description,SKU):
        self.name=name
        self.price=price
        self.descrption=description
        self.SKU=SKU


    def __str__(self):
        return (
            f"Product Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Description: {self.descrption}\n"
            f"SKU: {self.SKU}\n"
            

        )
    

class Shoppingcart:
    def __init__(self):
        self.items=[]

    def addItems(self,product,itemQty=1):
        self.items.append({"product":product,"qty":itemQty})

    def removeItem(self,product):
        for item in self.items:
            if item["product"]==product:
                self.items.remove(item)


    def totalPrice(self):
        total=0
        for item in self.items:
            
            total+=item["product"].price * item["qty"]

        return total
            

    def __str__(self):
        catstr=""

        for item in self.items:
            product=item["product"]
            catstr+=f"\nProduct: {product.name}\n"+f"Quantity:{item['qty']} \n"

        return catstr



class User:
    def __init__(self,name,address,email):
        self.name=name
        self.address=address
        self.email=email

    def __str__(self):
        return f"{self.name,self.address,self.email}"

    

class Order:
    def __init__(self,user,cart):
        self.user=user
        self.cart=cart
        self.order_status="Pending"

    def place_order(self):
        self.order_status="Placed"

    def cancel_order(self):
        self.order_status="Cancelled"

    def order_details(self):

        print("Order Details: \n")
        print("User Information:")
        print(f"\nName:{self.user.name}")
        print(f"Email:{self.user.email}")
        print(f"Address:{self.user.address}\n")
        print("Products Purchased:\n")
        for item in self.cart.items:
            product = item["product"]
            quantity = item["qty"]
            print(f"Product: {product.name}")
            print(f"Price:${product.price}")
            print(f"Quantity: {quantity}\n")

        print(f"Total Price: ${self.cart.totalPrice()}\n")

        

    def __str__(self):
        return f"{self.user.name,self.cart.items,self.status}"


    
#Product Catalog Objects

product1=Productcatalog("Adidas Hightop Shoes",3000,"New Adidas Shoes White","ADD-HS-WH-007")
product2=Productcatalog("Nike Hightop Shoes",4000,"New Nike Shoes White","NK-HS-WH-008")
product3=Productcatalog("Puma Hightop Shoes",3000,"New Puma Shoes White","PUM-HS-WH-007")

productList=[product1,product2,product3]

cart=Shoppingcart()


userName=input("Enter Name: ")
userEmail=input("Enter Email: ")
userAddress=input("Enter Address : ")

customer=User(userName,userAddress,userEmail)

choice="y"

print(f"\nWelcome {customer.name} \n")



#Code for Add or delete products in cart

while choice=="y":


    print("Here are the items available in the Shop: \n")

    for item in productList:
        print(item)

    chooseItem=int(input("""
        Enter "1" for First Product
        Enter "2" for Second Product
        Enter "3" for Third Product
        Select Product: """))

    

    if chooseItem==1:
        chooseQty=int(input("\nSelect Quantity: "))
        cart.addItems(product1,chooseQty)
    elif chooseItem==2:
        chooseQty=int(input("\nSelect Quantity: "))
        cart.addItems(product2,chooseQty)
    elif chooseItem==3:
        chooseQty=int(input("\nSelect Quantity: "))
        cart.addItems(product3,chooseQty)

    else:
        print("No items selected \n")

    print("\nProducts Added:")
    print(cart)

    #Code for deleting Product from cart

    if len(cart.items)>0:
        delChoice=input("Do  you want delete any items(y/n) ?")

        while delChoice=="y":
            delItem=int(input("\n Select items to delete according to the number system as above \n"))

            if delItem==1:
                cart.removeItem(product1)

            elif delItem==2:
                cart.removeItem(product2)

            elif delItem==3:
                cart.removeItem(product3)
            else:
                print("Wrong Input")

            print(cart)

            delChoice=input("\n Do you want to delete anymore item?(y/n)\n")

    print("\nProducts Added:")
    print(cart)

    print(f"Total Price:${cart.totalPrice()} \n")





    choice=input("Do do want to continue your shopping?(y/n)")


placeOrder=Order(customer,cart)

placeOrder.order_details()

#Code for choosing order status

while placeOrder.order_status=="Pending":

    order_choice=int(input("Press 1 to confirm order Or Press 2 to Cancel order "))

    if order_choice==1:
        placeOrder.place_order()

    elif order_choice==2:
        placeOrder.cancel_order()
    else:
        print("Wrong input")



if placeOrder.order_status=="Placed":
    sys.exit("Order Placed")

else:
    sys.exit("Order Cancelled")



    








