import analüüs, algoritm

valem = "CH3(CH2)3OH + O2 -> CO2 + H2O"

km = analüüs.komp_maatriks(valem)
c = algoritm.lahenda(km)
analüüs.mvis(km,valem)
print(c)
print(analüüs.tasakaalustatud(c,valem))

