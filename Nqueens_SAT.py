# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:41:12 2021

@author: MAEVA

"""

n = input("Enter n: ")
n = int(n)
if n < 4:
  print("UNSATISFIABLE")
  exit()
count=0 # count clauses number
constraints="constraints.cnf"
constraints_file= open(constraints,"w");

#generator rule
for i in range(0,n):
 str0='';
 for j in range(1,n+1):
  number=str(j+n*i);
  str0=str0+number+" "
 str0=str0+" 0\n"
 constraints_file.write(str0);
 count+=1

#constraints on rows
for i in range(0,n):
 for j in range(1,n):
   number=j+n*i;
   for l in range(1,n-j+1):
    str0="-"+str(number)+" -"+str(number+l)+" 0\n"
    constraints_file.write(str0);
    count+=1

#constraints on columns
for j in range(1,n+1):
 for i in range(0,n):
   number=j+n*i;
   for l in range(1,n-i):
    str0="-"+str(number)+" -"+str(number+n*l)+" 0\n"
    constraints_file.write(str0);
    count+=1 

#constraints on left to right diagonal
# part 1, upper bound triangle
for i in range(0,n-1):
 for j in range(i,n-1):
  number=j+1+n*i;
  for l in range(1,n-j):
    str0="-"+str(number)+" -"+str(number+l*(n+1))+" 0\n"
    constraints_file.write(str0);
    count+=1 

# part 2, lower bound triangle
for i in range(0,n-1):
 for j in range(0,i):
  number=j+1+n*i;
  for l in range(1,n-i):
   str0="-"+str(number)+" -"+str(number+l*(n+1))+" 0\n"
   constraints_file.write(str0);
   count+=1

#constraints on right to left diagonal
# part 1, upper bound triangle
for i in range(0,n):
 for j in range(0,n-i):
  number=j+1+n*i;
  for l in range(1,j+1):
   str0="-"+str(number)+" -"+str(number+l*(n-1))+" 0\n"
   constraints_file.write(str0);
   count+=1

# part 2, lower bound triangle
for i in range(0,n):
 for j in range(n-i,n):
  number=j+1+n*i;
  if (number != n*n ):
   for l in range(1,n-i):
    str0="-"+str(number)+" -"+str(number+l*(n-1))+" 0\n"
    constraints_file.write(str0);
    count+=1

constraints_file.close()
