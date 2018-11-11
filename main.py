from analüüs import *
from algoritm import *

valem_test1 = "CH3(CH2)3OH + O2 -> CO2 + H2O"
valem_test2 = "Cu{2+} + OH{-} = Cu(OH)2"
valem = input("Näited korrektselt sisestatud valemitest:\n{}\n{}\n\nSisesta valem: ".format(valem_test1, valem_test2))

km = komp_maatriks(valem)
c = lahenda(km)
mvis(km,valem)
try:
    print("\nTASAKAALUSTATUD VALEM\n" + tasakaalustatud(c,valem))
except:
    print("Valemit pole võimalik tasakaalustada.")
