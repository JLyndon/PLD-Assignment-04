def ProductS_Quant():
    while True:
        NumbApl = input("\nHow many apples would you like to buy? \n> ")
        NumbOrng = input("\nHow many oranges would you like to buy? \n> ")
        if NumbApl.isdigit() and NumbOrng.isdigit() == True:
            InitApl = int(NumbApl)
            InitOrng = int(NumbOrng)
            return InitApl, InitOrng
        elif NumbApl.isalpha() or NumbOrng.isalpha() == True:
            print("\nInputs must be both numerical values.")
        elif NumbApl.isspace() or NumbOrng.isspace() == True:
            print("\nPlease fill all the blanks.")
        else:
            if NumbApl.replace(",","",10).isdigit() and NumbOrng.replace(",","",10).isdigit() == True:
                Apl_Q = int(NumbApl.replace(",","",10))
                Orng_Q = int(NumbOrng.replace(",","",10))
                return Apl_Q, Orng_Q

def total_(NumApl, NumOrng):
    ttlprc_apl = NumApl*20
    ttlprc_orng = NumOrng*25
    summation = ttlprc_apl + ttlprc_orng
    return summation

apl_quant, orng_quant = ProductS_Quant()

grnd_total = total_(apl_quant, orng_quant)

print(f"\nThe total amount is {grnd_total}.")