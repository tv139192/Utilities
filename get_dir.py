
import os 
import os.path 
def dir_list (inpath, dirlisting) : 
  print ("input path (0)". format (inpath) ) 
  if not os path. exists (inpath) : 
    print ("input path 10} doesn't exist". format (inpath) ) 
    return None 
  dirlist=os. listdir (inpath) 
  onlydir =[os.path.join (inpath, f)  for f in dirlist if os path.isdir (os.path.join(inpath, f))]
  for i in onlydir: 
      if i not in dirlisting: 
           dirlisting. append (i) 
  while (len (onlydir) > 0) : 
    dir list (onlydir.pop () ,dirlisting)
  
  #print ("path (0) directory names (1)". format (inpath, onlydir) ) 
   return None 

pathlist=[] 
dir_list ('/tmp/', pathlist) 
print (" (1) (0}". format (pathlist, len (pathlist)))
