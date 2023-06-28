class item:
    def __init__(self, name: str, category: str, buy_price: int, sell_price: int, attack: int, defense: int):
        self.name = name
        self.category = category
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.attack = attack
        self.defense = defense

def heal():
    global health, medpacs
    if medpacs == 0:
        print("You don't have any medpacs!")
        return
    health += round((health * 0.2))
    medpacs -= 1