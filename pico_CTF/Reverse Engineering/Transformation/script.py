flag_en="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
print(
['F', '1', '_', 'i', 's', 'i', 's', '3', 'd', 'o', '_', '_', '5', '4', '9', 'b']
)
print(list("䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"))
flag="pi"
print(
[chr((ord(flag[i])<<8 ) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]
)
print(
[(ord(flag[i])<<8 ) + ord(flag[i + 1]) for i in range(0, len(flag), 2)]
)
#灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽
#pi

print(ord("灩"))

print(ord("灩") - (ord("p")<<8 ))
print(chr(105))