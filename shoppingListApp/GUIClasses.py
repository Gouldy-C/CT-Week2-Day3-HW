import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
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
        self.load_cart = ctk.CTkButton(self.file_btns, text="Load Cart", font=("Roboto", 18,"bold"), command=button_click_event)
        self.load_cart.grid(row=0, column=0, padx=20, pady=8,)
        
        self.save_cart = ctk.CTkButton(self.file_btns, text="Save Cart", font=("Roboto", 18,"bold"), command=button_click_event)
        self.save_cart.grid(row=0, column=1, padx=20, pady=8,)
        
        
        self.cart_display = ctk.CTkLabel(self,
                                        text='Shopping Cart\n\n',
                                        corner_radius= 20,
                                        width=375, 
                                        height=540,
                                        font= ("Roboto", 20),
                                        justify='left',
                                        anchor='nw',
                                        fg_color='#0e1011',
                                        padx= 5,
                                        pady= 10)
        self.cart_display.pack(padx=20, pady=4)
        
        
        self.a_r_btns = ctk.CTkFrame(self, width=400, height=150, corner_radius=15)
        self.a_r_btns.pack(padx=0, pady=4)
        self.add_item = ctk.CTkButton(self.a_r_btns, text="Add Item", font=("Roboto", 18,"bold"), command=button_click_event)
        self.add_item.grid(row=0, column=0, padx=20, pady=8)
        
        self.remove_item = ctk.CTkButton(self.a_r_btns, text="Remove Item", font=("Roboto", 18,"bold"), command=button_click_event)
        self.remove_item.grid(row=0, column=1, padx=20, pady=8)
        
        self.close_app = ctk.CTkButton(self, text="Close", font=("Roboto", 18,"bold"), command= exit)
        self.close_app.pack(padx=10, pady=(25,5))

def button_click_event():
            dialog = ctk.CTkInputDialog(text="Type in a number:", title="Test")
            print("Number:", dialog.get_input())
            dialog2 = ctk.CTkInputDialog(text="Type in a number:", title="Test")
            print("Number:", dialog2.get_input())
app = App()
app.mainloop()