class Player:
    def  __init__(self, name, ap):
        print("I'm born")  # only use once at create
        self.name = name # need a property to save object's info
        self.hp = 100
        self.ap = ap #attack point

    def attack(self, target):
        target.hp = target.hp - self.ap
        print(self.name, "attacking", target.name)
        print(target, "'s' hp less ", target.hp, " point!")

    def allen(self):
        self.name = "allen"

#class 內沒有順序差別，電腦會一次讀
#self. 增加應該在init內，但不一定要在裡面
#function in class is method!
# method 空1行，fuction 2行

p1 = Player(100)
p2 = Player(50)
p1.attack(p2)