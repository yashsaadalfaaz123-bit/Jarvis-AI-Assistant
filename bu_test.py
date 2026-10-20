import difflib
name_find=input("Enter find name: ")
found=False
with open("Costomer.txt","r") as f:
   e= f.read ()
   

   f=e.splitlines()

   names=[]
   for i in f:
      r = i.split(",")
      print()
      o=r[0].split(":")
      print(o)
      name=o[1].strip()
   
      names.append(name)
      r = i.split(",")
      print()
      o=r[1].split(":")
      print(o)
      phone=o[1].strip()
          
print(len(f))
print(names)
matches = difflib.get_close_matches(name_find, names, n=len(names), cutoff=0.5)
print(matches)
phon_find=input("costamer ka phon number batayo: ")
for i in f:
     r = i.split(",")
     print()
     o=r[1].split(":")
     print(o)
     phone=o[1].strip()
            
   



if(name in matches):


  
   
      
      