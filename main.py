from analysis import *
from algorithm import *
from thermodynamics import *
    
#valem_test1 = "C8H16,1-octene + O2 -> CO2 + H2O(l)"
valem_test3 = "Cu{2+} + OH{-} = Cu(OH)2"
valem_test2 = "H2 + Al + O2 + Cl2 = AlOHCl2"
valem_test4 = "H2 + Ca(CN)2 + NaAlF4 + FeSO4 + MgSiO3 + KI + H3PO4 + PbCrO4 + BrCl + CF2Cl2 + SO2 = PbBr2 + CrCl3 + MgCO3 + KAl(OH)4 + Fe(SCN)3 + PI3 + Na2SiO3 + CaF2 + H2O"
#valem = input("Näited korrektselt sisestatud valemitest:\n{}\n{}\n{}\n\nSisesta valem: ".format(valem_test1, valem_test2, valem_test3))
valem = valem_test3
km = komp_maatriks(valem)
c = lahenda(km)
mvis(km,valem)

try:
    print("\nTASAKAALUSTATUD VALEM\n" + tasakaalustatud(c,valem))
    print("\nTERMODÜNAAMILISED ANDMED")
    try:
        print("Antud reaktsiooni standardse entroopia muut on {:.2f} J/(mol*k), standardse entalpia muut on {:.2f} kJ/mol ja standardse Gibbsi vaba energia muut on {:.2f} kJ/mol.".format(*therm_data(c, valem)))
    except:
        print("Andmebaasis ei ole piisavalt andmeid arvutamiseks.")
    
except:
    print("Valemit pole võimalik tasakaalustada.")
