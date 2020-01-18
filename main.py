import os

results = {}
result = open ("results.txt", "a+")
for root, dirs, files in os.walk("."):
   for name in files:
       if "app.config" in name:
           x = os.path.join(root, name)
           f = open(x,"r")
           for line in f:
               if "Framework" in line:
                   temp = line
                   result.write(line + " Found in " + x + "\n")
