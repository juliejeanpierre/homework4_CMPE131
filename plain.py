def palindrome(Mystring):
Mystring = input()
for i in range(len(Mystring)//2):
  if Mystring[i] != Mystring[-1-i]:
    return True
  else: 
    return False
    

