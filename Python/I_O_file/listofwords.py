words = ["Rauf", "hassan"]

with open("Data.txt") as f:
   content =  f.read()
   for word in words:
      if(word in content):
        content = content.replace(word , "*"*len(word))
     
   
with open("Data.txt","w") as w:
   w.write(content)