# -*- coding: utf-8 -*
import random
symbol='○'
operate=["+", "-"]
qs1=""
p=["b__" , "__ā" , "b__" , "b__" , "__ǐ" , "b__" , "l__" , "__ě" , "__ì" , "l__" , "__ì" , "__è" , "__ǐ" , "m__" ,"m__" , "m__" , "__ǎ" , "__ā" , "t__" , "n__" , "n__" , "__ě" , "__à" , "__à" ]
h=                  ["爸" , "巴" , "把" , "八" , "比" , "不" , "乐" , "了" , "里" , "力" , "立" , "么" , "米" , "木" , "目" , "妈" , "马" , "他" , "土" , "你" , "女" , "可" , "怕" , "大" ]
print len(p)
print len(h)
def cm():
    syb=operate[random.randint(0, 1)]
    num1=random.randrange(11)
    if syb == "-":
        return  str(num1)+syb+str(random.randrange(num1+1))
    return str(random.randrange(1,11))+syb+str(random.randrange(11))
for x in range(6):
    if x in (3, 4, 5):
        qs1 += cm()+symbol+cm()+" "
    else:
        qs1 += str(random.randint(0, 10))+symbol+str(random.randint(0, 10))+" "
print qs1;
qs1=""
for x in range(3):
   for y in range(8):
     qs1 += cm()+"= "
   print qs1
   qs1 = ""
list1=range(22)
random.shuffle(list1)
qs1=""
qs2=""
for x in list1:
    qs1 += p[x]+" "
    qs2 += h[x]+" "
print qs1
print qs2