from analüüs import *
from algoritm import *

valem_test1 = "CH3(CH2)3OH + O2 -> CO2 + H2O"
valem_test2 = "Cu{2+} + OH{-} = Cu(OH)2"
valem_test3 = "[Cu]{2+} + OH{-} = Cu(OH)2"
valem_test4 = "H2 + Ca(CN)2 + NaAlF4 + FeSO4 + MgSiO3 + KI + H3PO4 + PbCrO4 + BrCl + CF2Cl2 + SO2 = PbBr2 + CrCl3 + MgCO3 + KAl(OH)4 + Fe(SCN)3 + PI3 + Na2SiO3 + CaF2 + H2O"
valem = input("Näited korrektselt sisestatud valemitest:\n{}\n{}\n\nSisesta valem: ".format(valem_test1, valem_test2))
#valem = valem_test1
km = komp_maatriks(valem)
c = lahenda(km)
mvis(km,valem)
try:
    print("\nTASAKAALUSTATUD VALEM\n" + tasakaalustatud(c,valem))
except:
    print("Valemit pole võimalik tasakaalustada.")
