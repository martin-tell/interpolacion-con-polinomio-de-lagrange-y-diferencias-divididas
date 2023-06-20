from tkinter import Tk, Frame, Label, Entry, Button, Listbox, messagebox, Text
from tabulate import tabulate
from metodos_interpolacion import polinomio_de_lagrange, diferencias_divididas

class Interfaz:

    def __init__(self) -> None:
        self.cadena_puntos = ""
        self.n_puntos = 0
        self.xn = list()
        self.yn = list()
        self.p = None

        self.raiz = Tk()
        self.raiz.title("Interpolación")
        self.raiz.resizable(0, 0)

        self.base = Frame()
        self.base.pack()

        Label(self.base, text="x").grid(row=0, column=0)
        Label(self.base, text="f(x)").grid(row=0, column=1)
        self.lista_puntos = Listbox(self.base)
        self.lista_puntos.grid(row=1, column=0, rowspan=6, columnspan=2, padx=10, pady=10)

        Label(self.base, text="Valores de x").grid(row=1, column=2)
        self.campo_equis = Entry(self.base)
        self.campo_equis.grid(row=1, column=3, columnspan=7, padx=10)
        self.campo_equis.config(justify="center", width=100)

        Label(self.base, text="Evaluaciones").grid(row=2, column=2)
        self.campo_evaluaciones = Entry(self.base)
        self.campo_evaluaciones.grid(row=2, column=3, columnspan=7, padx=10)
        self.campo_evaluaciones.config(justify="center", width=100)

        Label(self.base, text="Grado").grid(row=3, column=2)
        self.campo_grado = Entry(self.base)
        self.campo_grado.grid(row=3, column=3, padx=10, columnspan=7)
        self.campo_grado.config(justify="center", width=100)

        Label(self.base, text="Valor x").grid(row=4, column=2)
        self.campo_valor_x = Entry(self.base)
        self.campo_valor_x.grid(row=4, column=3, padx=10, columnspan=7)
        self.campo_valor_x.config(justify="center", width=100)

        Label(self.base, text="Puntos").grid(row=5, column=2)
        self.campo_puntos_evaluar = Entry(self.base)
        self.campo_puntos_evaluar.grid(row=5, column=3, columnspan=7, padx=10)
        self.campo_puntos_evaluar.config(justify="center", width=100)

        self.boton_indroduce_valores = Button(self.base, text="Introduce Valores", command=self.introduce_valores)
        self.boton_indroduce_valores.grid(row=6, column=4)

        self.boton_elige_punto = Button(self.base, text="Elige Punto", command=self.elige_punto)
        self.boton_elige_punto.grid(row=6, column=5)

        self.boton_nuevos_puntos = Button(self.base, text="Nuevos Puntos", command=self.nuevos_puntos)
        self.boton_nuevos_puntos.grid(row=6, column=6)

        self.boton_interpolar = Button(self.base, text="Interpolar", command=self.interpolar, state="disable")
        self.boton_interpolar.grid(row=6, column=7)

        self.datos = Text(self.base, width=115, height=15)
        self.datos.grid(row=7, column=0, padx=10, columnspan=9)

        Label(self.base, text="Pol. Lagrange").grid(row=8, column=0, columnspan=2, pady=10)
        self.campo_lagrange = Entry(self.base)
        self.campo_lagrange.grid(row=8, column=2, padx=10)
        self.campo_lagrange.config(justify="center")

        Label(self.base, text="Dif. Div.").grid(row=8, column=3)
        self.campo_diferencias = Entry(self.base)
        self.campo_diferencias.grid(row=8, column=4, padx=10)
        self.campo_diferencias.config(justify="center")

        self.raiz.mainloop()

    def interpolar(self):
        self.campo_lagrange.delete(0, "end")
        self.campo_diferencias.delete(0, "end")
        self.datos.delete(1.0, "end")
        p = float(self.campo_valor_x.get())
        self.campo_lagrange.insert(0, polinomio_de_lagrange(p, self.xn, self.yn))
        matriz, y = diferencias_divididas(p, self.xn, self.yn)
        self.datos.insert(1.0, "Tabla Diferencias Divididas\n"+tabulate(matriz, tablefmt='fancy_grid'))
        self.campo_diferencias.insert(0, y)
            

    def verifica_grado(self):
        g = int(self.campo_grado.get())
        if self.n_puntos == g:
            self.boton_interpolar.config(state="normal")
        return self.n_puntos < g
    
    def nuevos_puntos(self):
        self.campo_puntos_evaluar.delete(0, "end")
        self.xn.clear()
        self.yn.clear()
        self.cadena_puntos = ""
        self.n_puntos = 0
        self.boton_interpolar.config(state="disable")

    def elige_punto(self):
        if self.verifica_grado():
            i = self.lista_puntos.curselection()[0]
            x = float(self.lista_puntos.get(i)[0])
            y = float(self.lista_puntos.get(i)[1])
            self.xn.append(x)
            self.yn.append(y)
            punto = f"({x},{y})"
            self.cadena_puntos += punto
            self.campo_puntos_evaluar.delete(0, "end")
            self.campo_puntos_evaluar.insert(0, self.cadena_puntos)
            self.n_puntos += 1
        else:
            messagebox.showinfo("Puntos suficientes", "Ya ha insertado la cantidad de puntos suficientes.")

    def introduce_valores(self):
        self.lista_puntos.delete(0, "end")
        x = self.campo_equis.get().split(',')
        fx = self.campo_evaluaciones.get().split(',')
        for punto in zip(x, fx):
            self.lista_puntos.insert("end", punto)

if __name__ == "__main__":
   Interfaz()

# xn = [1.3, 1.6]
# yn = [0.6200860, 0.4554022]
# print(polinomio_de_lagrange(1.5, xn, yn))
# print(diferencias_divididas(1.5, xn, yn)[1])
#
# xn = [1.3, 1.6, 1.9]
# yn = [0.6200860, 0.4554022, 0.2818186]
# print(polinomio_de_lagrange(1.5, xn, yn))
#
# xn = [1.0, 1.3, 1.6, 1.9, 2.2]
# yn = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
# print(polinomio_de_lagrange(1.5, xn, yn))
#
# xn = [1.0, 1.3, 1.6, 1.9, 2.2]
# yn = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
# print(diferencias_divididas(1.5, xn, yn)[1])

#1.0,1.3,1.6,1.9,2.2
#0.7651977,0.6200860,0.4554022,0.2818186,0.1103623

#0.0,0.5,1.0,2.0
#1.00000,1.64872,2.71828,7.38906

#1930,1940,1950,1960,1970,1980
#123203,131669,150697,179323,203212,226505