#==============================
#CLOTHING WEBSITE ORDER PROCESS
#==============================
import random

orders = []

products = {
    "1": ("shirt", 20.00),
    "2": ("hoodie", 30.00),
    "3": ("shorts", 12.00),
    "4": ("sweatpants", 18.00)
}

test_cards = {
    "TEST-APPROVE": True,
    "TEST-DECLINE": False
}

def show_products():
    """display all available products and their prices."""
    print("\n--- clothing ----")
    
    for number, item in products.items():
        name, price = item
        print (f"{number}. {name}: ${price:.2f}")

def receive_order ():
    """display an order was recieved."""
    
    customer = input("customer name: ").strip()
    if not customer:
        print("error: name is required.")
        return
    show_products()

    choice = input("choose a product number:")

    if choice not in products:
        print("error: product not found.")
        return

    product_name, price = products [choice]

    try: 
        quantity = int(input("quantity (1-10):"))
    except ValueError:
        print("error: enter a whole number.")
        return

    if quantity < 1 or quantity > 10:
        print("error: quantity must be 1-10.")
        return

    total = price * quantity 

    print(f"\ncustomer: {customer}")
    print(f"product: {product_name}")
    print(f"quantity: {quantity}")
    print(f"total: ${total:.2f}")

    print("\n--- simulated payment ---")
    print("use TEST-APPROVE or TEST-DECLINE")
    token = input("test payment token:").strip().upper()

    if token not in test_cards:
        print("error: unknown test token.")
        return

    if test_cards[token] == False:
        print("payment declined (simulation).")
        return

    order = {
        "id": random.randint(10000, 99999),
        "customer": customer,
        "product": product_name,
        "quantity": quantity,
        "total": round(total, 2),
        "status": "approved"
    }

    orders.append(order)

    print("\norder recieved successfully!")
    print(f"order ID: {order['id']}")
    print(f"payment status: {order['status']}")
    print(f"amount: ${order ['total']:.2f}")


def show_orders():
    """display all orders."""
    print("\n--- order history ---")
    
    if len(orders) == 0:
        print("no approved orders yet.")
        return

    for order in orders:
        print("----------------------")
        print(f"ID: {order['id']}")
        print(f"customer: {order['customer']}")
        print(f"product: {order['product']}")
        print(f"quantity: {order['quantity']}")
        print(f"total: ${order['total']}")
        print(f"status: {order['status']}")


def main():
    """run the main menu for joseph's order receiver."""
    print("welcome to joseph, the order receiver!")
    
    while True:
        print("\n--- joseph's order reciever ---")
        print("1. receive an order")
        print("2. view order history")
        print("3. view products")
        print("4. exit")

        option = input("select an option: ").strip()

        if option == "1":
            receive_order()

        elif option == "2":
            show_orders()

        elif option == "3":
            show_products()

        elif option == "4":
            print("order receiver joseph shutting down.")
            break

        else:
            print("invalid option. try again!")


if __name__ == "__main__":
    main()      

#================================================================================
#       DON'T WORRY     JOSEPH WAS NEVER FORCED TO BE HERE IN THE FIRST PLACE
#================================================================================ 