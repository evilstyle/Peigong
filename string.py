name = "Dog"
age = 2
text = " %s今年%d岁"%(name,age)
print(text)
text1="ws{}，sdf{}".format ("dog","12")
print(text1)
name ="dog"
age =23
text2 = f"oh {name},sdf{age}"
print(text2)


a = 10
b = 20
 
if  a and b :
   print ("变量 a 和 b 都为 true")
else:
   print ("变量 a 和 b 有一个不为 true")
 
if  a or b :
   print ("变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("变量 a 和 b 都不为 true")
 
# 修改变量 a 的值
a = 0
if  a and b :
   print ("变量 a 和 b 都为 true")
else:
   print ("变量 a 和 b 有一个不为 true")
 
if  a or b :
   print ("变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("变量 a 和 b 都不为 true")
 
if not( a and b ):
   print ("变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("变量 a 和 b 都为 true")


name="sdf,wer,dsfs"
date= name.