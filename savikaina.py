import json

def date1(item):
  return items[item].get("date")

def warehouse1(item):
  return items[item].get("warehouse")
  
def preke1(item):
  return items[item].get("item")

def kiekis1(item):
  return items[item].get("quantity")

def kaina1(item):
  return items[item].get("cost")

def vnt1(item):
  return items[item].get("cost")/items[item].get("quantity")

def pkiekis1(item):
  return items[item].get("quantity")

def calc2(i,j,kiekis,kaina,vnt):
  return kaina[i]-vnt[j]*(kiekis[i]-kiekis[j])

def calc3(j,kiekis):
  return kiekis[j]

def calc4(i,j,kiekis,kaina,vnt): 
  return kaina[i]+(vnt[j]*-kiekis[i])

def calc5(i,j,kiekis):
  return kiekis[j]+kiekis[i] 
def bugfix():
  return 0
items = [
    {
      'date':"2022.01.01",
      'item':"A",
      'warehouse':"A",
      'quantity':20,
      'cost':1000,
    },
    {
      'date':"2022.01.02",
      'item':"A",
      'warehouse':"A",
      'quantity':25,
      'cost':1000,
    },
    {
      'date':"2022.01.03",
      'item':"B",
      'warehouse':"A",
      'quantity':10,
      'cost':1750,
    },
    {
      'date':"2022.01.04",
      'item':"B",
      'warehouse':"A",
      'quantity':15,
      'cost':1500,
    },
    {
      'date':"2022.01.05",
      'item':"A",
      'warehouse':"B",
      'quantity':12,
      'cost':1440,
    },
    {
      'date':"2022.01.06",
      'item':"B",
      'warehouse':"A",
      'quantity':-13,
      'cost':0,
    },
    {
      'date':"2022.01.07",
      'item':"B",
      'warehouse':"A",
      'quantity':-12,
      'cost':0,
    },
    {
      'date':"2022.01.08",
      'item':"A",
      'warehouse':"A",
      'quantity':-8,
      'cost':0,
    },
    {
      'date':"2022.01.09",
      'item':"A",
      'warehouse':"B",
      'quantity':-9,
      'cost':0,
    },
       {
      'date':"2022.01.10",
      'item':"C",
      'warehouse':"C",
      'quantity':25,
      'cost':100000,
    },
       {
      'date':"2022.01.11",
      'item':"C",
      'warehouse':"C",
      'quantity':25,
      'cost':120000,
    },
       {
      'date':"2022.01.11",
      'item':"C",
      'warehouse':"C",
      'quantity':25,
      'cost':135000,
    },
       {
      'date':"2022.01.11",
      'item':"C",
      'warehouse':"C",
      'quantity':60,
      'cost':100000,
    },
   
       {
      'date':"2022.01.12",
      'item':"C",
      'warehouse':"C",
      'quantity':-129,
      'cost':0,
    },

       {
      'date':"2022.01.11",
      'item':"C",
      'warehouse':"C",
      'quantity':100,
      'cost':100000,
    },
]
def main():
  date=[]
  sandelis=[]
  preke=[]
  kiekis=[]
  kaina=[]
  vnt=[]
  pkiekis=[]
  for item in range(len(items)): 
    date.append(date1(item))
    sandelis.append(warehouse1(item))
    preke.append(preke1(item))
    kiekis.append(kiekis1(item))
    kaina.append(kaina1(item))
    vnt.append(vnt1(item))
    pkiekis.append(pkiekis1(item))
  for i in range(len(kaina)):      
    for j in range(len(kaina)):
      if kiekis[i]<0:
        if kiekis[j]>=0 and sandelis[j]==sandelis[i] and preke[j]==preke[i]:
            kiekis[j]=calc5(i,j,kiekis)
            if kiekis[j]<0:
              kaina[i]=calc2(i,j,kiekis,kaina,vnt)
              kiekis[i]=calc3(j,kiekis)           
            if kiekis[j]>=0:
              kaina[i]=calc4(i,j,kiekis,kaina,vnt)
              kiekis[i]=bugfix()
              print("Data:",date[i],"preke:",preke[i],"sandelis:",sandelis[i],"kiekis:",pkiekis[i],"Savikaina:",kaina[i])   
main()
                            

               
            


