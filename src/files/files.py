import random
num = random.randint(1,10)
fo = open("input.txt","r+")
content = fo.readlines()
print(content[num-1])
fo.close()
answer = input("What is your response to the question?")
fi = open("output.txt", "a+")
fi.write(content[num-1]+answer+"\n_________________\n")
fi.close()