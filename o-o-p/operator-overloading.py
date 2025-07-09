class Vault:
    def __init__(self, gold=0, silver=0):
        self.gold = gold
        self.silver = silver

    def __str__(self):
        return f"{self.gold}g gold and {self.silver}kg silver in vault"

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        return Vault(gold, silver)


sham = Vault(20, 403)
zeeshan = Vault(15, 306)
sanan = Vault()


total = sham + zeeshan + sanan
print(total) # 45g gold and 903kg silver in vault

