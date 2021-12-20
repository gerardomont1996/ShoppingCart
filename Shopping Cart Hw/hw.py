
def shopping_cart(cart_list):
        total=0
        cart_list={}
        while True:
            
            ask=input("What would you like to add/remove/show/Quit/Total ?").lower()
            if ask == 'quit':
                   break 
            elif ask == 'add':
                add_list=input('What would you like to add to your cart?')
                total == float (input(f'How much does it cost?'))
                quantity ==int(input("How many would you like to add?"))
            cart_list == [total, quantity] 
            clear_output()

            elif "ask" == "remove"
            ask=input("What would you like to remove?")
            del shopping_cart[cart_list[0]]
            total_for_cart=[]
            elif ask=="show".
            shopping_cart (cart_list)
            for total in cart_list:
                cart_total=cart_list[0] + cart_list[1]
                total_for_cart.append(cart_total)
                print(total_for_cart)

            elif ask =="clear"
            cart_list.clear()
            print("Nothing in your list")
            

         


            shopping_cart(cart_list)      
