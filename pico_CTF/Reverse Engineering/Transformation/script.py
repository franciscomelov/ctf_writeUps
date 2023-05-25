

encoded ="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
partial_flag= "pcCF1_isis3do__549b"
original_flag=""
for i in range(0, len(encoded)):
    encoded_char = ord(encoded[i])
    known_letter = partial_flag[i]

    first_char = known_letter
    second_char = chr(encoded_char - (ord(known_letter) << 8))
    original_flag += first_char + second_char

print(original_flag)




