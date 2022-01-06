

# Method 1
# Time Complexity: O(n^2)

def check_anagram(string1, string2):
    
    if len(string1) != len(string2): return False

    string1 = sorted(string1)
    string2 = sorted(string2)

    for i in range(len(string1)):
        if not string1[i] == string2[i]:
            return False
    
    return True


# string1 = "ass"
# string2 = "aas"
# print(check_anagram(string1, string2))


# Method 2
# Time Complexity: O(n log n)

def check_anagram_01(string1, string2):
    if len(string1) != len(string2): return False

    counts= [0 for i in range(126)]

    for i in range(len(string1)):
        counts[ord(str(string1[i]))] +=1
        counts[ord(str(string2[i]))] -=1
    
    for count in counts:
        if count != 0:
            return False
    
    return True


string1 = "ass"
string2 = "ass"
print(check_anagram_01(string1, string2))
