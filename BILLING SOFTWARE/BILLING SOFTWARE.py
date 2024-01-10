from tkinter import *
import random as ra
from tkinter import messagebox as mb
import os
from plyer import notification
import tempfile
import datetime
import time

class Billing_Software:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1919x1079+0+0")
        self.root.title("BILLING SOFTWARE - BY ABHIRUP RUDRA")
        bg_colour = "#16fad8"
        fg_colour = "#fa23ab"
        title = Label(self.root, text = "BILLING SOFTWARE", bd = 12, relief = "groove", bg = bg_colour, fg = "Black", font = ("times new roman", 30, "bold"), pady = 2).pack(fill = X)

        #--------------------------VARIABLES--------------------------#

        self.check_print_bill = 0
        #cosmetics
        self.cosmetics = []
        for i in range(0,18):
            self.cosmetics.append(IntVar())

        self.cosmetics_name = ['SOAP        ', 'LIPSTICK    ', 'PERFUME     ', 'POWDER      ', 'FACIAL KIT  ', 'HAIR COLOUR ', 'EYE LINER   ', 'NAIL PAINT  ', 'BODY LOTION ', 'CREAM       ', 'MOISTURISER ', 'BRUSH       ', 'TONER       ', 'KAJAL       ', 'HIGH LIGHTER', 'BLUSHER     ', 'SINDUR      ', 'BINDI       ']

        self.cosmetics_price = [85, 550, 300, 500, 650, 500, 200, 150, 425, 300, 400, 100, 150, 180, 200, 300, 150, 50]

        #grocery
        self.grocerys = []
        for i in range(0,18):
            self.grocerys.append(IntVar())

        self.grocerys_name = ['MUSTARD OIL ', 'SOYABEAN OIL', 'GOTA MUG    ', 'SORSE       ', 'JEERA       ', 'JEERA GURO  ', 'NUSUR DAL   ', 'MUG DAL     ', 'SALT        ', 'SUGAR       ', 'KALAIR DAL  ', 'MAIDA       ', 'ATTA        ', 'HALDI GURO  ', 'BLACK PEPPER', 'TEA         ', 'COFFEE      ', 'RICE        ']

        self.grocerys_price = [130, 113, 71, 20, 94, 30, 76, 79, 30, 38, 45, 41, 55, 167, 46, 195, 140, 410]
        
        #statinery
        self.stationarys = []
        for i in range(0,18):
            self.stationarys.append(IntVar())

        self.stationarys_name = ['ERASER      ', 'PAPER       ', 'STICKY NOTES', 'CALCULATOR  ', 'MARKER      ', 'ENVELOP     ', 'SCISSOR     ', 'STAPLER     ', 'CLIP        ', 'RULER       ', 'DOT PEN     ', 'COPY        ', 'BALL PEN    ', 'CELLO TAPE  ', 'BROWN TAPE  ', 'DST         ', 'PENCIL      ', 'GEL PEN     ']

        self.stationarys_price = [5, 35, 50, 1295, 40, 60, 100, 150, 70, 26, 15, 65, 5, 80, 100, 150, 100, 50]

        #buttons
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.stationary_price = StringVar()
        self.total_price = StringVar()
        self.discount_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.stationary_tax = StringVar()
        self.total_tax = StringVar()
        self.payable_price = StringVar()

        #customer details
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill = StringVar()
        self.c_bill.set(str(ra.randint(100000, 999999)))
        self.search_bill = StringVar()

        #--------------------------CUSTOMER DETAILS FRAME--------------------------#
        
        F1 = LabelFrame(self.root, text = "CUSTOMER DETAILS", font = ("times new roman", 15, "bold"),bd = 12, relief = "groove", fg = fg_colour, bg = bg_colour)
        F1.place(x = 0, y = 80, relwidth = 1)

        cname_label = Label(F1, text = "Customer Name", bg = bg_colour, font = ("times new roman", 17, "bold")).grid(row = 0, column = 0, padx = 20, pady = 5)
        cname_text = Entry(F1, width = 20, textvariable = self.c_name, font = ("arial", 15), bd = 7, relief = "sunken").grid(row = 0, column = 1, padx = 10, pady = 5)

        cphone_label = Label(F1, text = "Phone Number", bg = bg_colour, font = ("times new roman", 17, "bold")).grid(row = 0, column = 2, padx = 20, pady = 5)
        cphone_text = Entry(F1, width = 20, textvariable = self.c_phone, font = ("arial", 15), bd = 7, relief = "sunken").grid(row = 0, column = 3, padx = 10, pady = 5)

        cbill_label = Label(F1, text = "Bill Number", bg = bg_colour, font = ("times new roman", 17, "bold")).grid(row = 0, column = 4, padx = 20, pady = 5)
        cbill_text = Entry(F1, width = 20, textvariable = self.search_bill, font = ("arial", 15), bd = 7, relief = "sunken").grid(row = 0, column = 5, padx = 10, pady = 5)

        cbill_button = Button(F1, text = "SEARCH", command = self.find_bill, width = 10, bd = 7, relief = "groove", font = ("arial", 12, "bold"), cursor = "hand2").grid(row = 0, column = 6, padx = 20, pady = 5)

        #--------------------------COSMETICS FRAME--------------------------#

        F2 = LabelFrame(self.root, text = "COSMETICS", font = ("times new roman", 15, "bold"),bd = 12, relief = "groove", fg = fg_colour, bg = bg_colour)
        F2.place(x = 0, y = 177, width = 360, height = 400)

        soap_label = Label(F2, text = "Soap", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        soap_text = Entry(F2, width = 5, textvariable = self.cosmetics[0], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 0, column = 1, padx = 3, pady = 5)

        lip_label = Label(F2, text = "Lipstick", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "w")
        lip_text = Entry(F2, width = 5, textvariable = self.cosmetics[1], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 0, column = 3, padx = 3, pady = 5)

        perfume_label = Label(F2, text = "Perfume", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        perfume_text = Entry(F2, width = 5, textvariable = self.cosmetics[2], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 1, column = 1, padx = 3, pady = 5)

        powder_label = Label(F2, text = "Powder", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "w")
        powder_text = Entry(F2, width = 5, textvariable = self.cosmetics[3], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 1, column = 3, padx = 3, pady = 5)

        facial_label = Label(F2, text = "Facial Kit", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        facial_text = Entry(F2, width = 5, textvariable = self.cosmetics[4], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 2, column = 1, padx = 3, pady = 5)

        hair_label = Label(F2, text = "Hair Colour", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
        hair_text = Entry(F2, width = 5, textvariable = self.cosmetics[5], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 2, column = 3, padx = 3, pady = 5)

        eye_label = Label(F2, text = "Eye Liner", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        eye_text = Entry(F2, width = 5, textvariable = self.cosmetics[6], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 3, column = 1, padx = 3, pady = 5)

        nail_label = Label(F2, text = "Nail Polish", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "w")
        nail_text = Entry(F2, width = 5, textvariable = self.cosmetics[7], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 3, column = 3, padx = 3, pady = 5)

        body_label = Label(F2, text = "Body Lotion", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        body_text = Entry(F2, width = 5, textvariable = self.cosmetics[8], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 4, column = 1, padx = 3, pady = 5)

        cream_label = Label(F2, text = "Cream", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "w")
        cream_text = Entry(F2, width = 5, textvariable = self.cosmetics[9], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 4, column = 3, padx = 3, pady = 5)

        moist_label = Label(F2, text = "Moisterizure", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "w")
        moist_text = Entry(F2, width = 5, textvariable = self.cosmetics[10], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 5, column = 1, padx = 5, pady = 5)

        brush_label = Label(F2, text = "Brush", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 5, column = 2, padx = 15, pady = 5, sticky = "w")
        brush_text = Entry(F2, width = 5, textvariable = self.cosmetics[11], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 5, column = 3, padx = 5, pady = 5)

        toner_label = Label(F2, text = "Toner", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "w")
        toner_text = Entry(F2, width = 5, textvariable = self.cosmetics[12], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 6, column = 1, padx = 5, pady = 5)

        kajal_label = Label(F2, text = "Kajal", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 6, column = 2, padx = 15, pady = 5, sticky = "w")
        kajal_text = Entry(F2, width = 5, textvariable = self.cosmetics[13], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 6, column = 3, padx = 5, pady = 5)

        lighter_label = Label(F2, text = "Highlighter", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "w")
        lighter_text = Entry(F2, width = 5, textvariable = self.cosmetics[14], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 7, column = 1, padx = 5, pady = 5)

        blusher_label = Label(F2, text = "Blusher", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 7, column = 2, padx = 15, pady = 5, sticky = "w")
        blusher_text = Entry(F2, width = 5, textvariable = self.cosmetics[15], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 7, column = 3, padx = 5, pady = 5)

        sindur_label = Label(F2, text = "Sindur", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "w")
        sindur_text = Entry(F2, width = 5, textvariable = self.cosmetics[16], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 8, column = 1, padx = 5, pady = 5)

        bindi_label = Label(F2, text = "Bindi", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 8, column = 2, padx = 15, pady = 5, sticky = "w")
        bindi_text = Entry(F2, width = 5, textvariable = self.cosmetics[17], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 8, column = 3, padx = 5, pady = 5)

        #--------------------------GROCERY FRAME--------------------------#

        F3 = LabelFrame(self.root, text = "GROCERY", font = ("times new roman", 15, "bold"),bd = 12, relief = "groove", fg = fg_colour, bg = bg_colour)
        F3.place(x = 368, y = 177, width = 395, height = 400)

        mustard_label = Label(F3, text = "Mustard Oil", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        mustard_text = Entry(F3, width = 5, textvariable = self.grocerys[0], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 0, column = 1, padx = 3, pady = 5)

        soyabean_label = Label(F3, text = "Soyabean Oil", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "w")
        soyabean_text = Entry(F3, width = 5, textvariable = self.grocerys[1], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 0, column = 3, padx = 3, pady = 5)

        gmug_label = Label(F3, text = "Gota Mug", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        gmug_text = Entry(F3, width = 5, textvariable = self.grocerys[2], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 1, column = 1, padx = 3, pady = 5)

        sorse_label = Label(F3, text = "Gota Sorse", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "w")
        sorse_text = Entry(F3, width = 5, textvariable = self.grocerys[3], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 1, column = 3, padx = 3, pady = 5)

        jeera_label = Label(F3, text = "Jeera", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        jeera_text = Entry(F3, width = 5, textvariable = self.grocerys[4], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 2, column = 1, padx = 3, pady = 5)

        gjeera_label = Label(F3, text = "Jeera Powder", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
        gjeera_text = Entry(F3, width = 5, textvariable = self.grocerys[5], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 2, column = 3, padx = 3, pady = 5)

        musur_label = Label(F3, text = "Musur Dal", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        musur_text = Entry(F3, width = 5, textvariable = self.grocerys[6], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 3, column = 1, padx = 3, pady = 5)

        mug_label = Label(F3, text = "Mug Dal", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "w")
        mug_text = Entry(F3, width = 5, textvariable = self.grocerys[7], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 3, column = 3, padx = 3, pady = 5)

        salt_label = Label(F3, text = "Salt", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        salt_text = Entry(F3, width = 5, textvariable = self.grocerys[8], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 4, column = 1, padx = 3, pady = 5)

        sugar_label = Label(F3, text = "Sugar", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "w")
        sugar_text = Entry(F3, width = 5, textvariable = self.grocerys[9], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 4, column = 3, padx = 3, pady = 5)

        kalai_label = Label(F3, text = "Kalair Dal", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "w")
        kalai_text = Entry(F3, width = 5, textvariable = self.grocerys[10], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 5, column = 1, padx = 5, pady = 5)

        maida_label = Label(F3, text = "Maida", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 5, column = 2, padx = 15, pady = 5, sticky = "w")
        maida_text = Entry(F3, width = 5, textvariable = self.grocerys[11], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 5, column = 3, padx = 5, pady = 5)

        atta_label = Label(F3, text = "Atta", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "w")
        atta_text = Entry(F3, width = 5, textvariable = self.grocerys[12], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 6, column = 1, padx = 5, pady = 5)

        haldi_label = Label(F3, text = "Haldi Powder", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 6, column = 2, padx = 15, pady = 5, sticky = "w")
        haldi_text = Entry(F3, width = 5, textvariable = self.grocerys[13], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 6, column = 3, padx = 5, pady = 5)

        black_label = Label(F3, text = "Black Pepper", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "w")
        black_text = Entry(F3, width = 5, textvariable = self.grocerys[14], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 7, column = 1, padx = 5, pady = 5)

        tea_label = Label(F3, text = "Tea", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 7, column = 2, padx = 15, pady = 5, sticky = "w")
        tea_text = Entry(F3, width = 5, textvariable = self.grocerys[15], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 7, column = 3, padx = 5, pady = 5)

        coffee_label = Label(F3, text = "Coffee", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "w")
        coffee_text = Entry(F3, width = 5, textvariable = self.grocerys[16], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 8, column = 1, padx = 5, pady = 5)

        rice_label = Label(F3, text = "Rice", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 8, column = 2, padx = 15, pady = 5, sticky = "w")
        rice_text = Entry(F3, width = 5, textvariable = self.grocerys[17], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 8, column = 3, padx = 5, pady = 5)

        #--------------------------Stationery FRAME--------------------------#

        F4 = LabelFrame(self.root, text = "STATIONERY", font = ("times new roman", 15, "bold"),bd = 12, relief = "groove", fg = fg_colour, bg = bg_colour)
        F4.place(x = 770, y = 177, width = 365, height = 400)

        eraser_label = Label(F4, text = "Eraser", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        eraser_text = Entry(F4, width = 5, textvariable = self.stationarys[0], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 0, column = 1, padx = 3, pady = 5)

        paper_label = Label(F4, text = "Paper", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "w")
        paper_text = Entry(F4, width = 5, textvariable = self.stationarys[1], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 0, column = 3, padx = 3, pady = 5)

        snotes_label = Label(F4, text = "Sticky Notes", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        snotes_text = Entry(F4, width = 5, textvariable = self.stationarys[2], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 1, column = 1, padx = 3, pady = 5)

        calc_label = Label(F4, text = "Calculator", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "w")
        calc_text = Entry(F4, width = 5, textvariable = self.stationarys[3], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 1, column = 3, padx = 3, pady = 5)

        marker_label = Label(F4, text = "Marker", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        marker_text = Entry(F4, width = 5, textvariable = self.stationarys[4], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 2, column = 1, padx = 3, pady = 5)

        envelop_label = Label(F4, text = "Envelop", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "w")
        envelop_text = Entry(F4, width = 5, textvariable = self.stationarys[5], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 2, column = 3, padx = 3, pady = 5)

        scissor_label = Label(F4, text = "Scissor", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        scissor_text = Entry(F4, width = 5, textvariable = self.stationarys[6], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 3, column = 1, padx = 3, pady = 5)

        stapler_label = Label(F4, text = "Stapler", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "w")
        stapler_text = Entry(F4, width = 5, textvariable = self.stationarys[7], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 3, column = 3, padx = 3, pady = 5)

        clip_label = Label(F4, text = "Paperclip", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        clip_text = Entry(F4, width = 5, textvariable = self.stationarys[8], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 4, column = 1, padx = 3, pady = 5)

        ruler_label = Label(F4, text = "Ruler", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "w")
        ruler_text = Entry(F4, width = 5, textvariable = self.stationarys[9], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 4, column = 3, padx = 3, pady = 5)

        dpen_label = Label(F4, text = "Dot Pen", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "w")
        dpen_text = Entry(F4, width = 5, textvariable = self.stationarys[10], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 5, column = 1, padx = 5, pady = 5)

        copy_label = Label(F4, text = "Copy", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 5, column = 2, padx = 15, pady = 5, sticky = "w")
        copy_text = Entry(F4, width = 5, textvariable = self.stationarys[11], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 5, column = 3, padx = 5, pady = 5)

        ball_label = Label(F4, text = "Ball Pen", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 6, column = 0, padx = 5, pady = 5, sticky = "w")
        ball_text = Entry(F4, width = 5, textvariable = self.stationarys[12], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 6, column = 1, padx = 5, pady = 5)

        ctape_label = Label(F4, text = "Cellotape", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 6, column = 2, padx = 15, pady = 5, sticky = "w")
        ctape_text = Entry(F4, width = 5, textvariable = self.stationarys[13], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 6, column = 3, padx = 5, pady = 5)

        btape_label = Label(F4, text = "Brown Tape", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 7, column = 0, padx = 5, pady = 5, sticky = "w")
        btape_text = Entry(F4, width = 5, textvariable = self.stationarys[14], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 7, column = 1, padx = 5, pady = 5)

        dst_label = Label(F4, text = "DST", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 7, column = 2, padx = 15, pady = 5, sticky = "w")
        dst_text = Entry(F4, width = 5, textvariable = self.stationarys[15], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 7, column = 3, padx = 5, pady = 5)

        pencil_label = Label(F4, text = "Pencil", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 8, column = 0, padx = 5, pady = 5, sticky = "w")
        pencil_text = Entry(F4, width = 5, textvariable = self.stationarys[16], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 8, column = 1, padx = 5, pady = 5)

        gpen_label = Label(F4, text = "Gel Pen", font = ("times new roman", 12, "bold"), bg = bg_colour, fg = "black").grid(row = 8, column = 2, padx = 15, pady = 5, sticky = "w")
        gpen_text = Entry(F4, width = 5, textvariable = self.stationarys[17], font = ("arial", 12), bd = 5, relief = "sunken").grid(row = 8, column = 3, padx = 5, pady = 5)
        
        #--------------------------Billing FRAME--------------------------#

        F5 = Frame(self.root,bd = 12, relief = "groove")
        F5.place(x = 1142, y = 177, width = 387, height = 400)

        bill_title = Label(F5, text = "BILL AREA", font = ("times new roman", 15, "bold"), bd = 12, relief = "groove").pack(fill = X)

        scroll_y = Scrollbar(F5, orient = VERTICAL)
        self.textarea = Text(F5, yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_y.config(command = self.textarea.yview)
        self.textarea.pack(fill = BOTH, expand = 1)
        self.welcome_bill()

        #--------------------------Button FRAME--------------------------#

        F6 = LabelFrame(self.root, text = "BILL MENU", font = ("times new roman", 15, "bold"),bd = 12, relief = "groove", fg = fg_colour, bg = bg_colour)
        F6.place(x = 0, y = 584, relwidth = 1, height = 208)

        m1_label = Label(F6, text = "Total Cosmetics Amount", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 0, padx = 5, pady = 2, sticky = "w")
        m1_text = Entry(F6, width = 18, textvariable = self.cosmetic_price, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 0, column = 1, padx = 5, pady = 2)

        m2_label = Label(F6, text = "Total Grocery Amount", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 0, padx = 10, pady = 2, sticky = "w")
        m2_text = Entry(F6, width = 18, textvariable = self.grocery_price, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 1, column = 1, padx = 10, pady = 2)

        m3_label = Label(F6, text = "Total Stationery Amount", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 0, padx = 10, pady = 2, sticky = "w")
        m3_text = Entry(F6, width = 18, textvariable = self.stationary_price, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 2, column = 1, padx = 10, pady = 2)

        m4_label = Label(F6, text = "Total Amount", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 0, padx = 10, pady = 2, sticky = "w")
        m4_text = Entry(F6, width = 18, textvariable = self.total_price, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 3, column = 1, padx = 10, pady = 2)

        m5_label = Label(F6, text = "Discount Percentage", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 0, padx = 10, pady = 2, sticky = "w")
        m5_text = Entry(F6, width = 18, textvariable = self.discount_price, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 4, column = 1, padx = 10, pady = 2)

        g1_label = Label(F6, text = "Cosmetics Tax", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 0, column = 2, padx = 10, pady = 2, sticky = "w")
        g1_text = Entry(F6, width = 18, textvariable = self.cosmetic_tax, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 0, column = 3, padx = 10, pady = 2)

        g2_label = Label(F6, text = "Grocery Tax", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 1, column = 2, padx = 10, pady = 2, sticky = "w")
        g2_text = Entry(F6, width = 18, textvariable = self.grocery_tax, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 1, column = 3, padx = 10, pady = 2)

        g3_label = Label(F6, text = "Stationery Tax", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 2, column = 2, padx = 10, pady = 2, sticky = "w")
        g3_text = Entry(F6, width = 18, textvariable = self.stationary_tax, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 2, column = 3, padx = 10, pady = 2)

        g4_label = Label(F6, text = "Total Tax", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 3, column = 2, padx = 10, pady = 2, sticky = "w")
        g4_text = Entry(F6, width = 18, textvariable = self.total_tax, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 3, column = 3, padx = 10, pady =2)

        g5_label = Label(F6, text = "Payable Amount", font = ("times new roman", 14, "bold"), bg = bg_colour, fg = "black").grid(row = 4, column = 2, padx = 10, pady = 2, sticky = "w")
        g5_text = Entry(F6, width = 18, textvariable = self.payable_price, font = ("arial", 10, "bold"), bd = 5, relief = "sunken").grid(row = 4, column = 3, padx = 10, pady = 2)

        self.cosmetic_price.set("Rs 0.0")
        self.grocery_price.set("Rs 0.0")
        self.stationary_price.set("Rs 0.0")
        self.total_price.set("Rs 0.0")
        self.discount_price.set("0.0%")
        self.cosmetic_tax.set("Rs 0.0")
        self.grocery_tax.set("Rs 0.0")
        self.stationary_tax.set("Rs 0.0")
        self.total_tax.set("Rs 0.0")
        self.payable_price.set("Rs 0.0")

        Fb = Frame(F6, bd = 12, relief = "groove", bg = "white")
        Fb.place(x = 750, width = 720, height = 162)

        tot_btn = Button(Fb, text = "TOTAL", command = self.total, width = 10, height = 5, font = ("arial", 10, "bold"), fg = "black", bg = bg_colour, bd = 5, relief = "groove", cursor = "hand2").grid(row = 0, column = 0, padx = 21, pady = 21)
        gbill_btn = Button(Fb, text = "GENERATE", command = self.bill_area, width = 10, height = 5, font = ("arial", 10, "bold"), fg = "black", bg = bg_colour, bd = 5, relief = "groove", cursor = "hand2").grid(row = 0, column = 1, padx = 21, pady = 21)
        print_btn = Button(Fb, text = "PRINT", command = self.print, width = 10, height = 5, font = ("arial", 10, "bold"), fg = "black", bg = bg_colour, bd = 5, relief = "groove", cursor = "hand2").grid(row = 0, column = 2, padx = 21, pady = 21)
        clear_btn = Button(Fb, text = "CLEAR", command = self.clear_all, width = 10, height = 5, font = ("arial", 10, "bold"), fg = "black", bg = bg_colour, bd = 5, relief = "groove", cursor = "hand2").grid(row = 0, column = 3, padx = 21, pady = 21)
        exit_btn = Button(Fb, text = "EXIT", command = self.exit, width = 10, height = 5, font = ("arial", 10, "bold"), fg = "black", bg = bg_colour, bd = 5, relief = "groove", cursor = "hand2").grid(row = 0, column = 4, padx = 21, pady = 21)

    #--------------------------FUNCTIONS--------------------------#

    def total(self):

        self.cosmetic = 0
        for i in range(0,18):
            self.cosmetic += self.cosmetics[i].get()*self.cosmetics_price[i]

        self.cosmetic_price.set("Rs " + str(float(self.cosmetic)))

        self.grocery = 0
        for i in range(0,18):
            self.grocery += self.grocerys[i].get()*self.grocerys_price[i]

        self.grocery_price.set("Rs " + str(float(self.grocery)))

        self.stationary = 0
        for i in range(0,18):
            self.stationary += self.stationarys[i].get()*self.stationarys_price[i]

        self.stationary_price.set("Rs " + str(float(self.stationary)))
        
        self.total = (
            self.cosmetic + self.grocery + self.stationary
        )
        self.total_price.set("Rs " + str(float(self.total)))

        self.discount = 0
        if self.total == 0:
            self.discount = 0
        elif self.total <= 500:
            self.discount = 2
        elif self.total <= 1000:
            self.discount = 5
        elif self.total <= 10000:
            self.discount = 10
        elif self.total <= 30000:
            self.discount = 15
        elif self.total <= 50000:
            self.discount = 20
        else:
            self.discount = 25

        self.discount_price.set(str(float(self.discount)) + "%")

        self.tcosmetic = self.cosmetic * 0.10
        self.cosmetic_tax.set("Rs " + str(float(self.tcosmetic)))

        self.tgrocery = self.grocery * 0.07
        self.grocery_tax.set("Rs " + str(float(self.tgrocery)))

        self.tstatinery = self.stationary * 0.02
        self.stationary_tax.set("Rs " + str(float(self.tstatinery)))

        self.ttotal = (
            self.tcosmetic + self.tgrocery + self.tstatinery
        )
        self.total_tax.set("Rs " + str(float(self.ttotal)))

        self.pay = self.total - (self.total * (self.discount / 100)) - self.ttotal
        self.payable_price.set("Rs " + str(float(self.pay)))

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        ts = time.time()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S %p", t)
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')

        self.textarea.insert(END, "             WELCOME MORE RETAIL")
        self.textarea.insert(END, f"\nDATE : {date}       TIME : {current_time}")
        self.textarea.insert(END, f"\nBILL NO. : {self.c_bill.get()}")
        self.textarea.insert(END, f"\nNAME : {self.c_name.get()}            ")
        self.textarea.insert(END, f"\nPHONE NO. : {self.c_phone.get()}")
        self.textarea.insert(END, "\n==========================================")
        self.textarea.insert(END, "\nPRODUCTS                  QTY      PRICE")
        self.textarea.insert(END, "\n==========================================")

    def bill_area(self):
        if self.c_name.get().strip() == "" or self.c_phone.get().strip() == "" :
            mb.showerror("ERROR", "Customer Details are must")
        else:
            self.welcome_bill()

            #COSMETICS
            for i in range(0,18):
                if self.cosmetics[i].get() != 0:
                    self.textarea.insert(END, f"\n{self.cosmetics_name[i]}             {self.cosmetics[i].get()}     Rs {self.cosmetics[i].get()*self.cosmetics_price[i]}")

            #GROCERY
            for i in range(0,18):
                if self.grocerys[i].get() != 0:
                    self.textarea.insert(END, f"\n{self.grocerys_name[i]}             {self.grocerys[i].get()}     Rs {self.grocerys[i].get()*self.grocerys_price[i]}")

            #STATIONERY
            for i in range(0,18):
                if self.stationarys[i].get() != 0:
                    self.textarea.insert(END, f"\n{self.stationarys_name[i]}             {self.stationarys[i].get()}     Rs {self.stationarys[i].get()*self.stationarys_price[i]}")

            #OTHERS
            self.textarea.insert(END, "\n==========================================")
            self.textarea.insert(END, f"\nTOTAL COSMETIC PRICE    {self.cosmetic_price.get()[:self.cosmetic_price.get().index('.')+3]}")
            self.textarea.insert(END, f"\nTOTAL GROCERY PRICE     {self.grocery_price.get()[:self.grocery_price.get().index('.')+3]}")
            self.textarea.insert(END, f"\nTOTAL STATIONERY PRICE  {self.stationary_price.get()[:self.stationary_price.get().index('.')+3]}")
            self.textarea.insert(END, f"\nTOTAL PRICE             {self.total_price.get()[:self.total_price.get().index('.')+3]}")
            self.textarea.insert(END, f"\nTOTAL COSMETIC TAX      {self.cosmetic_tax.get()[:self.cosmetic_tax.get().index('.')+3]}")
            self.textarea.insert(END, f"\nTOTAL GORCERY TAX       {self.grocery_tax.get()[:self.grocery_tax.get().index('.')+3]}")
            self.textarea.insert(END, f"\nTOTAL STATIONERY TAX    {self.stationary_tax.get()[:self.stationary_tax.get().index('.')+3]}")
            self.textarea.insert(END, f"\nDISCOUNT PERCENT        {self.discount_price.get()[:self.discount_price.get().index('.')+3]}")
            self.textarea.insert(END, f"\nPAYABLE AMOUNT          {self.payable_price.get()[:self.payable_price.get().index('.')+3]}")
            self.textarea.insert(END, "\n==========================================")

            self.save_bill()
            self.check_print_bill = 1
            self.print()

    def save_bill(self):

        flag = mb.askyesno("SAVE", "Do you want to save the bill?")
        if flag:
            self.bill_data = self.textarea.get('1.0', END)
            with open("bills/" + str(self.c_bill.get()) + ".txt", "w") as file:
                file.write(self.bill_data)
            file.close()
            notification.notify(title = "BILLING SOFTWARE", message = f"Bill no. {self.c_bill.get()} is saved successfully", timeout = 5)
        else:
            pass

    def find_bill(self):
        if self.search_bill.get().strip() != "": 
            flag = 0
            for i in os.listdir("bills/"):
                if i.split('.')[0] == self.search_bill.get():
                    flag = 1
                    file = open(f"bills/{i}", "r")
                    self.textarea.delete('1.0', END)
                    self.textarea.insert(END, file.read())
                    file.close()
                    self.check_print_bill = 1
                    break
            if flag == 0:
                mb.showerror("NOT FOUND", f"No records of the bill number {self.search_bill.get()} found.")
            else:
                pass
        else:
            mb.showerror("ERROR", f"No bill number entered\nFirst enter the bill number.")

    def print(self):
        flag = mb.askyesno("SAVE", "Do you want to print the bill?")
        if flag:
            if self.check_print_bill == 1:
                new_file = tempfile.mktemp('.txt')
                open(new_file, 'w').write(self.textarea.get('1.0', END))
                os.startfile(new_file, 'print')
                notification.notify(title = "BILLING SOFTWARE", message = f"Bill no. {self.c_bill.get()} is printed successfully", timeout = 5)
            else:
                mb.showerror("ERROR", "Please generate bill first then click on print.")
        else:
            pass

    def clear_all(self):

        flag = mb.askyesno("CLEAR ALL", "Do you want to clear all?")

        if flag:
            for i in range(0,18):
                self.cosmetics[i].set(0)

            for i in range(0,18):
                self.grocerys[i].set(0)

            for i in range(0,18):
                self.stationarys[i].set(0)

            self.cosmetic_price.set("Rs 0.0")
            self.grocery_price.set("Rs 0.0")
            self.stationary_price.set("Rs 0.0")
            self.total_price.set("Rs 0.0")
            self.discount_price.set("0.0%")

            self.cosmetic_tax.set("Rs 0.0")
            self.grocery_tax.set("Rs 0.0")
            self.stationary_tax.set("Rs 0.0")
            self.total_tax.set("Rs 0.0")
            self.payable_price.set("Rs 0.0")

            self.c_name.set("")
            self.c_phone.set("")
            self.c_bill.set("")
            self.c_bill.set(str(ra.randint(100000, 999999)))
            self.search_bill.set("")

            self.welcome_bill()
        else:
            pass

    def exit(self):
        flag = mb.askyesno("EXIT", "Do you want to EXIT")
        if flag:
            self.root.destroy()
        else:
            pass

root = Tk()
obj = Billing_Software(root)
root.mainloop()