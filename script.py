import os, random

def rename_all_slideshow():
    directorypath = r'./images/story'
    allfiles = os.listdir(directorypath)
    numoffiles = range(len(allfiles))
    random.shuffle(numoffiles)
    for i,each in enumerate(allfiles):
        os.rename(directorypath + r'/' + each, directorypath + r'/image{}.jpg'.format(str(numoffiles[i])))



if __name__ == '__main__':
    rename_all_slideshow()