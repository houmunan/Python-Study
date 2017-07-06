# 07/03/2017 Python 001                                                                                                  #07/03/2017 Python 001
print("Hello World.")

'''笔记
Github and Git
'''

# Arithmetic Operators                                                                                                   #Arithmetic Operators
num1 = 10
num2 = 20
print("Num1 + Num2 =", num1 + num2)
print("Num1 - Num2 =", num1 - num2)
print("Num1 * Num2 =", num1 * num2)
print("Num1 / Num2 =", num1 / num2)
print('5 ** 2 =', 5 ** 2)  # 幂
print("20 % 3 =", 20 % 3)  # 余数
print("22 // 7 =", 22 // 7)  # 整倍数
print("3.8 // 2 =", 3.8 // 2)

# 注释：‘单引号’，“双引号”在Python里没有区别。


# Assignment Operators                                                                                                   #Assignment Operators
num3 = num1 + num2
# print(num3)
num3 = num3 + num2  # 累加
# print(num3)
num3 += num2  # 相当于上一句，累加
# print(num3)


# Comparison Operator                                                                                                    #Comparison Operator
print("Is Num3 > Num2 ?", num3 > num2)
print("Is Num3 = Num2 ?", num3 == num2)
print("Is Num3 != Num2 ?", num3 != num2)

'''三个单引号之间的字符全算作注释，比如下面的命令'''  # Comment, 注释写法
'''
print("Is Num3 > Num2 ?", num3 > num2)
print("Is Num3 = Num2 ?", num3 == num2)
print("Is Num3 != Num2 ?", num3 != num2)
'''

# Logical Operator                                                                                                       #Logical Operator
x = True
y = False
z = True
print("X and Y", x and y)
print("X or Y", x or y)
print("Not X", not x)

print("X and Y and Z", x and y and z)
print("X and Z and Y", x and z and y)

five = 5
two = 2
one = 1
zero = 0

print(five and two and zero)
print(five and zero and two)

'''对Logical Operator的理解：Logical Operator是让我十分困惑的第一个Python的部分。比如 5 and 2，两个实数而已，怎么就有True或者False的分别了？简直莫名其妙。但后来经过反复尝试，最后发现了Python对True和False的定义如下：
首先，首字母大写的“True”和“False”是系统保留的名称，“True”就是True，“False”就是False。首字母小写的“true”“false”不是。
其次，数字“0”，“False”本身和“Null”是False，其他“real, non-false, and non-null values”都是True。
Python对and，or和not的判断过程是“从左往右”。比如说：
    1 and 2 and 0 and 4 and 5，即判断1，2，0，4，5全True才返回True值，否则返回False或者第一个（最左边）为False的值比如0。
        所以结果是0.
    0 or False or 1 or 2，即判断0，False，1，2里只要有一个True则返回True，否则返回最右边的False的值比如0或者False。
        所以结果是1.
以上。
'''

# Bitwise Operator                                                                                                       #Bitwise Operator
num4 = 6  # 110
num5 = 2  # 010
print('Bitwise and =', num4 & num5)
print('Bitwise or =', num4 | num5)
print('Bitwise xor =', num4 ^ num5)  # exclusive or

'''把数字字符转化成二进制0和1，再对一串0和1进行Logical Operator判断
如：seven: 111->7, five: 101->5, two: 010->2
or：seven | five，结果为7
and：seven & five，结果为5
xor：seven ^ five，结果为2
XOR: Exclusive Or, 对比于普通OR（Inclusive OR）：
    OR: (A OR B)意思是A，或者B，或者A和B同时出现则True，AB都False则False。
        (A OR B OR C OR ...)类似。
    XOR:(A OR B)意思是A，或者B，出现其中一个则True，两个都True或两个都False则False。
        (A XOR B XOR C XOR ...n)意思是A,B,C,D,...中有奇数(odd)个True时则True，否则(Even)为False。
        XOR只考虑True的数量，XOR只考虑True的数量，XOR只考虑True的数量；不是False的数量，不是False的数量，不是False的数量。重要的事情说三次。
            考虑n个代表True的圈圈重合的维恩图，所有圈共有的部分：只有重合奇数次的部分才是True。
而Bitwise XOR则是简单地逐个判断二进制Bit；如7(111) XOR 5(101)，逐个判断(11)(10)(11)->(0)(1)(0)，所以结果是2(010)。不足位数，正数用0补足负数用1补足。大概？？
以上。
'''



# Identity Operator                                                                                                      #Identity Operator

# Membership Operator                                                                                                    #Membership Operator
