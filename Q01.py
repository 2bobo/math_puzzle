def check_palindrome(check_word):
    check_list = list(check_word)
    for n in range(len(check_list)):
        if check_list[n] != check_list[(n + 1) * -1]:
            return 0
    return 1


for i in range(11, 1000000, 2):
    de = str(i)
    bi = str(bin(i))
    bi = bi.replace("0b", "")
    oc = str(oct(i))
    oc = oc.replace("0o", "")
    # print(de + ":" + bi + ":" + oc)
    if (check_palindrome(de) == 1 and
                check_palindrome(bi) == 1 and
                check_palindrome(oc) == 1):
        print(de + ":" + bi + ":" + oc)
        break
