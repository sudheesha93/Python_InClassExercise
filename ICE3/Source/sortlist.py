items=input("enter the words seperated by commas")
words=[word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))