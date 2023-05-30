from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk    # type pip install pillow in cmd 
import random,os
from tkinter import messagebox
import tempfile
from time import strftime       # to display time


# problem: after click on generate bill one value added to cart disappears but we are getting complete bill 


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1510x800+0+0")
        self.root.title("Billing Software")

# ===========variables creation for pro.Name, automatic price, default qty 1 and random No, also to show customer text field but no subcategory and product name=====

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()        # bill no should generate randomly so import random and below bill_no create a var z and give randint method from 1k to 10k
        z=random.randint(1000,9999)     #set this with bill no see below line
        self.bill_no.set(z)
        self.search_bill=StringVar()  
        self.product=StringVar()
        self.prices=IntVar()            # price and qty calculn will give remaining 3 values so string assigned to them
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()



# ---------Product Category List-----BR1-------------------------
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
                
                #-------------------------
        self.SubCatClothing=["Pant","TShirt","Shirt"]

        self.Pant=["Levis","Mufti","Denim"]
        self.price_Levis=5000
        self.price_Mufti=7000
        self.price_Denim=8000

        self.TShirt=["Polo","Roadsters","JackJones"]
        self.price_Polo=3000
        self.price_Roadsters=5000
        self.price_JackJones=6000

        self.Shirt=["PE","LP","PA"]
        self.price_PE=1500
        self.price_LP=1200
        self.price_PA=3520

                #------------------------------------
        self.SubCatLifeStyle=["Bath_Soap","Face_Cream","Hair_Oil"]

        self.Bath_Soap=["LifeBoy","Santoor","Dettol"]
        self.price_LifeBoy=50
        self.price_Santoor=70
        self.price_Dettol=80

        self.Face_Cream=["Garnier","Fair","Ponds"]
        self.price_Garnier=25
        self.price_Fair=22
        self.price_Ponds=30

        self.Hair_Oil=["Vatika","Lotus","Parachute"]
        self.price_Vatika=1500
        self.price_Lotus=1200
        self.price_Parachute=3520
                #--------------------------------------

        self.SubCatMobiles=["Iphone","samsung","oneplus"]

        self.Iphone=["x","Iphone_11","Iphone_12"]
        self.price_x=50000
        self.price_Iphone_11=62000
        self.price_Iphone_12=75000

        self.samsung=["note","dabba","fold"]
        self.price_note=25000
        self.price_dabba=22000
        self.price_fold=300000

        self.oneplus=["never","settle","brand"]
        self.price_never=15000
        self.price_settle=12000
        self.price_brand=35200
                #-----------------------------



#img1
        img=Image.open("images/wb.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

#img2
        img_1=Image.open("images/wb.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

#img3
        img_2=Image.open("images/wb.jpg")
        img_2=img_2.resize((520,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=520,height=130)


# Title of the website
        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("Times New Roman",35,"bold"),bg="black",fg="gold") #bg=white
        lbl_title.place(x=0,y=130,width=1530,height=45) 
   
    # Time code here down
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text = string)
                lbl.after(1000, time)

        lbl=Label(lbl_title, font=("Times New Roman",16,'bold'),background='black',foreground='gold') #bg=white
        lbl.place(x=0,y=0,width=120,height=55)
        time()


# Main Frame is the area behind small boxes change bg to understand
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="black")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

# customer Label frame
        Cust_Frame=LabelFrame(Main_Frame,text="CUSTOMER DETAILS",font=("Times New Roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=320,height=140)

# Customer Name
        self.lblCustname=Label(Cust_Frame,font=("Times New Roman",12,"bold"),bg="white",text="Customer Name:")
        self.lblCustname.grid(row=0,column=0,stick=W,padx=5,pady=2)

        # top variable given here
        self.txtCustname=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("Times New Roman",10,"bold"),width=24)
        self.txtCustname.grid(row=0,column=1)


# Mobile Number
        self.lbl_mob=Label(Cust_Frame,text="Mobile.No:",font=("Times New Roman",12,"bold"),bg="white",bd=4)
        self.lbl_mob.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("Times New Roman",10,"bold"),width=24)
        self.entry_mob.grid(row=1,column=1,stick=W,padx=5,pady=2)


# Product Label frame, change width to incrs or dcrs brd size
        Product_Frame=LabelFrame(Main_Frame,text="PRODUCT DETAILS",font=("Times New Roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=340,y=5,width=640,height=140)

# Category 
# here we r giving value=self.category in ttkcombobox to get values mentioned in s.c
        self.lblCategory=Label(Product_Frame,font=('arial',12,"bold"),bg="white",text="Select Categories:",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,"bold"),width=24,state="readonly")
        #---current 0 for indexing from 0 i.e; on select categories it shows select options 1st then other--------
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        # ---total below line is binding line
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories) 
        


# Sub Category
#in third line value is given empty as we dont know what value to get through subcategory in food name
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,"bold"),bg="white",text="Sub Category:",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=('arial',10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #below line is binding line with Product_add defined fun
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

# Product Name

        self.lblProduct=Label(Product_Frame,font=('arial',12,"bold"),bg="white",text="Product Name:",bd=4)
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',10,"bold"),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        # combo product bind product name and def price
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price) # see by putting prices


# Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,"bold"),bg="white",text="Price:",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        #  values come in price lbl as we give top made variables in price as we creat other var in .combobox. NOTEthis: This step is followed for all top vars defined

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,state="readonly",font=('arial',10,"bold"),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

# Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,"bold"),bg="white",text="Qty:",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

# Middle Frame, area where we put two same photos  ++put dark Image man
        Middle_Frame=Frame(Main_Frame,bd=10)
        Middle_Frame.place(x=10,y=150,width=980,height=340)
#img6
        img_5=Image.open("images/np2.jpg")
        img_5=img_5.resize((490,340),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lbl_img_5=Label(Middle_Frame,image=self.photoimg_5)
        lbl_img_5.place(x=0,y=0,width=490,height=340)

#img7
        img_6=Image.open("images/rolex.jpg")
        img_6=img_6.resize((490,340),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        lbl_img_6=Label(Middle_Frame,image=self.photoimg_6)
        lbl_img_6.place(x=500,y=0,width=460,height=340)


        
#Bill Search above Bill area   === SEARCH ====
        Search_Frame=Frame(Main_Frame,bd=2,bg="black")
        Search_Frame.place(x=1020,y=10,width=500,height=40)

        # search label for searching Bill 

        self.lblBill=Label(Search_Frame,font=('arial',10,"bold"),fg="black",bg="gold",text="Bill Number:")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        #Entry field

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        #Button for search

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)




# Bill area Frame at right side
        RightLabelFrame=LabelFrame(Main_Frame,text="BILL AREA",font=("Times New Roman",12,"bold"),bg="gold",fg="black") #bg=white #fg=red --------=====
        RightLabelFrame.place(x=990,y=45,width=520,height=440)

# Scroll bar
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="black",fg="gold",font=("Times New Roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

# bill counter      #copied Product Label frame changed as BILL COUNTER LABEL FRAME 
        Bottom_Frame=LabelFrame(Main_Frame,text="BILL COUNTER",font=("Times New Roman",12,"bold"),bg="black",fg="gold")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125) 


#---------------------------------------------------------------------------------------------------------------------------
# commented bcoz code is not working for me so i blocked it from display

# Qty code copied and cgd as SubTotal label. code is below 4 lines
        #self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,"bold"),bg="white",text="Sub Total:",bd=4)
        #self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        #self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,"bold"),width=26)
        #self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

# Tax Label in Bottom Label . code is below 4 lines
       #self.lbl_Tax=Label(Bottom_Frame,font=('arial',12,"bold"),bg="white",text="Gov Tax:",bd=4)
       #self.lbl_Tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

       #self.txt_Tax=ttk.Entry(Bottom_Frame,font=('arial',10,"bold"),width=24)
       #self.txt_Tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

# Total Amount Label in Bottom Label.  code is below 4 lines
        #self.lblTotalAmount=Label(Bottom_Frame,font=('arial',12,"bold"),bg="white",text="Total:",bd=4)
        #self.lblTotalAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        #self.txtTotalAmount=ttk.Entry(Bottom_Frame,font=('arial',10,"bold"),width=24)
        #self.txtTotalAmount.grid(row=2,column=1,sticky=W,padx=5,pady=2)
#-----------------------------------------------------------------------------------------------------------------------------
#Button Frame

        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="gold")
        Btn_Frame.place(x=170,y=0) # x was initially given 320 
#Buttons
        #1
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="black",fg="gold",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        #2
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="black",fg="gold",width=15,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1)

        #3
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="black",fg="gold",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        #4
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="black",fg="gold",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        #5
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="black",fg="gold",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        #6 here given command will clear everything
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="black",fg="gold",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
# ----- Calling welcome code -----
        self.l=[]       # this is var to count total in list, link with AddItem 

# Now declaring a new fun soo that selected qty product everything comes automatically in bill area, simply call it as FUNCTION DECLARATION and #we call this in Button Frame i.e; at BtnAddToCart by command=self.AddItem


# ============= below DEFAULT WELCOME code  related with  Text Area code line present in BILL AREA section ====================

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tTRK   INTERNATIONAL   MALLS ")
        self.textarea.insert(END,f" \n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f" \n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f" \n Phone Number:{self.c_phon.get()}")

        self.textarea.insert(END,"\n=======================================================")
        self.textarea.insert(END,f" \n PRODUCTS\t\tQTY\t\tPRICE")
        self.textarea.insert(END,"\n=======================================================\n")

# ************************************* welcome ends ***************************************************

# after selecting item when we press AddToCart then due to below code items added to bill area

    def AddItem (self):      # to add create var to do mul of price and qty
        Tax=1   # space b/w x and = created error for me
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n    # we got mul in m now to get total see below line
        self.l.append(self.m)
        if self.product.get()=="":      # condition for product, if nothing selected shows error msg with top line from tkinter import messagebox displays this sentence
            messagebox.showerror("Error","Please Select the Product Name")    
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")    # below are Formulae
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

# after selecting item when we press GenerateBill then due to below code bill is generated and call this by command=self.gen_bill at generate_bill btn
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please add product to cart to generate Bill")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ======================================================")

            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}") # from else of AddItem s_t, ,t_i, t
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
         
            self.textarea.insert(END,"\n ======================================================")




# save bill
    def save_bill(self):
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
            if op>0:
                self.bill_data=self.textarea.get(1.0,END)
                f1=open('bills/'+str(self.bill_no.get())+".txt","w")
                f1.write(self.bill_data)
                op=messagebox.showinfo("saved",f"Bill No:{self.bill_no.get()} Bill Successfully saved")
                f1.close()


#print bill
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename= tempfile.mktemp('.txt')       # TO print bill as txt file
        open(filename,'w').write(q)
        os.startfile(filename,"print")  # command at print btn


# we search for bill that we want with this code and command to call code  given at search btn i.e., command=self.find_bill 
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                        self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No")
            
# clear    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()          # wlcm page should come automatically afetr clearing cmd at clr btn


# ---defing a function for categories like clothing lifestyle and so on
#bind below def with this #Category present at up 8th line def position same as this def

# In Category this is binded---- RLN 2
    def Categories(self,event=""):
            if self.Combo_Category.get()=="Clothing":
                self.ComboSubCategory.config(value=self.SubCatClothing)
                self.ComboSubCategory.current(0)
        
            if self.Combo_Category.get()=="LifeStyle":
                self.ComboSubCategory.config(value=self.SubCatLifeStyle)
                self.ComboSubCategory.current(0)

            if self.Combo_Category.get()=="Mobiles":
                self.ComboSubCategory.config(value=self.SubCatMobiles)
                self.ComboSubCategory.current(0)

#----Product add binded with SubCategory---RLN 3---
    def Product_add(self,event=""):
            if self.ComboSubCategory.get()=="Pant":
                self.ComboProduct.config(value=self.Pant)
                self.ComboProduct.current(0)   

            if self.ComboSubCategory.get()=="TShirt":
                self.ComboProduct.config(value=self.TShirt)
                self.ComboProduct.current(0)  

            if self.ComboSubCategory.get()=="Shirt":
                self.ComboProduct.config(value=self.Shirt)
                self.ComboProduct.current(0)  

                #LifeStyle
            if self.ComboSubCategory.get()=="Bath_Soap":
                self.ComboProduct.config(value=self.Bath_Soap)
                self.ComboProduct.current(0)   

            if self.ComboSubCategory.get()=="Face_Cream":
                self.ComboProduct.config(value=self.Face_Cream)
                self.ComboProduct.current(0)  

            if self.ComboSubCategory.get()=="Hair_Oil":
                self.ComboProduct.config(value=self.Hair_Oil)
                self.ComboProduct.current(0)  

                #Mobile
            if self.ComboSubCategory.get()=="Iphone":
                self.ComboProduct.config(value=self.Iphone)
                self.ComboProduct.current(0)   

            if self.ComboSubCategory.get()=="samsung":
                self.ComboProduct.config(value=self.samsung)
                self.ComboProduct.current(0)  

            if self.ComboSubCategory.get()=="oneplus":
                self.ComboProduct.config(value=self.oneplus)
                self.ComboProduct.current(0)  
                
# ===================== Automatic Price and Qty funs below  ===============================================

    def price(self,event=""):

#Clothing

        #Pant 
        if self.ComboProduct.get()=="Levis":    # set this with comboproduct in product name label
            self.ComboPrice.config(value=self.price_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mufti":    # set this with comboproduct in product name label
            self.ComboPrice.config(value=self.price_Mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Denim":    # set this with comboproduct in product name label
            self.ComboPrice.config(value=self.price_Denim)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # TShirt

        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_Polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadsters":
            self.ComboPrice.config(value=self.price_Roadsters)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="JackJones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirt

        if self.ComboProduct.get()=="PE":
            self.ComboPrice.config(value=self.price_PE)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="LP":
            self.ComboPrice.config(value=self.price_LP)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="PA":
            self.ComboPrice.config(value=self.price_PA)
            self.ComboPrice.current(0)
            self.qty.set(1)

#LifeStyle

        #Bath_Soap

        if self.ComboProduct.get()=="LifeBoy":
            self.ComboPrice.config(value=self.price_LifeBoy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dettol":
            self.ComboPrice.config(value=self.price_Dettol)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Face_Cream

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_Garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Fair":
            self.ComboPrice.config(value=self.price_Fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_Ponds)
            self.ComboPrice.current(0)
            self.qty.set(1) 
              
        #Hair_Oil

        if self.ComboProduct.get()=="Vatika":
            self.ComboPrice.config(value=self.price_Vatika)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lotus":
            self.ComboPrice.config(value=self.price_Lotus)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_Parachute)
            self.ComboPrice.current(0)
            self.qty.set(1)



# Mobiles

        #Iphone

        if self.ComboProduct.get()=="x":
            self.ComboPrice.config(value=self.price_x)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_Iphone_11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_Iphone_12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #samsung

        if self.ComboProduct.get()=="note":
            self.ComboPrice.config(value=self.price_note)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="dabba":
            self.ComboPrice.config(value=self.price_dabba)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="fold":
            self.ComboPrice.config(value=self.price_fold)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #oneplus

        if self.ComboProduct.get()=="never":
            self.ComboPrice.config(value=self.price_never)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="settle":
            self.ComboPrice.config(value=self.price_settle)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="brand":
            self.ComboPrice.config(value=self.price_brand)
            self.ComboPrice.current(0)
            self.qty.set(1)


if __name__ == '__main__' :
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()






