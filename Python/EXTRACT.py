import glob,os
import requests
directory = "."
os.chdir(directory)
files = [file for file in glob.glob("*.py")]
print(files)
count = 0 
errors = []
for i in files:
    link = "https://www.codechef.com/problems/{}".format(i.strip(".py"))
    request = requests.get(link)
    if request.status_code == 200:
        print("- [{}](https://www.codechef.com/problems/{})\n".format(i.strip(".py"),i.strip(".py")))
    else: 
        count += 1
        errors.append(i) 
print("Error Count {}".format(count))
print(errors)