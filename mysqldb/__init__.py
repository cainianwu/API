
'''
import re
m = re.search('\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print("1",m.group())

m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print("2",m.group())


s = "asd123\aadasd1\a23"

a = re.search(r'(\a)',s).group(1)
print(a)

'''
