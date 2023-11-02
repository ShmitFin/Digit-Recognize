'''import customtkinter as tk

root = tk.CTk()
root.title("Neruon")
root.geometry("1300x500")
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=0)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=1)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=2)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=3)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=4)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=5)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=6)
a = tk.CTkCheckBox(root,text="")
a.grid(row=0,column=7)
root.mainloop()'''
class interface:
    def __init__(self,path) -> None:
        
        from PIL import Image
        from numpy import array
        self.im_1 = Image.open(path)
        self.ar = array(self.im_1)
    def img(self):
        return self.ar
    def conv(self,x):
        a= ""
        for i in range(5):
            for j in range(3):
                #print(x[i][j])
                if sum(x[i][j])-255>0:
                    a += "0"
                else:
                    a+="1"
                '''if x[i][j].ravel():
                    a += "0"
                else:
                    a += "1"'''
        return a
                



#print(ar)