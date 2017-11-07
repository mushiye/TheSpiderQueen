#encoding=utf-8

# 导入re模块
import re

# # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
# pattern = re.compile(r'hello')
#
# # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
# result1 = re.match(pattern, 'hello')
# result2 = re.match(pattern, 'helloo CQC!')
# result3 = re.match(pattern, 'helo CQC!')
# result4 = re.match(pattern, 'hello CQC!')
#
# # 如果1匹配成功
# if result1:
#     # 使用Match获得分组信息
#     print(result1.group())    #成功
# else:
#     print('1匹配失败！')
#
# # 如果2匹配成功
# if result2:
#     # 使用Match获得分组信息
#     print(result2.group())  #成功
# else:
#     print('2匹配失败！')
#
# # 如果3匹配成功
# if result3:
#     # 使用Match获得分组信息
#     print(result3.group())  #失败
# else:
#     print('3匹配失败！')
#
# # 如果4匹配成功
# if result4:
#     # 使用Match获得分组信息
#     print(result4.group())  #成功
# else:
#     print('4匹配失败！')

# # 匹配如下内容：单词+空格+单词+任意字符
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#
# print("m.string:", m.string)
# print("m.re:", m.re)
# print("m.pos:", m.pos)
# print("m.endpos:", m.endpos)
# print("m.lastindex:", m.lastindex)
# print("m.lastgroup:", m.lastgroup)
# print("m.group():", m.group())
# print("m.group(1,2):", m.group(1, 2))
# print("m.groups():", m.groups())
# print("m.groupdict():", m.groupdict())
# print("m.start(2):", m.start(2))
# print("m.end(2):", m.end(2))
# print("m.span(2):", m.span(2))
# print(r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3'))

# 将正则表达式编译成Pattern对象
# pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
# search方法与match方法极其类似，区别在于match()函数只检测re是不是在string的开始位置匹配，
# search()会扫描整个string查找匹配，match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回None。
# match = re.search(pattern,'hello world!')
# match1 = re.match(pattern,'hello world!')
# if match:
#     # 使用Match获得分组信息
#     print(match.group())
#
# pattern = re.compile(r'\d+')
# print(re.split(pattern,'one1two2three3four4'))
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print(m.group(),)

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print(re.sub(pattern, r'\2 \1', s))
print(re.subn(pattern, r'\2 \1', s))

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print(re.sub(pattern, func, s))
print(re.subn(pattern, func, s))