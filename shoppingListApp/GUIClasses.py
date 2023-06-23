import tkinter as tk
import customtkinter as ctk


shopping_cart = {}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        shopping_cart = {}
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("Shopping Cart App")
        self.geometry("400x800+800+300")
        self.resizable(False,False)
        self.wm_iconbitmap('C:/Users/mail4/Desktop/Coding-Temple/Matrix-123/Week-2/Day-3/Homework/shoppingListApp/images/white-cart-plus-solid.ico')
        
        self.hero = ctk.CTkLabel(self,
                                text='Shopping Cart App',
                                corner_radius= 20,
                                width=375, 
                                height=50,
                                font= ("Roboto", 30),
                                justify='center',
                                fg_color='#0e1011',
                                padx= 0,
                                pady= 0)
        self.hero.pack(padx=0, pady=5)
        
        
        self.file_btns = ctk.CTkFrame(master=self, width=400, height=150, corner_radius=15)
        self.file_btns.pack(padx=0, pady=4)
        self.load_cart = ctk.CTkButton(self.file_btns, text="Load Cart", font=("Roboto", 18,"bold"), command=exit)
        self.load_cart.grid(row=0, column=0, padx=20, pady=8,)
        
        self.save_cart = ctk.CTkButton(self.file_btns, text="Save Cart", font=("Roboto", 18,"bold"), command=exit)
        self.save_cart.grid(row=0, column=1, padx=20, pady=8,)
        
        self.cart_display = ctk.CTkFrame(self, width=350, height=540, bg_color='transparent', fg_color='transparent')
        self.cart_display.pack(padx=0, pady=4)
        self.header = ctk.CTkLabel(self.cart_display,
                                        text= 'Cart Items:',
                                        corner_radius=20,
                                        width= 350,
                                        font= ("Roboto", 20),
                                        justify='center',
                                        anchor='w',
                                        fg_color='#0e1011',
                                        padx= 0,
                                        pady= 0,)
        self.header.grid(row=0,ipadx = 5,ipady = 5)
        
        def clear_items():
            items.destroy()
        
        def displsy_cart_items(dic):
            global items
            for i in range(len(dic.keys())):
                item = list(dic.keys())[i]
                qty = list(dic.values())[i]
                f'{item} : {qty}\n'
                items = ctk.CTkLabel(self.cart_display, 
                            text = f'{item} : {qty}',
                            corner_radius=20,
                            width= 350,
                            font= ("Roboto", 20),
                            justify='center',
                            anchor='w',
                            fg_color='#0e1011',
                            padx= 0,
                            pady= 0,)
                items.grid(row=i+1, ipadx = 5,ipady = 5)
        
        def add_item_dict():
            item_dialog = ctk.CTkInputDialog(text="What item would you like to add to your cart:", title="Item Add")
            item = item_dialog.get_input()
            qty_dialog = ctk.CTkInputDialog(text="How many would you like to add:", title="Item Quantity")
            qty =  qty_dialog.get_input()
            shopping_cart[item] = qty
            displsy_cart_items(shopping_cart)
            
        def remove_item_dict():
            item_dialog = ctk.CTkInputDialog(text="What item would you lik to remove from your cart:", title="Item Remove")
            remove =  item_dialog.get_input()
            if remove in dic:
                del shopping_cart[remove]
            displsy_cart_items(shopping_cart)
            
            
        self.a_r_btns = ctk.CTkFrame(self, width=400, height=150, corner_radius=15)
        self.a_r_btns.pack(padx=0, pady=4)
        self.add_item = ctk.CTkButton(self.a_r_btns, text="Add Item", font=("Roboto", 18,"bold"), command=add_item_dict)
        self.add_item.grid(row=0, column=0, padx=20, pady=8)
        
        self.remove_item = ctk.CTkButton(self.a_r_btns, text="Remove Item", font=("Roboto", 18,"bold"), command=remove_item_dict)
        self.remove_item.grid(row=0, column=1, padx=20, pady=8)
        
        self.close_app = ctk.CTkButton(self, text="Close", font=("Roboto", 18,"bold"), command= exit)
        self.close_app.pack(padx=10, pady=(25,5))

    
app = App()
app.mainloop()