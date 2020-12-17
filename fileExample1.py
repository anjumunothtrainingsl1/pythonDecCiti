# read ; write; append;
# open; perform the op; close
# open -- file; mode (r,w,x, a, t,b,r+ ); encoding -- utf-8
# close

try:
    f=open("sample2.txt",mode="w",encoding="utf-8")
    f.write("This is the first line")
    f.write("\nThis is the second line")
    f.writelines(["This is the third line","\nThis is 4th line"])
except:
    print("Exception occurred during the file operations")

finally:
    f.close()

