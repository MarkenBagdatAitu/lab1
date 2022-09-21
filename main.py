import os

directory = "MArkee"
parent = "C:/doci/"
path = os.path.join(parent, directory)

# create a directory
os.mkdir(path)

print("'% s' created" % directory)

# remove a directory
os.rmdir(path)


#update the directory
os.chdir(r"C:/doci/")
os.rename("MissMarken", "MArkee")
print("'% s' renamed" % directory)

print(os.listdir(r"C:/doci/"))

