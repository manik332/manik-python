import os,glob
os.chdir("PYTHON")
for file in glob.glob(("*.txt")):
    print(file)