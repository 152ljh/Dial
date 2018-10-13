import tkinter  #图形界面
import threading
import time

#生成主窗口-->窗口标题、大小
root = tkinter.Tk()
root.title('抽奖系统')
root.minsize(300,300)

#摆放功能按钮
btn1 = tkinter.Button(root,text='一等奖',bg='red')
btn1.place(x=20,y=20,width=50,height=50)

btn2 = tkinter.Button(root,text='二等奖',bg='white')
btn2.place(x=90,y=20,width=50,height=50)

btn3 = tkinter.Button(root,text='空',bg='white')
btn3.place(x=160,y=20,width=50,height=50)

btn4 = tkinter.Button(root,text='三等奖',bg='white')
btn4.place(x=230,y=20,width=50,height=50)

btn5 = tkinter.Button(root,text='空',bg='white')
btn5.place(x=20,y=230,width=50,height=50)

btn6 = tkinter.Button(root,text='三等奖',bg='white')
btn6.place(x=90,y=230,width=50,height=50)

btn7 = tkinter.Button(root,text='空',bg='white')
btn7.place(x=160,y=230,width=50,height=50)

btn8 = tkinter.Button(root,text='三等奖',bg='white')
btn8.place(x=230,y=230,width=50,height=50)

btn9 = tkinter.Button(root,text='二等奖',bg='white')
btn9.place(x=20,y=90,width=50,height=50)

btn10 = tkinter.Button(root,text='空',bg='white')
btn10.place(x=20,y=160,width=50,height=50)

btn11 = tkinter.Button(root,text='空',bg='white')
btn11.place(x=230,y=90,width=50,height=50)

btn12 = tkinter.Button(root,text='空',bg='white')
btn12.place(x=230,y=160,width=50,height=50)

herolists= [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]
#是否开启循环
isloop = False
#是否停止
stopsign = False
#目的：通过ID的索引值我们来确定我们的对应选项
stopid = None

#定义一个函数  目的：循环备选选项，设置选项的北京颜色
def round():
    #global:声明变量的作用域为全局作用域
    global isloop
    global stopid

    #判断是否开启循环
    if isloop == True:
        return

    i = 1

    if isinstance(stopid,int):
        i = stopid

    #开始旋转
    while True:

        #延时操作
        time.sleep(0.05)

        #将所有组件背景变白色
        for x in herolists:
            x['bg']='white'

        #当前数值（i）对应的组件变为红色
        herolists[i]['bg'] = 'red'

        i+=1
        print('当前i为',i)

        if i>=len(herolists):
            i = 0

        if stopsign == True:
            isloop = False
            stopid = i
            break

#开始的函数
def newtask():
    global isloop
    global stopsign

    stopsign = False

    #拓展 Tread：线程类:1>直接要传入运行的方法  2>run()
    #group 线程组 target 要执行的方法 name 线程名
    t = threading.Thread(target=round)

    t.start()

    isloop = True

#停止
def stop1():

    global stopsign

    if stopsign == True:
        return
    stopsign = True

#设置开始和停止按钮
btn_start = tkinter.Button(root,text='开始',command=newtask)
btn_start.place(x=90,y=125,width=50,height=50)

btn_stop = tkinter.Button(root,text='停止',command=stop1)
btn_stop.place(x=160,y=125,width=50,height=50)

#显示窗口
root.mainloop()