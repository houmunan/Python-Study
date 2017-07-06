# 07/03/2017 Python 001                                                                                                  #07/03/2017 Python 001
print("Hello World.")

'''笔记
Github and Git
Push to Github, always create, commit & push local repository to server by Github Client!!!!!!先用GitHub客户端Push一遍之后在PyCharm和其他地方才能正常Push不然无法读取远程Repoitory!!!

关于Bitwise和Two's Complement Transformation.
Two's Complement https://en.wikipedia.org/wiki/Two%27s_complement
    "The sum of a number and its two's complement will always equal 0 (since the last digit is truncated), and the sum of a number and its one's complement will always equal -0."

理解："In two's-complement representation, positive numbers are simply represented as themselves, and negative numbers are represented by the two's complement of their absolute value."
二进制直接转化到10进制（把10进制考虑成释义），比如说 011=3， 010=2， 111=7，0111 1111=127，1111 1111=255，是这样，但这样没法表示负数。所以现在无论是几个bit组成的二进制数，都把做左边一个保留来表达正负，0为正，1为负；因为牵扯到0000 0000是0但1111 1111不能是-0只能是-1。比如1111 1111按二进制算原本是255，但现在用1111 1111代表一个负数，这个负数覆盖了255这个原本含义，于是1111 1111从此不再是255了；换算方法就是Two's complement。Two's complement是对“一个负bit数字代表的是哪个负的正数？”这个问题的解释，虽然本身是一种运算，但没有运算的意义，所以不当成运算. 所以叫“Two's-complement representation”而不是“Two's-complement transformation”。具体法则如下：
     例：0111 1111=127，其two's complement，因为自己是正数，所以就是自己，不需要换算，还是127.
        ！！！！！！！！！划重点！！！！！！！！！虽然没有意义，但是0111 1111=127也是有Two's-complement transformation的，只不过是把一个正数转换成负数了，-127-1=-128，没有现实意义。
     例：1000 0000原本(Unsigned Value)是代表130的。现在，two's complement是，对应的0111 1111（每个bit都0，1转换）所代表的正数，即127，的-x-1，即-127-1=-128。于是1000 0000现在不再代表130，而是代表-128。
     例；1111 1110原本代表254。现在，two's complement是对应的0000 0001所代表的正数1的-x-1，即-1-1=-2。于是1111 1110不再是254，而是-2.
Two's Complement的优势：
    0是唯一的，没有+0和-0的冲突。
    "The sum of a number and its two's complement will always equal 0 (since the last digit is truncated)"例：1111 1111=-1，0000 0001=1；1111 1111 + 0000 0001 = 1 0000 0000，而最左边的1溢出被删了，所以结果剩下0000 0000=0。从含义上来讲（用Two's Complement representation），1(0000 0001) + -1(1111 1111) = 0；从binary原理上来讲，1111 1111 + 0000 0001 = 0000 0000；这样就同时符合了数学运算原理和计算机二进制运算的原理。
以上
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

print('Num4 right shift by 2 = ', num4>>2)
print('Num5 left shift by 2 =', num5<<2)
print('426 right shift by 4 = ', 426>>4, '始终等于', '426 / 2 ** 4', 426/2**4, '去掉小数点后的位数')
print('6 left shift by 3 =', 6<<3, '始终等于', '6 * 2 **3 =', 6*2**3)

'''Left Shift (<<<) and Right Shift(>>>)
是把被操作的十进制数字的二进制形式往左右移动几个bit。左移就是往右添0，右移就是直接划掉右侧几位。
注意到有趣的点，如上面的“始终等于”所述：
     二进制位数的左移x位，等于在二进制数右侧加上x个0，等于这个数的10进制形式乘以2的x次方；
     而右移等于这个数的10进制形式除以2的x次方取整，因为右移基本会抹掉最右边的几个1。
以上。
'''

print('Returns the complement of Num4:', ~num4)
print('Returns the complement of 99:', ~99)
print('Returns the complement of 25536:', ~25536)
'''Return Complement (~x)
This is always equal to -x-1. In Binary, it turns every 1 to 0, and every 0 to 1.
    注：此处参考笔记开头Two's Complement Transformation部分标有划重点的部分
以上。
'''
# Identity Operator                                                                                                      #Identity Operator

# Membership Operator                                                                                                    #Membership Operator
