monday = [
    {"time":"7:00","action":"Morning exercises","spheare":"Health"},
    {"time":"8:00","action":"Finance planning","spheare":"Finances"},
    {"time":"9:00","action":"Week planning","spheare":"Career"},
    {"time":"10:00","action":"Report preparation","spheare":"Career"},
    {"time":"11:00","action":"Report preparation","spheare":"Career"},
    {"time":"12:00","action":"Weekly meeting","spheare":"Career"},
    {"time":"13:00","action":"Math of Economics","spheare":"Career"},
    {"time":"14:00","action":"Math of Economics","spheare":"Career"},
    {"time":"15:00","action":"Language study","spheare":"Self-development"},
    {"time":"16:00","action":"Language study","spheare":"Self-development"},
    {"time":"17:00","action":"Master class for Product management","spheare":"Self-development"},
    {"time":"18:00","action":"Time with family","spheare":"Family"},
    {"time":"19:00","action":"Time with family","spheare":"Family"},
    {"time":"20:00","action":"Football","spheare":"Health"},
    {"time":"21:00","action":"Football","spheare":"Health"},
    {"time":"22:00","action":"Bar after football","spheare":"Environment"},
    {"time":"23:00","action":"Bar after football","spheare":"Environment"},
    {"time":"00:00","action":"","spheare":"Free"}
]
count = 0
for element in monday:
  if element['spheare']=='Career':
    count+=1
print(count)