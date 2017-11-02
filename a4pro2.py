value="ayse tatile cikti"
finalMessage=""
for x in range(0,len(value)):
    if ord(value[x]) in range(97,123):
        finalMessage+=(chr(((ord(value[x])-84)%26)+97))
    elif ord(value[x]) in range(65,91):
        finalMessage+=(chr(((ord(value[x])-64)%26)+65))
    else:
        finalMessage+=value[x]
print(finalMessage)
