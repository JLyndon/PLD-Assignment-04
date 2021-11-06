def ProductS_Quant():
    NumbApl = int(input("\nHow many apples would you like to buy? \n> "))
    NumbOrng = int(input("\nHow many oranges would you like to buy? \n> "))
    return NumbApl, NumbOrng

def total_(NumApl, NumOrng):
    ttlprc_apl = NumApl*20
    ttlprc_orng = NumOrng*25
    summation = ttlprc_apl + ttlprc_orng
    return summation

apl_quant, orng_quant = ProductS_Quant()

grnd_total = total_(apl_quant, orng_quant)

print(f"\nThe total amount is {grnd_total}.")