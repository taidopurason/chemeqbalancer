import os
import re
import xml.etree.ElementTree as ET
import numpy as np
from thermopy.constants import ideal_gas_constant
_R = ideal_gas_constant[0]

#Calculate molar enthalpy at constant pressure for the compound for a given temperature
def enthalpy(self, T):
    coefficients = np.empty(9, dtype=np.float32)
    for (i, coef) in enumerate(self._xml_compound.findall(
            'T_range')[self._evaluate_temperature_interval(T)]):
        coefficients[i] = np.array(coef.text, dtype=np.float32)
    exponents = np.array([-2, -1, 0, 1, 2, 3, 4, -1],
                         dtype=np.signedinteger)
    other_factors = np.array([-1, np.log(T), 1, 0.5, 1/3, 0.25, 0.2, 1],
                             dtype=np.float32)
    return np.sum(
        np.multiply(
            np.multiply(
                np.power(T, exponents, dtype=np.float32),
                coefficients[0:8]),
            other_factors), dtype=np.float32) * _R * T



#Calculate molar entropy at constant pressure for the compound for a given temperature
def entropy(self, T):
    coefficients = np.empty(9, dtype=np.float32)
    for (i, coef) in enumerate(self._xml_compound.findall(
            'T_range')[self._evaluate_temperature_interval(T)]):
        coefficients[i] = np.array(coef.text, dtype=np.float32)
    exponents = np.array([-2, -1, 0, 1, 2, 3, 4, 0, 0],
                         dtype=np.signedinteger)
    other_factors = np.array([-0.5, -1, np.log(T), 1, 0.5, 1/3, 0.25,
                              0, 1],
                             dtype=np.float32)
    return np.sum(
        np.multiply(
            np.multiply(np.power(T, exponents, dtype=np.float32),
                        coefficients[:]),
            other_factors), dtype=np.float32) * _R



#Calculate molar Gibbs energy at constant pressure for the compound for a given temperature
def gibbs_energy(self, T):
    return self.enthalpy(T) - T * self.entropy(T)


#Initializes a Reaction object
def __init__(self, T, reactants, products, reactants_coefficients, product_coefficients):
    self.T = T
    self._reactants = reactants
    self._products = products
    self._rcoefs = tuple(abs(z) for z in reactants_coefficients)
    self._pcoefs = tuple(abs(z) for z in product_coefficients)
    # error checking
    if (len(self._reactants) != len(self._rcoefs) or
            len(self._products) != len(self._pcoefs)):
        raise Exception('Number of reactants or products is different'
                        'from the number of coefficients given')
    
    
    
# Calculate the enthalpy of the reaction at the standard state
def enthalpy_reaction(self, T=None):
    if T is not None:
        self.T = T
    deltah = 0
    for (coefficient, compound) in zip(self._rcoefs, self._reactants):
        deltah = deltah - coefficient * compound.enthalpy(self.T)
    for (coefficient, compound) in zip(self._rcoefs, self._products):
        deltah = deltah + coefficient * compound.enthalpy(self.T)
    return deltah


#Calculate the entropy of the reaction at the standard state
def entropy_reaction(self, T=None):
    if T is not None:
        self.T = T
    deltas = 0
    for (coefficient, compound) in zip(self._rcoefs, self._reactants):
        deltas = deltas - coefficient * compound.entropy(self.T)
    for (coefficient, compound) in zip(self._rcoefs, self._products):
        deltas = deltas + coefficient * compound.entropy(self.T)
    return deltas


#Calculate the Gibbs energy of the reaction at the standard state
def gibbs_energy_reaction(self, T=None):
    if T is not None:
        self.T = T
    deltag = 0
    for (coefficient, compound) in zip(self._rcoefs, self._reactants):
        deltag = deltag - coefficient * compound.gibbs_energy(self.T)
    for (coefficient, compound) in zip(self._rcoefs, self._products):
        deltag = deltag + coefficient * compound.gibbs_energy(self.T)
    return deltag

import thermopy
from thermopy import nasa9polynomials as nasa9
from main import *

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
    print("\n")
    print("Antud reaktsiooni standartse entroopia muut on {:.2f} J/(mol*k), standartse entalpia muut on {:.2f} kJ/mol ja standartse Gibbsi vaba energia muut on {:.2f} kJ/mol.".format(reaction1.entropy_reaction(), reaction1.enthalpy_reaction()/1000, reaction1.gibbs_energy_reaction()/1000))
    
except:
    print("Andmebaasis ei ole piisavalt andmeid arvutamiseks.")
