import random
class Warrior():
    def setHealth(self, health):
        self.health = health
    def getHealth(self):
        return self.health
    def defense(self):
        self.health -= (20 * random.random())
        return self.health
rw = Warrior()
bw = Warrior()
rw.setHealth(100)
bw.setHealth(100)
rw.getHealth()
bw.getHealth()
while rw.getHealth() > 0 and bw.getHealth() > 0:
      if rw.getHealth() > 0:
       print("Red warrior is attacking...")
       bw.defense()
       print("Health of Blue Warrior is: " + str(bw.getHealth()))
      if bw.getHealth() > 0:
       print("Blue warrior is attacking...")
       rw.defense()
       print("Health of Red Warrior is: " + str(rw.getHealth()))
if bw.getHealth() <= 0.00:
    print("The war has ended!")
    print("Red warrior won this battle !!!")
elif rw.getHealth() <= 0.00:
    print("The war has ended!")
    print("Blue warrior won this battle !!!")          