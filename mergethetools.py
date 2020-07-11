def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        line = string[i:i+k]
        new = ""
        for i in line:
            if i not in new:
                new+=i
        print(new)
