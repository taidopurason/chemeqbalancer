from analysis import *
from algorithm import *
try:
    from tkinter import *
except:
    from Tkinter import *

def tasakaalusta():
    valem = sisend.get()
    km = komp_maatriks(valem)
    c = lahenda(km)
    mvis(km,valem)
    try:
        vastus.set("\nTASAKAALUSTATUD VALEM\n" + tasakaalustatud(c,valem))
    except:
        vastus.set("Valemit pole võimalik tasakaalustada.")  

valem_test1 = "CH3(CH2)3OH + O2 -> CO2 + H2O"
valem_test2 = "Cu{2+} + OH{-} = Cu(OH)2"

ui = Tk()
sisend = Entry(ui, width=50)
sisend.pack()
Button(ui, text="TASAKAALUSTA", command=tasakaalusta).pack()
vastus = StringVar()
vastus.set("Näited korrektselt sisestatud valemitest:\n{}\n{}".format(valem_test1, valem_test2))
Label(ui, textvariable=vastus).pack()

ui.mainloop()