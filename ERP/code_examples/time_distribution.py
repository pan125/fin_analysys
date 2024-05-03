monday = [
    {"time":"7:00","action":"get up","pan":"environment"},
    {"time":"8:00","action":"breakfast","pan":"health"},
    {"time":"9:00","action":"go to work","pan":"Career"},
    {"time":"10:00","action":"work","pan":"Career"},
    {"time":"11:00","action":"work","pan":"Career"},
    {"time":"12:00","action":"Weekly meeting","pan":"Career"},
    {"time":"13:00","action":"work","pan":"Career"},
    {"time":"14:00","action":"class","pan":"education"},
    {"time":"15:00","action":"class","pan":"class"},
    {"time":"16:00","action":"classy","pan":"Self-development"},
    {"time":"17:00","action":"class","pan":"Self-development"},
    {"time":"18:00","action":"class","pan":"Self-development"},
    {"time":"19:00","action":"dinner","pan":"Family"},
    {"time":"20:00","action":"homework","pan":"education"},
    {"time":"21:00","action":"homework","pan":"education"},
    {"time":"22:00","action":"wash-up","pan":"environment"},
    {"time":"23:00","action":"sleep","pan":"rest"},
 
]
count = 0
for element in monday:
  if element['pan']=='Career':
    count+=1
print(count)
