import os
import time

while True:
  os.system("cp -f ../../pySense/*.png .") 
  os.system("cp -f ../../pySense/*.ico .")
  os.system("cp -f ../../pySense/*.html .")
  os.system(" git add . ; git commit -m \".\" ; git push")
  time.sleep(60)
  print "sleep for %d" % sleep_
