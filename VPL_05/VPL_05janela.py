from tkinter import *


##################################################

class Janela(Tk):  ## Questão 01: (Complete o código que declara a classe)
    __Lb_flamengo = None
    __Lb_vasco = None
    __Lb_torcida_total = None
    __Lb_pr = None
    __Lb_sc = None
    __Lb_rs = None
    __Et_flamengo_pr = None
    __Et_flamengo_sc = None
    __Et_flamengo_rs = None
    __Et_vasco_pr = None
    __Et_vasco_sc = None
    __Et_vasco_rs = None
    __Et_total_flamengo = None
    __Et_total_vasco = None
    __Bt_calc = None

    def __init__(self, Str="Minha janela", cor='orange'):
        super().__init__()
        super().title(Str)
        super().configure(bg=cor)
        self.inicialize()

    def action_Total_Flamengo(self):
        valor1 = float(self.__Et_flamengo_pr.get())
        valor2 = float(self.__Et_flamengo_sc.get())
        valor3 = float(self.__Et_flamengo_rs.get())
        soma_fla = valor1 + valor2 + valor3
        self.__Et_total_flamengo.delete(0, END)
        self.__Et_total_flamengo.insert(END, "%.1f" % soma_fla)

    def action_Total_Vasco(self):
        valor1 = float(self.__Et_vasco_pr.get())
        valor2 = float(self.__Et_vasco_sc.get())
        valor3 = float(self.__Et_vasco_rs.get())
        soma_vasco = valor1 + valor2 + valor3
        self.__Et_total_vasco.delete(0, END)
        self.__Et_total_vasco.insert(END, "%.1f" % soma_vasco)

    def action_exit(self):
        print("Destruindo janela")
        self.destroy()

    def action_Bt_calc(self):
        self.action_Total_Flamengo()
        self.action_Total_Vasco()

    def inicialize(self):
        self.__Lb_flamengo = Label(self, text="Flamengo", width=20, bg='yellow')
        self.__Lb_vasco = Label(self, text="Vasco", width=20, bg='yellow')
        self.__Lb_pr = Label(self, text="Paraná", width=20, bg='yellow')
        self.__Lb_sc = Label(self, text="Santa Catarina", width=20, bg='yellow')
        self.__Lb_rs = Label(self, text="Rio G. do Sul", width=20, bg='yellow')
        self.__Lb_torcida_total = Label(self, text="Torcida total:", width=20, bg='yellow')

        self.__Et_flamengo_pr = Entry(self, width=22)
        self.__Et_flamengo_sc = Entry(self, width=22)
        self.__Et_flamengo_rs = Entry(self, width=22)
        self.__Et_vasco_pr = Entry(self, width=22)
        self.__Et_vasco_sc = Entry(self, width=22)
        self.__Et_vasco_rs = Entry(self, width=22)
        self.__Et_total_flamengo = Entry(self, width=22)
        self.__Et_total_vasco = Entry(self, width=22)

        self.__Bt_calc = Button(self, text='Calcular', command=self.action_Bt_calc)

        self.__Lb_flamengo.grid(row=0, column=1, rowspan=1, columnspan=1)
        self.__Lb_vasco.grid(row=0, column=2)
        self.__Lb_pr.grid(row=1, column=0, rowspan=1, columnspan=1)
        self.__Lb_sc.grid(row=2, column=0)
        self.__Lb_rs.grid(row=3, column=0)
        self.__Lb_torcida_total.grid(row=5, column=0)

        self.__Et_flamengo_pr.grid(row=1, column=1, padx=2, pady=2, columnspan=1)
        self.__Et_vasco_pr.grid(row=1, column=2, padx=2, pady=2, columnspan=1)
        self.__Et_flamengo_sc.grid(row=2, column=1, padx=2, pady=2, columnspan=1)
        self.__Et_vasco_sc.grid(row=2, column=2, padx=2, pady=2, columnspan=1)
        self.__Et_flamengo_rs.grid(row=3, column=1, padx=2, pady=2, columnspan=1)
        self.__Et_vasco_rs.grid(row=3, column=2, padx=2, pady=2, columnspan=1)
        self.__Et_total_flamengo.grid(row=5, column=1)
        self.__Et_total_vasco.grid(row=5, column=2, columnspan=1)

        self.__Bt_calc.grid(row=4, column=1)

        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
