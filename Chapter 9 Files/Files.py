# Python can be used to perform operations on a file. (read & write data)
# Types of all files
# 1 . Text Files : .txt, .docx, .10g etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

# syntax: f = open("file_name", "mode")

# f = open(r"C:\Users\sahil\Desktop\Python\Chapter 9 Files\demo.txt", "r")
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


