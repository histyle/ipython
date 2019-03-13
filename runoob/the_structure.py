list = [66.25, 333, 333, 1, 1234.5]
a = [1,2,3,4,5]

#list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.append(12313)

#list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.extend(a)

#删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.remove(5)

#从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。
list.pop(-1)

#移除列表中的所有项
#list.clear()

#返回列表中第一个值为 x 的元素的索引
print(list.index(3))

#返回 x 在列表中出现的次数。
print(list.count(3))

#对列表中的元素进行排序。
list.sort()
print(list)

#倒排列表中的元素。
list.reverse()
print(list)

#返回列表的浅复制
blist = list.copy()
print(blist)


'''
将列表当做堆栈使用
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来

后进先出
'''

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())


'''
将列表当作队列使用
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

先进先出
'''
print("++++++++++++++++++++++++++++++++++++++")
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leavesqueue                           
print(queue)                    # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

#列表推导式
xlist = [3*x for x in [1,2,3,4]]
print(xlist)

#元表
#元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的
t = 12345, 54321, 'hello!'
print(t[0])


#集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

aset = set("1,2,3,4,5 6")
print(aset)
bset = set({1,2,3,4,44,2})
print(bset)

#字典
tel = {'jack': 4098, 'sape': 4139}
print(tel["jack"])