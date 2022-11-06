# Area of a planar polygon

# For correct answer, vertices have to be ordered sequentially CCW or CW (not randomly).

def area(x1,y1,x2,y2,x0,y0): # area of a triangle
# x0,y0 = ref. point; x1,y1 = 1st point; x2,y2 = 2nd point
 xx1=x1-x0; yy1=y1-y0; xx2=x2-x0; yy2=y2-y0
 a=(xx1*yy2-xx2*yy1)/2
 return a
 
from math import *
x=[0]*100; y=[0]*100
 
while True:
 n=int(input('Number of vertices: n='))
 
 while n < 3:
  print('n is smaller than 3...')
  n=int(input('Number of vertices: n='))
  if n > 2:
    break
 xr,yr=map(float,input('Reference point xr,yr=').split())

 for i in range(0,n):
  print('Vertex no. i=',i)
  x[i],y[i]=map(float,input('Vertex: xi,yi=').split())
  x[n],y[n]=x[0],y[0]
  s=0
 for i in range(0,n):
  ta=area(x[i],y[i],x[i+1],y[i+1],xr,yr)
  s=s+ta
  print('Triangle no. =',i,'Area of triangle=',ta)
  print('Area of polygon: s=',abs(s))
