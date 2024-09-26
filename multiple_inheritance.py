class father():
    def gardening(self):
        print("I enjoy gardening")
class mother():
    def cooking(self):
        print("I love cooking")

class child(father,mother):
    def sports(self):
        print("I enjoy sports")

c = child()
c.sports()
c.cooking()
c.gardening()


# or you can do it as this

class plar():
    def skills(self):
        print("Wushu, Coding")
class mor():
    def skills(self):
        print("cooking, studying")
class zoy():
    def skills(self):
        plar.skills(self)
        mor.skills(self)
        print("Fun")
c=zoy()
c.skills()
