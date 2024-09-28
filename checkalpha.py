alphabet =["a","b", "c", "d" ,"e", "f", "g", "h" ,"i" ,"j", "k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x", "y","z"]
enter = input("Please enter any character:")
if not alphabet:
    print(alphabet.index(enter),f"This{enter}isn't  the alphabet ")
else:
    print(alphabet.index(enter), f"This {enter}is in the alphabet ")