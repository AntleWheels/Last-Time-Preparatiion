string1 = "cork"
string2 = "rock"
if len(string1) != len(string2):
    print("Not anagram")
else:
    count =0
    for i in string1:
        for j in string2:
            if i == j:
                count += 1
    if count == len(string1):
        print("Anagram")
    else:
        print("Not anagram")
