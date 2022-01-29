class Dict_Parsing:
  def __init__ (self,a):
    self.a = a

  def getkey(self):
    if self.notdict():
      print ( list(self.a.keys()) )

  def getvalue(self):
    if self.notdict():
      return list(self.a.values())

  def notdict(self):
    if type(self.a) != dict :
      raise Exception (self.a,"Not Dictonary")
    return 1

  def nouserinput(self):
    self.a = eval(input())
    print(self.a, type(self.a))
    print(self.getkey())
    print(self.getvalue())

  def getinsersion(self,k,v):
    self.a[k] = v

d11 = Dict_Parsing({"k" : "mahima", "k1" : "Hello"})

d11.getvalue()
d11.nouserinput()
d11.getkey()
d11.getinsersion("L","LIFE")
