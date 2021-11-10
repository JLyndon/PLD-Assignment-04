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
            if "," in NumbApl or NumbOrng:
                ModNumApl, ModNumOrng = CommaReader(NumbApl, NumbOrng)
                if ModNumApl.isdigit() and ModNumOrng.isdigit() == True:
                    FnlApl = int(ModNumApl)
                    FnlOrng = int(ModNumOrng)
                    return FnlApl, FnlOrng
                else:
                    if "." in ModNumApl or ModNumOrng:
                        ValueChckApl = ModNumApl.split(".")
                        ValueChckOrng = ModNumOrng.split(".")
                        if (len(ValueChckApl)) + (len(ValueChckOrng)) == 4: 
                            if (int(ValueChckApl[1]) > 0) and (int(ValueChckOrng[1]) > 0):
                                print("\nYou can't purchase a fraction of our products.\nPlease enter whole quantity values.")
                            elif (int(ValueChckApl[1]) == 0) and (int(ValueChckOrng[1]) == 0):
                                EligiApl= int(ValueChckApl[0])
                                EligiOrng = int(ValueChckOrng[0])
                                return EligiApl, EligiOrng
                            elif (int(ValueChckApl[1]) == 0) and (int(ValueChckOrng[1]) > 0):
                                print("\nYou can't purchase a fraction of an orange.\nPlease enter whole quantity values.")
                            elif (int(ValueChckApl[1]) > 0) and (int(ValueChckOrng[1]) == 0):
                                print("\nYou can't purchase a fraction of an apple.\nPlease enter whole quantity values.")
                        elif (len(ValueChckApl)) + (len(ValueChckOrng)) == 3:
                            if (len(ValueChckApl)) == 2:
                                if int(ValueChckApl[1]) > 0:
                                    print("\nYou can't purchase a fraction of an apple.\nPlease enter whole quantity values.")
                                elif int(ValueChckApl[1]) == 0:
                                    EligiApl= int(ValueChckApl[0])
                                    EligiOrng = int(ValueChckOrng[0])
                                    return EligiApl, EligiOrng
                            elif (len(ValueChckApl)) == 1:
                                if int(ValueChckOrng[1]) > 0:
                                    print("\nYou can't purchase a fraction of an orange.\nPlease enter whole quantity values.")
                                elif int(ValueChckOrng[1]) == 0:
                                    EligiApl= int(ValueChckApl[0])
                                    EligiOrng = int(ValueChckOrng[0])
                                    return EligiApl, EligiOrng
                                                     

def CommaReader(AplInp, OrngInp):
    if "," in AplInp and OrngInp:
        Price_01 = AplInp.replace(",","")
        Price_02 = OrngInp.replace(",","")
        return Price_01, Price_02
    elif "," in AplInp:
        AplprcOnly = AplInp.replace(",","")
        return AplprcOnly, OrngInp
    elif "," in OrngInp:
        OrngprcOnly = OrngInp.replace(",","")
        return AplInp, OrngprcOnly
    else:
        return AplInp, OrngInp

def total_(NumApl, NumOrng):
    ttlprc_apl = NumApl*20
    ttlprc_orng = NumOrng*25
    summation = ttlprc_apl + ttlprc_orng
    return summation

apl_quant, orng_quant = ProductS_Quant()

grnd_total = total_(apl_quant, orng_quant)

print(f"\nThe total amount is {grnd_total:,} Php.")