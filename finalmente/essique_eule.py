import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np
import tkinter as tk 
from ctypes import windll, byref, sizeof, c_int
import ctypes as ct
from customtkinter import *
import pandas as pd
from PIL import Image    
from time import localtime

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #f1 = GradientFrame(self, borderwidth=1, relief="sunken")
        f2 = GradientFrame(self,(161, 183, 237),(175, 237, 161), borderwidth=1, relief="sunken")
        #f1.pack(side="top", fill="both", expand=True)
        f2.pack(side="bottom", fill="both", expand=True)
class GradientFrame(tk.Canvas):
    def __init__(self, parent, color1=(175, 237, 161), color2=(161, 183, 237),axi=1, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.axi = axi
        def convHEX(r,g,b):
            return f"#{r:02x}{g:02x}{b:02x}"
        if type(color1[0]) is str:
            self._color1 = color1
            self._color2 = color2
        else:
            self._color1 = convHEX(int(color1[0]),int(color1[1]),int(color1[2]))
            self._color2 = convHEX(int(color2[0]),int(color2[1]),int(color2[2]))  
        self.bind("<Configure>", self._draw_gradient)
    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()   
        if self.axi == 1:
            limit = height
            (r1,g1,b1) = self.winfo_rgb(self._color1)
            (r2,g2,b2) = self.winfo_rgb(self._color2)
            r_ratio = float(r2-r1) / limit
            g_ratio = float(g2-g1) / limit
            b_ratio = float(b2-b1) / limit
            for i in range(limit):  
                nr = int(r1 + (r_ratio * i))
                ng = int(g1 + (g_ratio * i))
                nb = int(b1 + (b_ratio * i))
                color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
                self.create_line(0,i,i+width*height,height, tags=("gradient",), fill=color)
            self.lower("gradient")
        else:
            limit = width
            (r1,g1,b1) = self.winfo_rgb(self._color1)
            (r2,g2,b2) = self.winfo_rgb(self._color2)
            r_ratio = float(r2-r1) / limit
            g_ratio = float(g2-g1) / limit
            b_ratio = float(b2-b1) / limit
            for i in range(limit):
                nr = int(r1 + (r_ratio * i))
                ng = int(g1 + (g_ratio * i))
                nb = int(b1 + (b_ratio * i))
                color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
                self.create_line(i,0,i,height, tags=("gradient",), fill=color)
            self.lower("gradient")
    def convHEX(r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"



class CONM:
    def __init__(self):
        self.produtos_id = { 
            "agua c/ gas": 2,"coca-cola": 3,"coca-cola-0": 4, "agua-coco":5,"budweiser":6,"heineken":7,"fanta-guarana":8,"fanta-laranja":9,"fanta-uva":10,
            "tonica-antartica": 11,"schweppes":12,"suco-del-vale":13,"monster":14,"red-bull":15,"toddynho":16,"agua s/ gas":17
            }
        self.plusplus = CTkImage(Image.open("plus.png"))
        self.lessless = CTkImage(Image.open("less.png"))
        self.host = "localhost"
        self.user = "admin"
        self.user_pass = "DuDu$1605"
        self.qnt_value =  0
        # conecta no banco de dados #
        self.conexao = self.create_server(self.host,self.user,self.user_pass)
        # executa comandos no banco #
        self.exec_query(self.conexao, "use geladeira;", result=False)
        self.convert = lambda r,g,b: f"#{r:02x}{g:02x}{b:02x}"
        self.vender1 =  lambda: self.vender(self.conexao, self.lista_obj.get(), self.qnt_value)
        self.root = CTk()
        
        self.root.geometry("400x400")
        self.root.title("Lançador de comandas")
        self.root.resizable(True, True)
       

        self.label = tk.Label(master=self.root,text="oI", width=400, height=400,relief=None)
        self.label.pack(fill="both", expand=True)#relx=0.5, rely=0.5, anchor="center")
        self.dark_title_bar(self.root)
        self.tela = tk.Label(master=self.root, width=40,height=20
                    , text="", background=self.convert(240,230,230))
        self.lista_obj = CTkComboBox(self.tela, values=["escolha um produto"])

        Example(self.label).pack(fill="both", expand=True)
     
    
        
        self.tela.place(relx=0.5, rely=0.5, anchor="center")
        self.main()
        
        #self.ler_excel(conexao)

    def dark_title_bar(self, window):
        window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(window.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
     

    def log(self, acao):
        with open(AMBIENTE["HOMEPATH"]+"\\log\\log.txt", "a") as p:
            p.write("[{}/{}/{}:=:{}:{}]: {}\n".format(localtime()[0],
                                                      localtime()[1],
                                                      localtime()[2],
                                                      localtime()[3],
                                                      localtime()[4],
                                                        acao))
            
    def get_data(self, conn,  table="produtos") -> list:
        res = self.exec_query(conn, "select * from {};".format(table), result=True)
        dick = []
        self.id = []
        for a in range(0, len(res)):
            dick.append(res[a][0])
            self.id.append(res[a][2])
        self.lista_obj.configure(values=dick)
        
        return res
    
    def create_server(self, host, user, user_pass):
        conn = None
        try:
            conn = mysql.connector.connect( host=self.host, user=self.user, passwd=self.user_pass)
            print("[SUCESSO lek]")
        except Error as err:
            print("[!] vish... : {}".format(err))
        return conn
    def vender(self, conn,  prod, qnt):
        #self.exec_query(conn, "use geladeira;")
        self.
        dia = str(localtime()[2])+"/"+str(localtime()[1])+"/"+str(localtime()[0])+"["+str(localtime()[3])+":"+str(localtime()[4])+"]"
        
        self.exec_query(conn, "insert into vendidos(nome , qnt, data)  values('{}', {}, '{}');".format(prod, qnt, dia), result=False)
        
        
    def db_conn(self, host, user, user_pass, db_name="geladeira"):
        conn = None
        try:
            conn = mysql.connector.connect(host=self.host, user=self.user, passwd=self.user_pass, database=db_name)
        except Error as err:
            print("[vish... não foi possivel se conectar a {} ]: {}".format(db_name,err))
        return conn

    def exec_query(self, conn, query, result=False):
        if result is True:
            self.cursor = conn.cursor(buffered=True)
            try:
                self.cursor.execute(query)
                r = self.cursor.fetchall()
                conn.commit()
                print("[SUCESSO!]")
            except Error as err:
                print("[vish... houve erro na linha de comando]: {}".format(err))
                r= 0 

            return r
        else:
            self.cursor = conn.cursor(buffered=True)
            try:
                self.cursor.execute(query)
                conn.commit()
                print("[SUCECO]")
            except Error as err:
                print("[comando não executado ou digitado corretamente]: {}".format(err))

    def escrever(self):
        pass

    def deposito(self):
        pass

    def mais(self):
        value = int(self.qnt_value)+1
        self.qnt_value = str(value)
        self.quantidade.configure(text=self.qnt_value)
               
            
    def menos(self):
        if int(value) != 0:
            value = int(self.qnt_value) - 1
            self.qnt_value = str(value)
            self.quantidade.configure(text=self.qnt_value)
        
        
    def main(self):
        
        self.lista_obj.place(relx=0.3, rely=0.1, anchor="center")
        itens = self.get_data(self.conexao)
    
        self.error_text = CTkLabel(self.tela, text="")
        self.bottao_lan = CTkButton(self.tela, text="Lançar", width=30, command=self.vender1)
        self.bottao_lan.place(relx=0.3, rely=0.8, anchor="center")

        self.bottao_op = CTkButton(self.tela, text="Depósito", width=55, fg_color=self.convert(200,80,60), command=self.deposito)
        self.bottao_op.place(relx=0.8, rely=0.8, anchor="center")

        self.bottao_pls = CTkButton(self.tela, image=self.plusplus,text="", width=20, height=20, corner_radius=20, border_width=1, command=self.mais)
        self.bottao_pls.place(relx=0.5, rely=0.3, anchor="center")

        self.bottao_lss = CTkButton(self.tela, image=self.lessless, text="", width=20, height=20, corner_radius=20, border_width=1, command=self.menos)
        self.bottao_lss.place(relx=0.1, rely=0.3, anchor="center")
        
        self.quantidade = CTkLabel(self.tela, text=self.qnt_value)
        self.quantidade.place(relx=0.3, rely=0.3, anchor="center")
        self.error_text.place(relx=0.3, rely=0.4, anchor="center")
        self.root.mainloop()

    def alterar_(self, conn, a):
        pass

if __name__ == "__main__":
    CONM()
    
