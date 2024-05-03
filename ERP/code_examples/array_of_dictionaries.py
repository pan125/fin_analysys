life_balance1={"spheare":"Career","dream":"Dream for career","points":8,"goal":"closest goal for career"}
life_balance2={"spheare":"Family","dream":"Dream for Family","points":7,"goal":"closest goal for Family"}
life_balance3={"spheare":"Finances","dream":"Dream for Finances","points":6,"goal":"closest goal for Financesreer"}
life_balance4={"spheare":"Environment","dream":"Dream for Environment","points":9,"goal":"closest goal for Environment"}
life_balance5={"spheare":"Self-development","dream":"Dream for Self-development","points":5,"goal":"closest goal for Self-development"}
life_balance6={"spheare":"Rest","dream":"Dream for Rest","points":7,"goal":"closest goal for Rest"}
life_balance7={"spheare":"Traveling","dream":"Dream for Traveling","points":9,"goal":"closest goal for Traveling"}
life_balance8={"spheare":"Health","dream":"Dream for Health","points":10,"goal":"closest goal for Health"}

life_balance=[]
life_balance.append(life_balance1)
life_balance.append(life_balance2)
life_balance.append(life_balance3)
life_balance.append(life_balance4)
life_balance.append(life_balance5)
life_balance.append(life_balance6)
life_balance.append(life_balance7)
life_balance.append(life_balance8)
print(life_balance)
# points for finances
# If I know that finances under number 2
print(life_balance[2]["points"])

# If I know that number of elements with finance 
for element in life_balance:
  if element["spheare"]=='Finances':
    print(element["points"])
