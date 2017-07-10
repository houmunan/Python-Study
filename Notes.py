# 07/03/2017 Python 001                                                                                                 # 07/03/2017 Python 001
print("Hello World.")

'''笔记

视频地址：
https://www.youtube.com/watch?v=N0lxfilGfak

三个单引号之间的字符全算作注释。和#一样的注释写法。单引号之间句尾加/n似乎也是注释写法。就算句尾无/n也是注释，但当点击回车换行的时候，格式会不一样。

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


# 07/06/2017 Python 001                                                                                                 # 07/06/2017 Python 001


# Six Datatype (3 Immutable, 3 Mutable)

'''
Immutable(不可变，固定的，fixed): Numbers, Strings, Tuples
Mutable(可变的):Lists, Dictionaries, Sets

List写法：
    >>> x=[1,2,3,4,5]
    >>> x
    [1, 2, 3, 4, 5]
    
    
'''

