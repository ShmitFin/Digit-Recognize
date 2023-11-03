import numpy
import random,os
#from numba import njit, jit
import ColorNetWork as ColorNetWork
os.system("color 2")
print(''' 
  _____  _       _ _     _____                            _ _   _             
 |  __ \(_)     (_) |   |  __ \                          (_) | (_)            
 | |  | |_  __ _ _| |_  | |__) |___  ___ ___   __ _ _ __  _| |_ _  ___  _ __  
 | |  | | |/ _` | | __| |  _  // _ \/ __/ _ \ / _` | '_ \| | __| |/ _ \| '_ \ 
 | |__| | | (_| | | |_  | | \ \  __/ (_| (_) | (_| | | | | | |_| | (_) | | | |
 |_____/|_|\__, |_|\__| |_|  \_\___|\___\___/ \__, |_| |_|_|\__|_|\___/|_| |_|
            __/ |                              __/ |                          
           |___/                              |___/                           ''')
input()
print("Running NetWork")
class NetWorkMenager:
    def __init__(self):
        import os, pickle
        path = os.getcwd()

    def SaveNetWork(self,obj,name):
        import pickle
        with open(name+".work","wb") as f:
            f.write(pickle.dumps(obj))
    #def PrepareNetWork(self,)
    def LoadNetWork(self,name):
        with open(name+".work","rb") as f:
            import pickle
            return pickle.loads(f.read())
class Programm:
    
    def __init__(self) -> None:
        import ColorNetWork as ColorNetWork,os,time
        self.NetWork=[Perceptron() for i in range(10)]
        #self.test=Neruon()
        self.test2 = Perceptron()
        self.warns=[]
        
        
    #@jit(fastmath=True,nopython=False)
    def SetLoadType(self,Type,file):
        h = NetWorkMenager()
        import os
        o = []
        if Type=="Load":
            h.LoadNetWork(name=file)
            for i in range(10):
                #print(self.NetWork[i].weights) #= 
                #print(h.LoadNetWork(name="test")[i])
                self.NetWork[i].weights=h.LoadNetWork(name=file)[i]
        elif Type=="Edu":
            os.system("color 4")
            for i in range(10):
                for j in range(1000):
                    self.NetWork[i].edu(i,arr=ColorNetWork.Book())
                    print(str(i),":",str(j))
                    #time.sleep(0.1)
                    #os.system("CLS")
                o.append(self.NetWork[i].weights)
            
            h.SaveNetWork(o,name=file)
        
        
    
            
            

    def ask(self,n: str)-> list:
        a = []
        for i in range(10):
            a.append([self.NetWork[i].perdict(n),i])
        return a
    def format(self,x):
        for i in x:
            if i[0]:
                return i[1]

    def loss(self):
        self.line=[]
        for i in range(100):
            self.line.append(i)

        loss = 0
        for i in range(100):
            true = random.randint(0,9)
            if self.format(self.ask(self.NetWork[0].numers[true])) != true:
                loss+=1
        return loss


class Perceptron:
    def __init__(self) -> None:
        import random
        self.weights=[0 for i in range(15)]
        self.loss=[]
        import random
        self.zeros=["010100100100010"]
        self.ones=["010110010010111","010010010010010","010010010010111","001011001001001","010110010010010"]
        self.twos=["011001111100111","011001111100110","111001111100110","010001111100010"]
        self.threes=["010001010001010","011001111001011"]
        self.fours=["000101111001001","001101111001001","100101111001001"]
        self.fives=["110100010001111","111100010001111","111100011001111","110100111001111","110100111001011"]
        self.six=["110100111101111","111100110101110"]
        self.sevens=["011001001001001","111001001001001"]
        self.eights=["010101010101010"]
        self.nines=["010101011001001"]
        self.numers=["010100100100010","010110010010111","011001111100111","010001010001010","000101111001001","110100010001111","110100111101111","011001001001001","010101010101010","010101011001001"]
        #self.numers=[self.zeros,self.ones,self.twos,self.threes,self.fours,self.fives,self.six,self.sevens,self.eights,self.nines]
    #@njit(fastmath=True)
    def perdict(self,Sensor):
        b = 7
        s = 0
        for i in range(15):
            s += int(Sensor[i]) * self.weights[i]

        if s>=b:
            return True
        else:
            return False
    def incrase(self, x: str):
        for i in range(len(x)):
            if int(x[i]) == 1:
                self.weights[i]+=1

    
    def decrase(self, x: str):
        for i in range(len(x)):
            if int(x[i]) == 1:
                self.weights[i]-=1
    #@jit(fastmath=True, forceobj=True)
    def edu(self,tema,arr):
        
        losses = 0
        for i in range(10000):
            j = random.randint(0,9)
            r = self.perdict(arr[j])
            
            if j != tema:
                if r:
                    self.decrase(arr[j])
                    losses+=1
            else:
                if not r:

                    self.incrase(arr[j])
                    losses+=1
        return losses

    # import the cv2 library
    def show(self):
        pass
        #import cv2
        
        # The function cv2.imread() is used to read an image.
        #img_grayscale = cv2.imread('C:\\Users\User\\projects\\5.png',0)
        
        # The function cv2.imshow() is used to display an image in a window.
        #resized_up = cv2.resize(img_grayscale, (120,200), interpolation= cv2.INTER_NEAREST)
        #cv2.imshow('graycsale image',resized_up)
        
        # waitKey() waits for a key press to close the window and 0 specifies indefinite loop
        #cv2.waitKey(0)
        
        # cv2.destroyAllWindows() simply destroys all the windows we created.
        #cv2.destroyAllWindows()

    def visualize(self,weights):
        import matplotlib.pyplot as plt
        x = []
        for i in range(15):
            x.append(i)
        plt.scatter(x,weights)
        plt.show()

class LossCounter():
    def __init__(self) -> None:
        pass
    def a(RUN):
        import ColorNetWork as ColorNetWork
        h = ColorNetWork.Book()
        loss = []
        for i in range(1000):
            temp = 0
            for i in range(100):
                run = RUN
                v =random.choice(h)
                #print(run.ask(v),h.index(v))
                #print(run.format(run.ask(v)),h.index(v))
                if run.format(run.ask(v)) != h.index(v):
                    temp+=1
                else:
                    temp+=0
            loss.append(temp)
        return loss
        

if __name__=="__main__":
    
    pass
    '''
    import Interface
    import matplotlib.pyplot as plt
    #import customnums
    i = Interface.interface("5.png")
    q = i.conv(i.ar)
    #print(q)
    import os
    run = Programm()
    run.SetLoadType("Load","network")
    os.system("color 7")
    test = Perceptron()
    a = Perceptron()
    a.educustom(5,a.numers)
    a.educustom(5,test.nums)
    print(a.perdict("111100111001111")) 
    #print(test.nums[4])
    #print(run.ask(q))

    Menager = NetWorkMenager()
    obj = []
    for i in range(10):
        obj.append(run.NetWork[i].weights)
    #Menager.SaveNetWork(obj=obj,name="network")

    #for i in range(10):
        #run.NetWork[i].weights = Menager.LoadNetWork(name="network")[i]
    






    print(run.format(run.ask(q)))
    run.loss()
    line = []
    for i in range(10):
        line.append(i)

    #test.visualize(run.weights)
    from matplotlib import pyplot as plt
    from matplotlib import image as mpimg
    
    plt.title("Network think it's number "+str(run.format(run.ask(q))))
    plt.xlabel("X pixel scaling")
    plt.ylabel("Y pixels scaling")
    
    image = mpimg.imread("C:\\Users\\User\\projects\\5.png")
    plt.imshow(image)
    plt.show()
    line=[]
    for i in range(1000):
        line.append(i)
    plt.plot(line,LossCounter.a(run))
    plt.show()
    #print(run.NetWork[1].weights)
    #test.show()
'''