from thermopy import nasa9polynomials as nasa9
from analysis import koef_list

def therm_data(c, valem):
    db = nasa9.Database()
    stoichiometry=koef_list(c, valem)
    try:
        reacts=[]
        for comp in stoichiometry[0]:
            reacts.append(db.set_compound(comp))
        prods=[]
        for prod in stoichiometry[1]:
            prods.append(db.set_compound(prod))
        reacts_coefs=[]
        for r_coef in stoichiometry[2]:
            reacts_coefs.append(r_coef)
        prods_coefs=[]
        for p_coef in stoichiometry[3]:
            prods_coefs.append(p_coef)
        reacts=tuple(reacts)
        prods=tuple(prods)
        reacts_coefs=tuple(reacts_coefs)
        prods_coefs=tuple(prods_coefs)
        reaction1 = nasa9.Reaction(293, reacts, prods, reacts_coefs, prods_coefs)
        return reaction1.entropy_reaction(), reaction1.enthalpy_reaction()/1000, reaction1.gibbs_energy_reaction()/1000
        
    except:
        return
