
# a =set()
# with open('text.txt') as f:
#     for i in f.read():
#         a.add(i)
#     print(a)
#aeilqtuy
f= [2,3,4]
b = {'l', '&', '%', '<', '*', '-', 'u', '#', '\n', 'e', 
     'q', '$', ')', 'i', '{', '}', '[', '+', '^', 'a', 't', 
     '!', '@', ']', '>', '(', 'y', '_'}
#print(chr(ord('&')+2))

v = list(map(lambda x: chr(ord(x)+2),b))
print(v)