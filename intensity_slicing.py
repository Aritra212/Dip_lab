import numpy as np

img= open("images/airport_river.pgm","r")
f1=img.readline()
f2=img.readline()
f3=img.readline()
f4=img.readline()

[w,h]=[int (i) for i in f3.split()]
k=np.zeros((h,w),np.int64)
for i in range (h):
    for j in range(w):
        k[i,j]=img.readline()

img.close()


img= open("i_slice.pgm","w")
img.write(f1)
img.write(f2)
img.write(f3)
img.write(f4)

for i in range(h):
    for j in range(w):
      if(k[i,j]>0 and k[i,j]<=90):
         img.write("0\n")
      elif(k[i,j]>90 and k[i,j]<100):
         img.write("%d\n"%k[i,j])
      elif(k[i,j]>=100 and k[i,j]<120):
         img.write("0\n")
      else:
         img.write("%d\n"%k[i,j])