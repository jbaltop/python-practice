# p233

poem = """There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night."""

fout = open("output/relativity", "wt", encoding="utf-8")
print(poem, file=fout, sep="", end="")
fout.close()
