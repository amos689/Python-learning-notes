# 字典是键值对之间的无序集合，由{}或者dict()创建
'''
字典类型函数及其操作方法1

del d[k]        删除d中第k个键值对
k in d          判断k是否在d中
d.keys()        返回d中所有键的信息
d.values()      返回d中所有值的信息
d.items()       返回d中所有键值对的信息
'''
dic1 = {}
dic1['Age'] = 8
dic1['School'] = "菜鸟教程"
print(dic1.keys(),type(dic1.keys()))
print(dic1.items())
dic1['School'] = 'HAUT'
del dic1['Age']
print(dic1.items())

'''
字典类型函数及其操作方法2

d.get(k,<default>)      键k存在，则返回k对应的值，不存在则返回<default>的值
d.pop(k,<default>)      键k存在，则取出k对应的值，并删除k元素，不存在则返回<default>的值
d.popitem()             从字典中随机取出一个键值对，以元组形式返回
d.clear()               清除一个字典
len(d)                  返回字典的长度
'''
d2 = {'中国': '北京', '美国': '华盛顿', '俄罗斯': '莫斯科'}
print(d2.get('中国', 'errorinput'))
print(d2.get('日本', 'errorinput'))
print(d2.pop('美国', 'errorinput'))  # 美国被调出后被删除
print(d2.items())
print(len(d2))
d2.clear()
dic1.clear()
print(d2)

# 综合练习：用字典记录学生成绩并分级
students = {}
write = 1
while write:
    name = str(input('输入名字:'))
    grade = int(input('输入分数:'))
    students[str(name)] = grade
    write = int(input('继续输入？\n 1/继续  0/退出'))
print('name  rate'.center(20, '-'))
for key, value in students.items():
    if value >= 90:
        print('%s %s  A'.center(20, '-') % (key, value))
    elif 89 > value >= 60:
        print('%s %s  B'.center(20, '-') % (key, value))
    else:
        print('%s %s  C'.center(20, '-') % (key, value))

# 字典是支持无限极嵌套的，如下面代码：
cities = {
    '北京': {
        '朝阳': ['国贸', 'CBD', '天阶', '我爱我家', '链接地产'],
        '海淀': ['圆明园', '苏州街', '中关村', '北京大学'],
        '昌平': ['沙河', '南口', '小汤山', ],
        '怀柔': ['桃花', '梅花', '大山'],
        '密云': ['密云A', '密云B', '密云C']
    },
    '河北': {
        '石家庄': ['石家庄A', '石家庄B', '石家庄C', '石家庄D', '石家庄E'],
        '张家口': ['张家口A', '张家口B', '张家口C'],
        '承德': ['承德A', '承德B', '承德C', '承德D']
    }
}
for i in cities['北京']:
    print(i)
print('\n\n')
for i in cities['北京']['海淀']:
    print(i)