import math

def energy_consumption(CA,Fconv,Fcorr):
    Fconv_value = ""
    Fcorr_value = ""
    F1_values = [["gasoline",0.770],["anhydrous alcohol",0.534],["hydrated alcohol",0.510],["diesel",0.848],["dry gas",0.880]] #Fconv
    F2_values = [["solid_liquid",0.95],["gas",0.90]] #Fcorr
    for i in F1_values:
        if i[0] == Fconv:
            Fconv_value = i[1]
    for i in F2_values:
        if i[0] == Fcorr:
            Fcorr_value = i[1]
    CC = CA * Fconv_value * Fcorr_value * 45.2 * math.pow(10,-3)
    return CC

def carbon_emission(CC,Femiss):
    Femiss_value = ""
    F_values = [["gasoline",18.9],["anhydrous alcohol",14.81],["hydrated alcohol",14.81],["diesel",20.2],["dry gas",15.3]] #Femiss
    for i in F_values:
        if i[0] == Femiss:
            Femiss_value = i[1]
    QC =  CC * Femiss_value * math.pow(10,-3)
    return QC

def co2_Emission(EC):
    ECO2 = (EC * 44 / 12) * 1000 * 1000
    return ECO2

def gcc_emission(CA,Fconv,Fcorr,Femiss):
    CC = energy_consumption(CA,Fconv,Fcorr)
    EC = carbon_emission(CC,Femiss)
    ECO2 = co2_Emission(EC)
    return ECO2