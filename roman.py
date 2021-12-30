s = input()
roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
number = 0
for i in range(0, len(s) - 1):
    if roman[s[i]] < roman[s[i+1]]:
        number -= roman[s[i]]
    else:
        number += roman[s[i]]
print(number + roman[s[-1]])