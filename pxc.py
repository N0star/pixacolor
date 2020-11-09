# FDC # PXC # 1.0.0 # 2020

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import numpy as np

def upload(name):           #get an image
    img = mpimg.imread(name)
    tab = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            tab.append(img[i][j])
    return tab, img

def minipix(xx,cc,idx):     #reduce the colours
    for i in range(len(xx)):
        xx[i]=cc[idx[i]]
    return xx

def download(xx,pic):       #prepare to save
    l1=len(pic[0])
    l=len(pic)
    pic = []
    for i in range(l):
        pas = []
        for j in range(l1):
            pix=xx[i*l1+j].astype(int)
            pas.append(pix)
        pic.append(pas)
    return pic


def kc_init(xx, k):         #init k-index centroids
    ridx = np.random.permutation(len(xx))
    ctrd = xx[:k]
    return ctrd

def find_cc(xx, cc):        #find closest values
    indx = []
    for i in range(len(xx)):
        mval = 9999;
        indx.append(0)
        for j in range(len(cc)):
            val = xx[i]-cc[j];
            val = np.linalg.norm(val)**2;
            if val<mval:
                mval=val;
                indx[i]=j;
    return indx

def ccc(xx,idx,k):          #update centroids
    cc = []; c = [];
    for i in range(k):
        col = np.array([])
        for j in range(len(xx[i])):
            col=np.append(col,0)
        cc.append(col)
        c.append(0)

    for i in range(len(idx)): #idx==xx
        cc[idx[i]]+=xx[i]
        c[idx[i]]+=1

    for i in range(k):
        cc[i]/=c[i]
    return cc

def setting():
    name = input("Image name: ")
    tab = []; pic = [];
    f = 0; n = 0; k = 0;
    try:
        tab,pic = upload(name)
    except FileNotFoundError: f=1;
    print("table size: ",len(tab))
    n = input("Number of interations (int): ")
    k = input("Number of colours (int): ")
    n = int(n); k = int(k)%256;
    print("File: ",name,", k=",k,", n=",n)
    ch = input("Is this data correct? (Y/n): ")
    if(ch=='Y' or ch=='y'):
        if(f): print("File not found...")
        else: pass
    else: f=1;
    return f,tab,pic,n,k;
                
#tab, pic = upload("Homare.jpeg")
#k=8; tab = tab[:1000] # testing
print("Welcome to Pixacolor!")
while True:                         # main menu # MAIN LOOP #
    ch=input("u - upload, s - save,\ni - info, q - quit.\n\n")
    if(ch=='q'): break;
    elif(ch=='u'):
        f,tab,pic,itn,k = setting()
        if(not f):
            cc = kc_init(tab,k)
            for i in range(itn):
                print("Finding:",i+1)
                idx = find_cc(tab,cc)
                print("Updating:",i+1)
                cc = ccc(tab,idx,k)
            print("Final finding...")
            idx = find_cc(tab,cc)
            print("Reducing...")
            xx = minipix(tab,cc,idx)
            print("Completing...")
            npic = download(xx,pic)
            print("Ready!")
    elif(ch=='s'):
        if(npic is not None):
            print("Name file to save, or...\ntype 'show' to show instead")
            name=input()
            fig = plt.matshow(npic)
            if(name=='show'):
                plt.show()
            else:
                name=name+".png"
                plt.axis('off')
                plt.savefig(name, bbox_inches='tight')
        else: print("No image to save")
    elif(ch=='i'):
        print("to do");
