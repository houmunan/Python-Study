# 07/03/2017 Python 001                                                                                                 # 07/03/2017 Python 001
print("Hello World.")

'Six Operators, 六种 Operators'


# Arithmetic Operators                                                                                                  # Arithmetic Operators
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


# Assignment Operators                                                                                                  # Assignment Operators
num3 = num1 + num2
# print(num3)
num3 = num3 + num2  # 累加
# print(num3)
num3 += num2  # 相当于上一句，累加
# print(num3)


# Comparison Operator                                                                                                   # Comparison Operator
print("Is Num3 > Num2 ?", num3 > num2)
print("Is Num3 = Num2 ?", num3 == num2)
print("Is Num3 != Num2 ?", num3 != num2)

'''
和“is”以及“is not”，即后面的Identity Operator似乎作用没有区别。
'''

# Logical Operator                                                                                                      # Logical Operator
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

# Bitwise Operator                                                                                                      # Bitwise Operator
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

# Identity Operator                                                                                                     # Identity Operator
'''
    >>> x = 5
    >>> x is 5
    True
    >>> x is not 5
    False
    >>> x = 'gg'
    >>> x is not 'gg'
    False
    >>> x is 'gg'
    True
似乎跟前面“==”，“!=”，即Comparison Operator是一个东西，有一样的作用。“==”，“!=”后面也可以连着字符，不一定是数字。
'''

# Membership Operator                                                                                                   # Membership Operator
'''
验证in和not in前面的（数字，字符等）是不是在其后的（list，字符串等）里
    >>> x = [1,2,3,4,5]
    >>> 3 in x
    True
    >>> 3 not in x
    False
    >>> x = 'ghost'
    >>> 'g' in x
    True
    >>> 't' not in x
    False
'''



# 07/06/2017 Python 001                                                                                                 # 07/06/2017 Python 001


# Sequence Operations:                                                                                                  # 对各类不同数据的各种操作，有公用的，有面对特定类型数据的。

##########String数据类型##########                                                                                       # String
                                                                                                                        #  对String类型的data的操作：组合，重复，返回片段，索引，寻找，
                                                                                                                        # 替换，按特定符号切分成list，数出现次数，换大小写，按字母表找
                                                                                                                        # 最前最后的字母如a和z，判断是否是英文字母等。
#公用部分，包括但不限于String类型

## Concatenation
'Python' + 'Tutorial' #返回'PythonTutorial'。无空格'

## Repetation
'Python'*2            #返回'PythonPython'。无空格'

## Slicing
string1 = 'Python'
string1[2:2] #返回null''
string1[2:3] #返回't'
string1[2:4] #返回'th'
string1[0]   #返回'P'

'''
研究发现，
    2:2，2:3，2:4等，可以理解为字符串中字母之间的缝隙，而字符串之前的缝隙是0，如2:3就是yt之间到th之间，所以是t
    而单个数字，如0，1，2，-1，是把第一个字母P当成第0个，y第一个，一次类推；负数-1代表最后一个n。详细在下面Indexing
以上
'''

## Indexing
string1 = 'Python'
string1[0]  #返回'P'
string1[1]  #返回'y'
string1[-1] #返回'n'


# Type Specific Method,只对String类型的数据的                                                                             # Type Specific Method

## find()
str = 'Python'
str.find('th') #返回2

## replace()
str = 'Python'
str.replace('thon','THON') #返回'PyTHON'

## split
str = 'P, y, t, h, o, n'
str.split(',') #返回['P', ' y', ' t', ' h', ' o', ' n']，为List

## count
str = 'Python'
str.count('Python',0,len(str)) #返回1。len()长度。
str.count('th',0,5)            #返回1
str.count('Python',0,-1)       #返回0
str.count('Pytho',0,-1)        #返回1

## upper()
str = 'Python'
str.upper() #返回'PYTHON'。

## max() min()
str = 'Python'
max(str) #返回'y'。
min(str) #返回'P'。
str = 'Python0,'
max(str) #返回'y'。
min(str) #返回','。
str = 'Python0'
max(str) #返回'y'。
min(str) #返回'0'。

'''
按字母表顺序，min()找排最前的字母，max()找最后面的字母。
     大写字母靠前，小写字母靠后。数字靠大写字母前面，再前面是乱七八糟符号大概。
以上。
'''

##isalpha()
str='Python'
str.isalpha() #返回True
str='Python?'
str.isalpha() #返回False

'''
判断是不是全都是字母
'''


##########Tuple(多元组)类型的数据和相关操作##########                                                                       # Tuple(多元组)

'''
顾名思义，多元组是多种不同Immutable类型变量的组合。其不可modify，比较于list的中括号[,,,]，Tuple用小括号(,,,)。
“A Tuple is a sequenceof immutable Python objects like floating number, string literals, etc.”
“The tuples can't be changed, unlike lists.”
“Tuples are defined using curve braces.”
'''

myTuple = ('Yukiho', 2.4, 5, 'Python')
print(myTuple)  # 返回('Yukiho', 2.4, 5, 'Python')

#公用部分

## Concatenation
tup = ('a','b','c')
tup + ('d','e')     #返回('a', 'b', 'c', 'd', 'e')

## Repettion
tup = ('a','b','c')
tup * 2     #返回('a', 'b', 'c', 'a', 'b', 'c')

## Slicing
tup = ('a','b','c')
tup[1:2]     #返回('b',)，没错总有至少一个逗号
tup[1:3]     #返回('b', 'c')
tup[0:3]     #返回('a', 'b', 'c')

## Indexing
tup = ('a','b','c')
tup[0]     #返回'a'，没错，没括号了，不是Tuple了，剩下一个string了。

'''
其他特别部分省略了
'''


##########Lists类型的数据和相关操作##########                                                                              # List

'''
和Tuple相对的存在，是多种不同utable类型变量的组合。其不可modify，比较于list的中括号[,,,]，Tuple用小括号(,,,)。
“A List is a sequenceof immutable Python objects like floating number, string literals, etc.”
“Lists can be modified.”
“用中括号[]”
'''

myList = ['Yukiho', 2.4, 5, 'Python']
print(myList)  # 返回['Yukiho', 2.4, 5, 'Python']
'''公用部分省略，四项相同'''

# Type Specific Method,只对List类型的数据的                                                                               # Type Specific Method

## append(value),往list最后加一个值
list = [1, 'a', 2.5]
list.append('d')
list    #返回[1, 'a', 2.5, 'd']
'''往list最后加一个东西'''

## extend(list),往list最后加一个list,一串值
list = [1, 'a', 2.5]
ext_list = ['c', 'd']
list.extend(ext_list)
list    #返回[1, 'a', 2.5, 'c', 'd']
list = [1, 'a', 2.5]
list.extend(['e', 'f'])
list    #返回[1, 'a', 2.5, 'e', 'f']
'''往list最后加一个list'''

## insert(index, value)
list = [1, 'a', 2.5]
list.insert(2, 'b')
list    #返回[1, 'a', 'b', 2.5]
list = [1, 'a', 2.5]
ext_list = ['c', 'd']
list.insert(2, ext_list)
list    #返回[1, 'a', ['c', 'd'], 2.5]
list = [1, 'a', 2.5]
list.insert(2, 'c', 'd')
list    #返回TypeError: insert() takes exactly 2 arguments (3 given)
'''往index的位置加一个东西。加List或者Tup的话会很奇怪。'''

## pop
list = ['a', 'b', 'c']
list.pop()
list    #返回['a', 'b']
list.pop()
list    #返回['a']
'''Pop的用处：“One by one eliminate from the list. 从最右边开始一个一个删除list里的东西。”'''




##########Dictionaries类型的数据和相关操作##########                                                                       # Dictionary
'''
特征是一一对应，正如字面意义，索引，字典。使用大括号{}。
“Are most flexible built-in data type in Python.
Dictionaries, items are stored and fetched by key, instead of by positional offset.”
一个Dictionary里的Value被Key编码储存，而不是像Tuple或者List一样按Index的顺序。
格式如下：
    myDict = {1:'Munan', 2:'Sakura', 3:'Yukiho', 4:'Asagami'}
    即{Key:Value, Key:Value, ...}
以上。
'''

## Dictionary例子                                                                                                        # Dictionary例子
### Empty Dictionary
myDict = {}

### Dictionary with Integer keys
myDict = {1:'apple', 2:'ball'}
myDict      #返回{1: 'apple', 2: 'ball'}

### Dictionary with mixed keys
myDict = {'name':'John', 1:[2, 4, 3]}
myDict      #返回{'name': 'John', 1: [2, 4, 3]}

### From sequence having each item as a pair
myDict = dict([(1,'apple'), (2,'ball')])
myDict      #返回{1: 'apple', 2: 'ball'}
'''dict()是编写Dictionary的函数，其用法是
    List1 = [(Pair1), (Pair2), ...]
    dict(List1)
以上
'''

### Dictionary操作                                                                                                       # Dictionary

## Accessing Dictionary 读取内容
myDict = {1:'apple', 2:'ball'}
myDict[1]       #返回'apple'

## len() 显示长度
myDict = {1:'apple', 2:'ball'}
len(myDict)     #返回2

## key() 显示Keys (List)
myDict = {1:'apple', 2:'ball'}
myDict.keys()   #返回dict_keys([1, 2])                    ！！！！！！

## values() 显示Value (也是List)
myDict = {1:'apple', 2:'ball'}
myDict.values() #返回dict_values(['apple', 'ball'])       ？！？！？！

## update() Update某个值
myDict = {1:'apple', 2:'ball', 3:'tree', 4:'ocean'}
myDict.update({1:'bad apple', 3:'wood'})
myDict          #返回{1: 'bad apple', 2: 'ball', 3: 'wood', 4: 'ocean'}





##########Sets类型的数据和相关操作##########                                                                               # Set
'''
特征是没有顺序，每个元素必须Unique不能重复，而且必须imutable不能变更。也使用大括号{}。
“A set is an unordered collection of items.
Every element is unique (no duplicates), and must be immutable (which cannot be changed)”
例子如下：
     mySet = {1,2,3,4,5}
'''

#Sets Methods, 操作                                                                                                      # Sets

## Creating
mySet = {1, 2, 3, 3, 3, 3, 3, 4}
mySet       #返回{1, 2, 3, 4}
'''创建Set的时候如果有重复元素，只留一个。'''

## Union
myS1 = {1, 2, 'c'}
myS2 = {1, 'b', 'c'}
myS1 | myS2     #返回{1, 2, 'b', 'c'}
'''基本相当于Merge，不同的放一筐'''

## Intersection
myS1 = {1, 2, 'c'}
myS2 = {1, 'b', 'c'}
myS1 & myS2     #返回{1, 'c'}
'''“&”找相同'''

## Difference
myS1 = {1, 2, 'c'}
myS2 = {1, 'b', 'c'}
myS1 - myS2     #返回{2}
'''减法“-”找不同'''

'''视频到1:09:32'''









# Flow Control