def add_side(str):
  temp = str
  for i in range(2):
    if i == 0:
      str += "_a.jpg, "
    else:
      str += temp + "_b.jpg"
  return str

def create_csv():
  print("pepper_id,label,side1,side2")
  
  for i in range(1,109):
    if i < 10:
      pepper_id1 = "P" + "00" + str(i) + ", "
      pepper_id2 = "P" + "00" + str(i)
      entry = pepper_id1 + "mild, " +  add_side(pepper_id2)
      print(entry)
    elif i < 37:
      pepper_id1 = "P" + "0" + str(i) + ", "
      pepper_id2 = "P" + "0" + str(i)
      entry = pepper_id1 + "mild, " +  add_side(pepper_id2)
      print(entry)
    elif i < 73:
      pepper_id1 = "P" + "0" + str(i) + ", "
      pepper_id2 = "P" + "0" + str(i)
      entry = pepper_id1 + "medium, " +  add_side(pepper_id2)
      print(entry)
    elif i < 100:
      pepper_id1 = "P" + "0" + str(i) + ", "
      pepper_id2 = "P" + "0" + str(i)
      entry = pepper_id1 + "hot, " +  add_side(pepper_id2)
      print(entry)
    else: 
      pepper_id1 = "P" + str(i) + ", "
      pepper_id2 = "P" + str(i)
      entry = pepper_id1 + "hot, " +  add_side(pepper_id2)
      print(entry)
  
create_csv()
  

