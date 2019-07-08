
import tkinter as tk
import wordRoot as wr

if __name__=='__main__':
    root=tk.Tk()
    root.title('="w"=')
    root.geometry('600x310')



    e=tk.Entry(root,font=("黑体", 20, "bold"))
    t=tk.Text(root,height=10,font=("黑体", 20, "bold"))


    e.pack()#side = tk.TOP
    t.pack(side = tk.BOTTOM)

    def enterAChar(event):
        print(e.get())
        t.delete(1.0,tk.END)
        t.insert('end',wr.getM(e.get()))

    e.bind("<KeyRelease>", enterAChar)

    root.mainloop()
