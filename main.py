import os
from git import Repo

#Download repositories

sourceFile = 'source.txt'
source = open(sourceFile, 'r')
for line in source:
    repoDir= line.rsplit("/")[-1].rsplit(".")[0]
    print("Cloning" + line + " in " + repoDir)
    os.system('git clone ' + line)
    #Repo.clone_from(line, repoDir)

result = open ("results.txt", "a+")
for root, dirs, files in os.walk("."):
   for name in files:
       if "app.config" in name:
           x = os.path.join(root, name)
           print(x)
           f = open(x,"r")
           for line in f:
               if "Framework" in line:
                   temp = line
                   result.write(line.rstrip() + " Found in " + x + "\n")
                   print("line written in file")
