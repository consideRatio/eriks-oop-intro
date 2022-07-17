# Klassdefinition
# - __init__
# - self
# - skapa objekt/instanser
# - metoder
# - 
#
# O

def detta_är_en_funktion():
    pass

class Bil:
    hur_många_bilar_finns_det = 0

    def __init__(self, färg):
        self.bilens_färg = färg
    
    def print_metoden(self):
        print(f"Hej jag är en {self.bilens_färg} bil!")

    def return_metoden(self):
        return f"Hej jag är en {self.bilens_färg} bil!"

    def print_antal_bilar(self):
        print(hur_många_bilar_finns_det)



brun_bil = Bil("brun")
brun_bil.print_antal_bilar()

grön_bil = Bil("grön")
brun_bil.print_antal_bilar()

brun_bil.print_metoden()
grön_bil.print_metoden()

