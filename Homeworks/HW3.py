# -*- coding: utf-8 -*-
"""HW3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O92YCrB2hULxY9tzwqQWaTmAF69IJtck
"""

# 1. Altay
Altay = { "name":"Altay", 
         "Midterm" : int(input("Please enter your Midterm Grade Altay ")),
         "Project" : int(input("Please enter your Project Grade Altay ")), 
         "Final" : int(input("Please enter your Final Grade Altay ")) 
       } 
         
# 2. Aybike 
Aybike = { "name":"Aybike",
         "Midterm" : int(input("Please enter your Midterm Grade Aybike ")),                      
         "Project" : int(input("Please enter your Project Grade Aybike ")), 
         "Final" : int(input("Please enter your Final Grade Aybike ")) 
       }  
  
# 3. Alper
Alper = { "name":"Alper", 
         "Midterm" : int(input("Please enter your Midterm Grade Alper ")), 
         "Project" : int(input("Please enter your Project Grade Alper ")), 
         "Final" : int(input("Please enter your Final Grade Alper ")) 
       } 
          
# 4. Hakkıcan
Hakkıcan = { "name":"Hakkıcan", 
         "Midterm" : int(input("Please enter your Midterm Grade Hakkıcan ")), 
         "Project" : int(input("Please enter your Project Grade Hakkıcan ")), 
         "Final" : int(input("Please enter your Final Grade Hakkıcan ")) 
       } 
         
# 5. Ayşe
Ayşe = { "name":"Ayşe", 
         "Midterm" : int(input("Please enter your Midterm Grade Ayşe ")), 
         "Project" : int(input("Please enter your Project Grade Ayşe ")), 
         "Final" : int(input("Please enter your Final Grade Ayşe ")) 
       } 

PG_Altay = Altay["Midterm"] * 0.3 + Altay["Project"] * 0.3 + Altay["Final"] * 0.4
PG_Aybike = Aybike["Midterm"] * 0.3 + Aybike["Project"] * 0.3 + Aybike["Final"] * 0.4
PG_Alper = Alper["Midterm"] * 0.3 + Alper["Project"] * 0.3 + Alper["Final"] * 0.4
PG_Hakkıcan = Hakkıcan["Midterm"] * 0.3 + Hakkıcan["Project"] * 0.3 + Hakkıcan["Final"] * 0.4
PG_Ayşe = Ayşe["Midterm"] * 0.3 + Ayşe["Project"] * 0.3 + Ayşe["Final"] * 0.4

Pass_All = {"Altay" : PG_Altay, "Aybike" : PG_Aybike, "Alper" : PG_Alper, "Hakkıcan" : PG_Hakkıcan, "Ayşe" : PG_Ayşe}
for keys,values in Pass_All.items():
    print(keys,values)

Grade_List = list(Pass_All.values())
Grade_List.sort()
Grade_List [::-1]