from tkinter import *
import random
import time

def up():
    global wx
    global wy
    if (wy > 11):
        wy = wy-10
        r.move(w, 0, -10)

    root.update()

def down():
    global wx
    global wy
    if (wy < 289):
        wy = wy + 10
        r.move(w, 0, 10)

    root.update()

def right():
    global wx
    global wy
    if (wx < 489):
        r.move(w, 10, 0)
        wx = wx+10

    root.update()

def left():
    global wx
    global wy
    if (wx > 11):
        r.move(w, -10, 0)
        wx = wx - 10
    root.update()

def keymove(event):
    if event.keysym == 'Up':
        up()
    if event.keysym == 'Down':
        down()
    if event.keysym == 'Left':
        left()
    if event.keysym == 'Right':
        right()
    if event.keysym == 'space':
        target()

def target():
    global tx
    global ty
    global tankx
    global tankl
    global tankg
    label['text'] = "ваш уровень:" + str(tankl)
    if(wx<tx+20 and wx>tx-20 and wy<ty+20 and wy>ty-20):
        shot.place_forget()
        a = random.randint(100, 350)
        b = random.randint(100, 200)
        r.move(t, a-tx, b-ty)
        r.move(ta, a-tx, b-ty)
        r.move(tb, a-tx, b-ty)
        r.move(tc, a-tx, b-ty)
        tankx = tankx+1
        for i in range(70):
            r.move(q, ((500/(tankl+1))/70)-(1/tankl), 0)
            tankg += ((500/(tankl+1))/70)-(1/tankl)
            time.sleep(0.01)
            root.update()
        tx = a
        ty = b
        if tankx>=tankl+1:
            tankx = 0
            tankl+=1
            r.move(q, -tankg, 0)
            tankg = 0
    shot.place(x = 55, y = 70)
    label['text'] = "ваш уровень:" + str(tankl)

def start():
    global xqwe
    global tx
    global ty
    global xx
    global xy
    global xl
    global xg
    while True:
        root.update()
        rzq.update()
        time.sleep(0.01)
        xqwe += 0.01
        if xqwe >= 5:
            xqwe = 0
            a = random.randint(100, 350)
            b = random.randint(100, 200)
            r.move(t, a - tx, b - ty)
            r.move(ta, a - tx, b - ty)
            r.move(tb, a - tx, b - ty)
            r.move(tc, a - tx, b - ty)
            tx = a
            ty = b
            xx = xx + 1
            for i in range(70):
                r.move(d, ((500 / (xl + 1)) / 70) - (1 / xl), 0)
                xg += ((500 / (xl + 1)) / 70) - (1 / xl)
                time.sleep(0.01)
                root.update()
            if xx >= xl + 1:
                xx = 0
                xl += 1
                r.move(d, -xg, 0)
                xg = 0
        lab['text'] = "уровень соперника:" + str(xl)

def menuf():
    menu_r.place(x = 0, y = 0)
    menu_exit.place(x = 400, y = 150)
    lab.place_forget()
    label.place_forget()
    choice_tank.place(x=0, y=270)
    choice_tank1.place(x=0, y=270)
    choice_tank2.place(x=350, y=270)
    choice_tank.create_polygon((201, 64), (201, 34), (230, 34), (230, 11), (280, 11), (280, 18),
                               (330, 18), (330, 25), (280, 25),
                               (280, 34), (301, 34), (301, 64), fill='#44af34', outline='#44af34')


def menu_exitf():
    menu_exit.place_forget()
    menu_r.place_forget()
    label.place(x=40, y=320)
    lab.place(x=200, y=320)
    choice_tank.place_forget()

root = Tk()
root.geometry('500x350')
root.title('tank and target')
root['bg'] = '#ddddff'
root.bind("<KeyPress-Up>", keymove)
root.bind("<KeyPress-Down>", keymove)
root.bind("<KeyPress-Left>", keymove)
root.bind("<KeyPress-Right>", keymove)
root.bind("<KeyPress-space>", keymove)

wx = 101
wy = 199
tx = 10
ty = 100
tankl = 1
tankx = 0
tankg = 0
xqwe = 0
xx = 1
xy = 7
xl = 1
xg = 0
r = Canvas(root, bg = '#ddddff', width=500, height=300)
r.pack()
r.create_oval((200, 200), (400, 400), fill = '#e39231', outline='#e39231')
Canvas(root, bg = '#000011', width=500, height=2).pack()
menu_r = Canvas(root, width=500, height=350, bg = '#347819')
menu_exit = Button(root, text = 'выход', command=menu_exitf)
q = r.create_polygon((1, 305), (1, 275),(30, 275),(30, 251),(80, 251),(80, 259),
                     (130, 259), (130, 267), (80, 267),
                     (80, 275), (101, 275), (101, 305), fill = '#44af34', outline='#44af34')
d = r.create_polygon((1, 7), (20, 30), (100, 31), (100, 40), (1, 40), fill = '#228d12', outline='#228d12')
t = r.create_oval((10, 100), (30, 120), fill = '#af3425', outline = '#8d1203')
ta = r.create_oval((13, 103), (27, 117), fill = '#efeffd', outline = '#efeffd')
tb = r.create_oval((14.5, 104.5), (24.5, 114.5), fill = '#af3425', outline = '#8d1203')
tc = r.create_oval((18, 108), (22.3, 112.3), fill = '#efeffd', outline = '#efeffd')
w = r.create_polygon((wx, wy), (wx+10, wy), (wx+10, wy+10), (wx, wy+10), fill = '#000032', outline='#000032')
choice_tank = Canvas(root, bg = '#f47819', width=500, height=70)
choice_tank1 = Canvas(root, bg = '#347819', width=150, height=70)
choice_tank2 = Canvas(root, bg = '#347819', width=150, height=70)
#choice_tank.place(x = 90, y = 270)
label = Label(root, bg = '#ddddff', fg = '#0100ff')
label.place(x = 40, y = 320)
label['text'] = "ваш уровень:" + str(tankl)
lab = Label(root, bg = '#ddddff', fg = '#0100ff')
lab.place(x = 200, y = 320)


rzq = Tk()
rzq.geometry('175x150+550+50')
rzq.title('упровление')
rzq['bg'] = '#0f8771'
rzq.wm_attributes('-alpha', 0.8)


Button(rzq, text = '←', bg = '#2fa993', command = left).place(x = 10, y = 10)
Button(rzq, text = '↑', bg = '#2fa993', command = up).place(x = 55, y = 10)
Button(rzq, text = '→', bg = '#2fa993', command = right).place(x = 100, y = 10)
Button(rzq, text = '↓', bg = '#2fa993', command=down)\
    .place(x = 55, y = 38)
shot = Button(rzq, text = 't', bg = '#2fa993', command=target)
shot.place(x = 55, y = 70)
menu = Button(rzq, text = 'menu', bg = '#2fa993', command = menuf)
menu.place(x = 5, y = 95)
rzq.bind("<KeyPress-Up>", keymove)
rzq.bind("<KeyPress-Down>", keymove)
rzq.bind("<KeyPress-Left>", keymove)
rzq.bind("<KeyPress-Right>", keymove)

start()


root.mainloop()
rzq.mainloop()
