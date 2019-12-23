import glob,os
directory = "./Beginner"
os.chdir(directory)
files = [file for file in glob.glob("*.py")]
print(files)

for i in files:
    print("- [Link Name](https://www.codechef.com/problems/{})\n".format(i.strip(".py")))