from tkinter import *
class Canteen_Bill:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x720+0+0")
        self.root.title("Billing Software for Softwarica's Canteen")
        self.root.iconbitmap('bill.ico')
        bg_color = "#143875"

 # Frame1 Customer Detail Frame 
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0, y=0, relwidth=1)

        # Frame1 Customer Details Variable types
        self.name=StringVar()
        self.phone=StringVar()
        self.bill=StringVar()
        
        name_lbl=Label(F1, text="Name: ", bg=bg_color, fg="white", font=("times new roman",18,"bold")).grid(row=0, column=0, padx=20, pady=5)
        name_txt=Entry(F1,width=20, bd=7, relief=SUNKEN,textvariable=self.name ,font="arial 15").grid(row=0,column=1,pady=5,padx=10)

        phone_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        phone_txt = Entry(F1, width=18,bd=7,relief=SUNKEN,textvariable=self.phone ,font="arial 15").grid(row=0, column=3, pady=5, padx=10)

        bill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        billtxt = Entry(F1, width=10,bd=7,relief=SUNKEN,textvariable=self.bill, font="arial 15").grid(row=0, column=5, pady=5, padx=10)
        
        search_btn=Button(F1,text="Search",width=10,bd=7,relief=GROOVE, font="arial 12 bold").grid(row=0, column=6,padx=10,pady=0)

#  Frame2  Snack items
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Snacks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5, y=90,width=325,height=530)

        # Snacks Variable types
        self.pop_corn=IntVar()
        self.noodle=IntVar()
        self.muffin=IntVar()
        self.samosa=IntVar()
        self.burger=IntVar()
        self.veg_sandwich=IntVar()
        self.fried_egg=IntVar()
        self.sel_roti=IntVar()
        self.chatamari=IntVar()
        self.dahi_chiura=IntVar()

        f2_lbl1=Label(F2,text="Pop Corn",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10,pady=7,sticky="w")
        f2_txt1=Entry(F2,width=8,textvariable=self.pop_corn,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7)

        f2_lbl2=Label(F2,text="Noodle",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0,padx=10,pady=7,sticky="w")
        f2_txt2=Entry(F2,width=8,textvariable=self.noodle, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=7)

        f2_lbl3=Label(F2,text="Muffin",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0,padx=10,pady=7,sticky="w")
        f2_txt3=Entry(F2,width=8,textvariable=self.muffin, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=7)

        f2_lbl4=Label(F2,text="Samosa",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0,padx=10,pady=7,sticky="w")
        f2_txt4=Entry(F2,width=8,textvariable=self.samosa, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=7)

        f2_lbl5=Label(F2,text="Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4, column=0,padx=10,pady=7,sticky="w")
        f2_txt5=Entry(F2,width=8,textvariable=self.burger, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=7)

        f2_lbl6=Label(F2,text="Veg Sandwich",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5, column=0,padx=10,pady=7,sticky="w")
        f2_txt6=Entry(F2,width=8,textvariable=self.veg_sandwich,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=7)
 
        f2_lbl7=Label(F2,text="Fried Egg",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6, column=0,padx=10,pady=7,sticky="w")
        f2_txt7=Entry(F2,width=8,textvariable=self.fried_egg,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=7)

        f2_lbl8=Label(F2,text="Sel Roti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=7, column=0,padx=10,pady=7,sticky="w")
        f2_txt8=Entry(F2,width=8,textvariable=self.sel_roti, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=7)
    
        f2_lbl9=Label(F2,text="Chatamari",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=8, column=0,padx=10,pady=7,sticky="w")
        f2_txt9=Entry(F2,width=8,textvariable=self.chatamari, font=("times new roman",16,"bold"),bd=5, relief=SUNKEN).grid(row=8,column=1,padx=10,pady=7)
     
        f2_lbl10=Label(F2,text="Dahi Chiura",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=9, column=0,padx=10,pady=7,sticky="w")
        f2_txt10=Entry(F2,width=8,textvariable=self.dahi_chiura, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=7)
        
       
# Frame 3 Refreshments

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Refreshments",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=335, y=90,width=375,height=530)

        # Refreshments Variable types
        self.water1l=IntVar()
        self.orange_juice=IntVar()
        self.coca_cola=IntVar()
        self.ice_cream=IntVar()
        self.red_bull=IntVar()
        self.black_forest=IntVar()
        self.cappuccino=IntVar()
        self.milk_shake=IntVar()
        self.milk_tea=IntVar()
        self.sweet_lassi=IntVar()

        f3_lbl1=Label(F3,text="Water 1L",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10,pady=7,sticky="w")
        f3_txt1=Entry(F3,width=8,textvariable=self.water1l ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7)

        f3_lbl2=Label(F3,text="Orange Juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0,padx=10,pady=7,sticky="w")
        f3_txt2=Entry(F3,width=8,textvariable=self.orange_juice ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=7)

        f3_lbl3=Label(F3,text="Coca-Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0,padx=10,pady=7,sticky="w")
        f3_txt3=Entry(F3,width=8,textvariable=self.coca_cola ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=7)

        f3_lbl4=Label(F3,text="Ice-Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0,padx=10,pady=7,sticky="w")
        f3_txt4=Entry(F3,width=8, textvariable=self.ice_cream ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=7)

        f3_lbl5=Label(F3,text="Red Bull",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4, column=0,padx=10,pady=7,sticky="w")
        f3_txt5=Entry(F3,width=8, textvariable=self.red_bull ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=7)

        f3_lbl6=Label(F3,text="Black Forest",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5, column=0,padx=10,pady=7,sticky="w")
        f3_txt6=Entry(F3,width=8, textvariable=self.black_forest ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=7)
 
        f3_lbl7=Label(F3,text="Cappuccino",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6, column=0,padx=10,pady=7,sticky="w")
        f3_txt7=Entry(F3,width=8, textvariable=self.cappuccino ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=7)

        f3_lbl8=Label(F3,text="Milk Shake",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=7, column=0,padx=10,pady=7,sticky="w")
        f3_txt8=Entry(F3,width=8, textvariable=self.milk_shake ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=7)
    
        f3_lbl9=Label(F3,text="Milk Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=8, column=0,padx=10,pady=7,sticky="w")
        f3_txt9=Entry(F3,width=8, textvariable=self.milk_tea ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=7)
     
        f3_lbl10=Label(F3,text="Sweet Lassi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=9, column=0,padx=10,pady=7,sticky="w")
        f3_txt10=Entry(F3,width=8, textvariable=self.sweet_lassi ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=7)
        
       
# Frame 4 Local Food Items

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Local Food Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=710, y=90,width=325,height=530)

        # Local food items Variable types
        self.dal_bhat=IntVar()
        self.momo=IntVar()
        self.thukpa=IntVar()
        self.choila=IntVar()
        self.sekuwa=IntVar()
        self.sukuti=IntVar()
        self.yomari=IntVar()
        self.dhido=IntVar()
        self.thakali_khana=IntVar()
        self.aalu_tama=IntVar()

        f4_lbl1=Label(F4,text="Dal Bhat",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10,pady=7,sticky="w")
        f4_txt1=Entry(F4,width=8, textvariable=self.dal_bhat, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7)

        f4_lbl2=Label(F4,text="Momo",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0,padx=10,pady=7,sticky="w")
        f4_txt2=Entry(F4,width=8, textvariable=self.momo, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=7)

        f4_lbl3=Label(F4,text="Thukpa",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0,padx=10,pady=7,sticky="w")
        f4_txt3=Entry(F4,width=8, textvariable=self.thukpa, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=7)

        f4_lbl4=Label(F4,text="Choila",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0,padx=10,pady=7,sticky="w")
        f4_txt4=Entry(F4,width=8, textvariable=self.choila ,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=7)

        f4_lbl5=Label(F4,text="Sekuwa",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4, column=0,padx=10,pady=7,sticky="w")
        f4_txt5=Entry(F4,width=8, textvariable=self.sekuwa, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=7)

        f4_lbl6=Label(F4,text="Sukuti",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5, column=0,padx=10,pady=7,sticky="w")
        f4_txt6=Entry(F4,width=8, textvariable=self.sukuti, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=7)
 
        f4_lbl7=Label(F4,text="Yomari",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=6, column=0,padx=10,pady=7,sticky="w")
        f4_txt7=Entry(F4,width=8, textvariable=self.yomari, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=7)

        f4_lbl8=Label(F4,text="Dhido",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=7, column=0,padx=10,pady=7,sticky="w")
        f4_txt8=Entry(F4,width=8, textvariable=self.dhido, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=7)

        f4_lbl9=Label(F4,text="Thakali Khana",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=8, column=0,padx=10,pady=7,sticky="w")
        f4_txt9=Entry(F4,width=8, textvariable=self.thakali_khana, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=7)

        f4_lbl10=Label(F4,text="Aalu Tama",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=9, column=0,padx=10,pady=7,sticky="w")
        f4_txt10=Entry(F4,width=8, textvariable=self.aalu_tama, font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=7)



# Frame 5 Bill Area

        F5=Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1040, y=90, width=350, height=530)
        bill_title = Label(F5, text="Bill Area", font="arial 14 bold", bd=7, relief=GROOVE).pack(fill=X)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5,font=16, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


# Frame6 Bill Menu

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F6.place(x=0, y=620, relwidth=1, height=95)

        self.total_price=StringVar()  #Frame 5 Variable types

        total_price_lbl=Label(F6,text="Total price: ",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0, column=0, padx=5,pady=1,sticky="w")
        total_price_txt=Entry(F6, width=18, textvariable=self.total_price, font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=9,pady=1)

        Label(F6, text="        ",bg=bg_color).grid(row=0, column=2, padx=50, pady=0)  # adding empty space


        Total_btn= Button(F6,text="Total",command=self.total, bg="white",fg="black",width=8,bd=7,font=("arial 14 bold")).grid(row=0, column=3, padx=10, pady=0)
        
        GBill_btn= Button(F6, text="Generate Bill", bg="white",width=10, fg="black",bd=7, font=("arial 14 bold")).grid(row=0, column=4, padx=10, pady=0)

        Clear_btn = Button(F6, text="Clear", bg="white", fg="black",width=8,bd=7,  font=("arial 14 bold")).grid(row=0, column=5, padx=10, pady=0)

        Exit_btn=Button(F6, text="Exit", bg="white", fg="black",width=8,bd=7, font=("arial 14 bold")).grid(row=0, column=6, padx=10, pady=0)

    def total(self):
        self.total_bill=(
                (self.pop_corn.get()*60)+
                (self.noodle.get()*60)+
                (self.muffin.get()*60)+
                (self.samosa.get()*60)+
                (self.burger.get()*60)+
                (self.veg_sandwich.get()*60)+
                (self.fried_egg.get()*60)+
                (self.sel_roti.get()*60)+
                (self.chatamari.get()*60)+
                (self.dahi_chiura.get()*60)+

                (self.water1l.get()*100)+
                (self.orange_juice.get()*100)+
                (self.coca_cola.get()*100)+
                (self.ice_cream.get()*100)+
                (self.red_bull.get()*100)+
                (self.black_forest.get()*100)+
                (self.cappuccino.get()*100)+
                (self.milk_shake.get()*100)+
                (self.milk_tea.get()*100)+
                (self.sweet_lassi.get()*100)+

                (self.dal_bhat.get()*100)+
                (self.momo.get()*100)+
                (self.thukpa.get()*100)+
                (self.choila.get()*100)+
                (self.sekuwa.get()*100)+
                (self.sukuti.get()*100)+
                (self.yomari.get()*100)+
                (self.dhido.get()*100)+
                (self.thakali_khana.get()*100)+
                (self.aalu_tama.get()*100)

        )
        self.total_price.set(str(self.total_bill))

root = Tk()
obj = Canteen_Bill(root)
root.mainloop()