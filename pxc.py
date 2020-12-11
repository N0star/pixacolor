I = '''FDC # PXC # 1.0.0 # 2020'''
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def upload(name):           #get an image
    img = mpimg.imread(name)
    tab = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            tab.append(img[i][j])
    print("table size: ",len(tab))
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


def kc_init(xx, k):         #init k-mean centroids
    ridx = np.random.permutation(len(xx))
    ctrd = xx[:k]
    return ctrd

def find_cc(xx, cc):        #find closest values
    indx = []#; cmpl=int(len(xx)/25)
    for i in range(len(xx)):
        mval = 9999;
        indx.append(0)
        #if(0==((i)%cmpl)): print(".",end="");
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

def setting(n=-1,k=-1):
    if(n<0): n = input("Number of interations (int): ")
    if(k<0): k = input("Number of colours (int): ")
    n = int(n); k = int(k)%256;
    print("File: ",name,", k=",k,", n=",n)
    ch = input("Is this data correct? (Y/n): ")
    if(ch=='Y' or ch=='y'): f=0;    
    else: f=1;
    return f,tab,pic,n,k;

#tab, pic = upload("Homare.jpeg")
#k=8; tab = tab[:1000] # testing
tab = []; pic = []; img = False;

print("Welcome to Pixacolor!")
while True:                         # main menu # MAIN LOOP #
    ch=input("\nu - upload, s - save,\nr - reduce colors\n"
             +"i - info, q - quit.\n\n"); cmd=ch.split(); ch=ch[0];
    
    upl = 0; red = 0; sav = 0; inf = 0; qui = 0;
    for i in range(len(cmd)):
        if(cmd[i]=='u'):         #case upload
            upl+=1;
            try:
                name=cmd[i+1]   #req img name
                upl+=1; j=0;
                try:
                    if(cmd[i+2]=='r'): j=1;
                    n=int(cmd[i+2+j]);
                    k=int(cmd[i+3+j]);
                    upl+=1; red=2;
                except IndexError: continue
            except IndexError: continue
            
        elif(cmd[i]=='r'):       #case reduce
            red=1;
            try:
                n=int(cmd[i+1]);
                k=int(cmd[i+2]);
                red=2;
            except IndexError: continue
            except ValueError: continue

        elif(cmd[i]=='s' or cmd[i]=='as'): #case save
            if(cmd[i]=='as'):
                target=name+"_"+str(k)+"x"+str(n);
                sav=2;
            else:
                sav=1;
                try:
                    target=cmd[i+1]; sav=2;
                except IndexError: continue

        elif(cmd[i]=='i' ): inf=1; #case info
        elif(cmd[i]=='q' ): qui=1; #case quit
            
    if(ch=='q'): break;
    if(upl>0):
        if(upl<2):
            name = input("Image name: ")
        tab = []; pic = []; img = True;
        try:
            tab,pic = upload(name)
        except FileNotFoundError:
            img=False; print("File not found...");
    if(red>0 or upl==3):
        if(img):
            if(red<2): f,tab,pic,itn,k = setting()
            else: f,tab,pic,itn,k = setting(n,k)
            if(not f):
                cc = kc_init(tab,k)
                for i in range(itn):
                    print("Searching...",i+1)
                    idx = find_cc(tab,cc)
                    print("Updating...",i+1)
                    cc = ccc(tab,idx,k)
                print("Final search...")
                idx = find_cc(tab,cc)
                print("Reducing...")
                xx = minipix(tab,cc,idx)
                print("Completing...")
                npic = download(xx,pic)
                print("Ready!")
        else: print("No image's been found!");
    if(sav>0):
        if(npic is not None):
            if(sav<2):
                print("Name file to save, or...\ntype 'show' to show instead")
                name=input()
            else: name=target;
            fig = plt.matshow(npic)
            if(name=='show'):
                plt.show()
            else:
                name=name+".png"
                plt.axis('off')
                plt.savefig(name, bbox_inches='tight')
        else: print("No image to save")
    if(inf):
        print(I);
    if(qui): break;
