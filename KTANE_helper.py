import tkinter as tk
from PIL import ImageTk, Image
loaded = None

pph = {}
mod = {}
sw = {}
tb = {}
kp = {}
ss = {}
wf = {}
mm = {}
mc = {}
cw = {}
ws = {}
mz = {}
pw = {}

class Swagbutton(tk.Label):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Label.__init__(self, master, cnf, **kw)
        self.sfg = self.cget('fg')
    
    def select(self):
        self.config(text = '✓'+self.cget('text')[1:], fg = 'red')

    def deselect(self):
        self.config(text = '✗'+self.cget('text')[1:], fg = self.sfg)

def init_all():
    pph_init()
    mod_init()
    sw_init()
    tb_init()
    kp_init()
    ss_init()
    wf_init()
    mm_init()
    mc_init()
    cw_init()
    ws_init()
    mz_init()
    pw_init()

def update():
    sw_answer()
    tb_answer()
    ss_answer()
    cw_answer()

def reset_module():
    module = mod['module'].get()
    if module == '':
        return
    elif module == "simple wires":
        sw_init()
    elif module == "the button":
        tb_init()
    elif module == "keypads":
        kp_init()
    elif module == "simon says":
        ss_init()
    elif module == "who's on first":
        wf_init()
    elif module == "memory":
        mm_init()
    elif module == "morse code":
        mc_init()
    elif module == "complicated wires":
        cw_init()
    elif module == "wire sequences":
        ws_init()
    elif module == "mazes":
        mz_init()
    elif module == "passwords":
        pw_init()
    update()
    change_module()

def reset_all():
    init_all()
    update()
    change_module()

def change_module():
    global loaded
    module = mod['module'].get()
    if module == loaded:
        return
    elif loaded != None:
        loaded.grid_forget()
        
    if module == "simple wires":
        sw['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = sw['frame']
    elif module == "the button": 
        tb['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = tb['frame']
    elif module == "keypads":
        kp['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = kp['frame']
    elif module == "simon says":
        ss['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = ss['frame']
    elif module == "who's on first":
        wf['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = wf['frame']
    elif module == "memory":
        mm['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = mm['frame']
    elif module == "morse code":
        mc['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = mc['frame']
    elif module == "complicated wires":
        cw['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = cw['frame']
    elif module == "wire sequences":
        ws['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = ws['frame']
    elif module == "mazes":
        mz['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = mz['frame']
    elif module == "passwords":
        pw['frame'].grid(row = 0, rowspan = 10, column = 1, padx = 15)
        loaded = pw['frame']

def pph_init():
    pph['frame'] = tk.Frame(frame1)
    pph['vowel'] = tk.BooleanVar(value = False)
    pph['e_vowel'] = tk.Checkbutton(pph['frame'], text = "vowel", variable = pph['vowel'], command = update)
    pph['digit'] = tk.StringVar(value = "odd")
    pph['e_digit'] = tk.Checkbutton(pph['frame'], text = "even", variable = pph['digit'], onvalue = "even", offvalue = "odd", command = update)
    pph['pport'] = tk.BooleanVar(value = False)
    pph['e_pport'] = tk.Checkbutton(pph['frame'], text = "parallel port", variable = pph['pport'], command = update)
    pph['lcar'] = tk.BooleanVar(value = False)
    pph['e_lcar'] = tk.Checkbutton(pph['frame'], text = "lit CAR", variable = pph['lcar'], command = update)
    pph['lfrk'] = tk.BooleanVar(value = False)
    pph['e_lfrk'] = tk.Checkbutton(pph['frame'], text = "lit FRK", variable = pph['lfrk'], command = update)
    pph['batteries'] = tk.IntVar(value = 1)
    pph['e1_batteries'] = tk.Radiobutton(pph['frame'], text = '0-1 batteries', variable = pph['batteries'], value = 1, command = update)
    pph['e2_batteries'] = tk.Radiobutton(pph['frame'], text = '2 batteries', variable = pph['batteries'], value = 2, command = update)
    pph['e3_batteries'] = tk.Radiobutton(pph['frame'], text = '3+ batteries', variable = pph['batteries'], value = 3, command = update)
    pph['resetmod_button'] = tk.Button(pph['frame'], text = "Reset Module", command = reset_module)
    pph['resetall_button'] = tk.Button(pph['frame'], text = "Reset All", command = reset_all)

    pph['e_vowel'].grid(row = 0, column = 0, sticky = 'w')
    pph['e_digit'].grid(row = 1, column = 0, sticky = 'w')
    pph['e_pport'].grid(row = 2, column = 0, sticky = 'w')
    pph['e_lcar'].grid(row = 3, column = 0, sticky = 'w')
    pph['e_lfrk'].grid(row = 4, column = 0, sticky = 'w')
    pph['e1_batteries'].grid(row = 5, column = 0, sticky = 'w')
    pph['e2_batteries'].grid(row = 6, column = 0, sticky = 'w')
    pph['e3_batteries'].grid(row = 7, column = 0, sticky = 'w')
    pph['resetmod_button'].grid(row = 8, column = 0, sticky = 'w')
    pph['resetall_button'].grid(row = 9, column = 0, sticky = 'w')
    pph['frame'].grid(row = 0, column = 0, sticky = 'n')

def mod_init():    
    mod['frame'] = tk.Frame(frame1)
    mod['list'] = ["simple wires", "the button", "keypads", "simon says", "who's on first", "memory", "morse code", "complicated wires", "wire sequences", \
                    "mazes", "passwords", "knobs"]
    mod['module'] = tk.StringVar()
    mod['rbuttons'] = [tk.Radiobutton(mod['frame'], indicatoron = False, text = mod_text, variable = mod['module'], value = mod_text, command = change_module) for mod_text in mod['list']]

    for i in range(len(mod['rbuttons'])):
        mod['rbuttons'][i].grid(row = i, column = 2, sticky = 'w', pady = 1)
    mod['frame'].grid(row = 0, column = 2, sticky = 'n')

def sw_init():
    sw['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    sw['cframe'] = tk.Frame(sw['frame'])

    sw['wires'] = [tk.StringVar(value = 'none') for i in range(6)]
    sw['colors'] = ["red", "blue", "yellow", "white", "black"]
    sw['rbuttons'] = []
    i = 0
    for wire in sw['wires']:
        sw['rbuttons'].append([tk.Radiobutton(sw['cframe'], background = color, variable = sw['wires'][i], value = color, command = sw_answer) for color in sw['colors']])
        sw['rbuttons'][i].append(tk.Radiobutton(sw['cframe'], text = 'none', variable = sw['wires'][i], value = 'none', command = sw_answer))
        i += 1

    sw['alabel'] = tk.Label(sw['frame'])
    sw['dlabel'] = tk.Label(sw['frame'], text = 'dependencies', fg = 'grey')
    sw['ddep'] = Swagbutton(sw['frame'], text = '✗ even', fg = 'grey')
    
    i = 0
    i2 = 0
    for rbutton_set in sw['rbuttons']:
        for rbutton in rbutton_set:
            rbutton.grid(row = i, column = i2, padx = 1, pady = 5)
            i2 += 1
        i2 = 0
        i += 1
    sw['cframe'].grid(row = 0, column = 0, columnspan = 6)
    sw['alabel'].grid(row = 1, column = 1, pady = 5, padx = 10)
    sw['dlabel'].grid(row = 1, column = 0, pady = 0, padx = 0, sticky = 'w')
    sw['ddep'].grid(row = 2, column = 0, pady = 0, sticky = 'w')

def sw_answer():
    wires = [wire.get() for wire in sw['wires']]
    wires_c = [wire for wire in wires if wire != 'none']
    count = len(wires_c)
    sw['ddep'].deselect()
    
    if count < 3:
        sw['alabel'].config(text = '')
        return
    cut = sw_check(count, wires_c, pph['digit'].get())
    if len(set([sw_check(count, wires_c, d) for d in ['odd', 'even']])) != 1:
        sw['ddep'].select()

    sw['alabel'].config(text = f"Wire to cut: {cut}")

def sw_check(count, w_c, d):
    if count == 3:
        if w_c.count("red") == 0:
            cut = 'second'
        elif w_c[-1] == "white":
            cut = 'last'
        elif w_c.count("blue") > 1:
            cut = 'last blue'
        else:
            cut = 'last'
    elif count == 4:
        if w_c.count("red") > 1 and d == 'odd':
            cut = 'last red'
        elif w_c[-1] == 'yellow' and w_c.count("red") == 0:
            cut = 'first'
        elif w_c.count("blue") == 1:
            cut = 'first'
        elif w_c.count("yellow") > 1:
            cut = 'last'
        else:
            cut = 'second'
    elif count == 5:
        if w_c[-1] == "black" and d == "odd":
            cut = 'fourth'
        elif w_c.count("red") == 1 and w_c.count("yellow") > 1:
            cut = 'first'
        elif w_c.count("black") == 0:
            cut = 'second'
        else:
            cut = 'first'
    elif count == 6:
        if w_c.count("yellow") == 0 and d == "odd":
            cut = 'third'
        elif w_c.count("yellow") == 1 and w_c.count("white") > 1:
            cut = 'fourth'
        elif w_c.count("red") == 0:
            cut = 'last'
        else:
            cut = 'fourth'
    else:
        while True:
            print('cringe')
    return cut

def tb_init():
    tb['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    tb['cframe'] = tk.Frame(tb['frame'])
    tb['wframe'] = tk.Frame(tb['frame'])

    tb['bcolor'] = tk.StringVar()
    tb['colors'] = ["red", "blue", "yellow", "white"]
    tb['crbuttons'] = [tk.Radiobutton(tb['cframe'], background = color, variable = tb['bcolor'], value = color, command = tb_answer) for color in tb['colors']]

    tb['bword'] = tk.StringVar()
    tb['words'] = ['abort', 'detonate', 'hold', 'other']
    tb['wrbuttons'] = [tk.Radiobutton(tb['wframe'], text = word, variable = tb['bword'], value = word, command = tb_answer) for word in tb['words']]

    tb['alabel'] = tk.Label(tb['frame'], justify = 'left')
    tb['dlabel'] = tk.Label(tb['frame'], text = 'dependencies', fg = 'grey')
    tb['bdep'] = Swagbutton(tb['frame'], text = '✗ battery', fg = 'grey')
    tb['lcardep'] = Swagbutton(tb['frame'], text = '✗ lit CAR', fg = 'grey')
    tb['lfrkdep'] = Swagbutton(tb['frame'], text = '✗ lit FRK', fg = 'grey')

    i = 0
    for rbutton in tb['crbuttons']:
        rbutton.grid(row = 0, column = i, padx = 1, pady = 5)
        i += 1
    i = 0
    for rbutton in tb['wrbuttons']:
        rbutton.grid(row = 1, column = i, padx = 1, pady = 5)
        i += 1
    tb['cframe'].grid(row = 0, column = 0, columnspan = 4)
    tb['wframe'].grid(row = 1, column = 0, columnspan = 3)
    tb['alabel'].grid(row = 2, rowspan = 4, column = 1, pady = 5, padx = 10, sticky = 'w')
    tb['dlabel'].grid(row = 2, column = 0, pady = 0, padx = 0, sticky = 'w')
    tb['bdep'].grid(row = 3, column = 0, pady = 0, sticky = 'w')
    tb['lcardep'].grid(row = 4, column = 0, pady = 0, sticky = 'w')
    tb['lfrkdep'].grid(row = 5, column = 0, pady = 0, sticky = 'w')

def tb_answer():
    tb['bdep'].deselect()
    tb['lcardep'].deselect()
    tb['lfrkdep'].deselect()

    if tb['bcolor'].get() == '' or tb['bword'].get() == '':
        tb['alabel'].config(text = '')
        return

    cstrip = tb_check(tb['bcolor'].get(), tb['bword'].get(), pph['batteries'].get(), pph['lcar'].get(), pph['lfrk'].get())

    bdep_check = []
    for frk in [True, False]:
        for car in [True, False]:
            bdep_check.append([tb_check(tb['bcolor'].get(), tb['bword'].get(), b, car, frk) for b in range(1, 4)])
    for l in bdep_check:
        if len(set(l)) != 1:
            tb['bdep'].select()
    
    lcardep_check = []
    for frk in [True, False]:
        for b in range(1, 4):
            lcardep_check.append([tb_check(tb['bcolor'].get(), tb['bword'].get(), b, car, frk) for car in [True, False]])
    for l in lcardep_check:
        if len(set(l)) != 1:
            tb['lcardep'].select()

    lfrkdep_check = []
    for car in [True, False]:
        for b in range(1, 4):
            lfrkdep_check.append([tb_check(tb['bcolor'].get(), tb['bword'].get(), b, car, frk) for frk in [True, False]])
    for l in lfrkdep_check:
        if len(set(l)) != 1:
            tb['lfrkdep'].select()
    
    if cstrip:
        tb['alabel'].config(text = "blue strip: let go when timer has a 4\n\nyellow strip: let go when timer has a 5\n\nother: let go when timer has a 1")
    else: 
        tb['alabel'].config(text = "press and let go immediately")

def tb_check(tbc_color, tbc_word, tbc_b, tbc_lcar, tbc_lfrk):

    if tbc_color == 'blue' and tbc_word == 'abort':
        cstrip = True
    elif tbc_b > 1 and tbc_word == 'detonate':
        cstrip = False
    elif tbc_color == 'white' and tbc_lcar:
        cstrip = True
    elif tbc_b > 2 and tbc_lfrk:
        cstrip = False
    elif tbc_color == 'yellow':
        cstrip = True
    elif tbc_color == 'red' and tbc_word == 'hold':
        cstrip = False
    else: 
        cstrip = True

    return cstrip

def kp_init():
    kp['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    kp['sframe'] = tk.Frame(kp['frame'])

    kp['s'] = ['ὦ', 'æ', '©', 'Ӭ', 'Ҩ', 'Ҋ', 'ϗ', 'ϟ', 'Ԇ', 'Ϙ', 'Ѯ', 'ƛ', 'Ω', '¶', 'ψ', '¿', 'Ϭ', 'Ͼ', 'Ͽ', '★', '☆', '҂', 'Ѣ', 'Ѭ', 'Ѧ', 'Җ', 'ټ']
    kp['svars'] = [tk.BooleanVar(value = False) for symbol in kp['s']]
    kp['se'] = [tk.Checkbutton(kp['sframe'], text = symbol, variable = kp['svars'][kp['s'].index(symbol)], command = kp_answer, font = ('microsoft yahei', 17)) for symbol in kp['s']]
    kp['alabel'] = tk.Label(kp['frame'], font = ('microsoft yahei', 17))

    i=0
    for b in kp['se']:
        b.grid(row = i//5, column = i%5, sticky = 'w')
        i += 1
    kp['sframe'].grid(row = 0, column = 0)
    kp['alabel'].grid(row = 1, column = 0)

def kp_answer():

    vars = [val.get() for val in kp['svars']]
    if vars.count(True) != 4:
        kp['alabel'].config(text = '')
        return
    vs = [kp['s'][i] for i in range(len(vars)) if vars[i]]
    # 'ὦ', 'æ', '©', 'Ӭ', 'Ҩ', 'Ҋ', 'ϗ', 'ϟ', 'Ԇ', 'Ϙ', 'Ѯ', 'ƛ', 'Ω', '¶', 'ψ', '¿', 'Ϭ', 'Ͼ', 'Ͽ', '★', '☆', '҂', 'Ѣ', 'Ѭ', 'Ѧ', 'Җ', 'ټ'
    cols = [['Ϙ', 'Ѧ', 'ƛ', 'ϟ', 'Ѭ', 'ϗ', 'Ͽ'], ['Ӭ', 'Ϙ', 'Ͽ', 'Ҩ', '☆', 'ϗ', '¿'], ['©', 'ὦ', 'Ҩ', 'Җ', 'Ԇ', 'ƛ', '☆'], \
            ['Ϭ', '¶', 'Ѣ', 'Ѭ', 'Җ', '¿', 'ټ'], ['ψ', 'ټ', 'Ѣ', 'Ͼ', '¶', 'Ѯ', '★'], ['Ϭ', 'Ӭ', '҂', 'æ', 'ψ', 'Ҋ', 'Ω']]
    fcol = []
    for col in cols:
        if [col.count(s) for s in vs] == [1, 1, 1, 1]:
            fcol = col
            break
    if fcol == []:
        kp['alabel'].config(text = 'INVALID COMBINATION')
        return
    ovi = [fcol.index(s) for s in vs]
    ovi.sort()
    ovs = [fcol[i] for i in ovi]
    kp['alabel'].config(text = ovs)
    
def ss_init():
    ss['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    ss['sframe'] = tk.Frame(ss['frame'])
    ss['strikes'] = tk.IntVar(value = 0)
    ss['rbuttons'] = [tk.Radiobutton(ss['sframe'], text = '0 strikes', variable = ss['strikes'], value = 0, command = ss_answer), \
                        tk.Radiobutton(ss['sframe'], text = '1 strike', variable = ss['strikes'], value = 1, command = ss_answer), \
                        tk.Radiobutton(ss['sframe'], text = '2 strikes', variable = ss['strikes'], value = 2, command = ss_answer)]
    ss['alabel'] = tk.Label(ss['frame'])
    
    ss['dlabel'] = tk.Label(ss['sframe'], text = 'dependencies', fg = 'grey')
    ss['vdep'] = Swagbutton(ss['sframe'], text = '✗ vowel', fg = 'grey')
    ss['vdep'].select()

    i = 0
    for rb in ss['rbuttons']:
        rb.grid(row = i, column = 0, sticky = 'w')
        i += 1
    ss['dlabel'].grid(row = i+1, column = 0)
    ss['vdep'].grid(row = i+2, column = 0)
    ss['sframe'].grid(row = 0, column = 0)
    ss['alabel'].grid(row = 0, column = 1)

    ss_answer()

def ss_answer():
    v = pph['vowel'].get() 
    s = ss['strikes'].get()
    a = ss['alabel']

    if v:
        if s == 0:
            a.config(text = 'Red --> Blue\nBlue --> Red\nGreen -> Yellow\nYellow --> Green')
        if s == 1: 
            a.config(text = 'Red --> Yellow\nBlue --> Green\nGreen -> Blue\nYellow --> Red')
        if s == 2:
            a.config(text = 'Red --> Green\nBlue --> Red\nGreen -> Yellow\nYellow --> Blue')
    else:
        if s == 0:
            a.config(text = 'Red --> Blue\nBlue --> Yellow\nGreen -> Green\nYellow --> Red')
        if s == 1: 
            a.config(text = 'Red --> Red\nBlue --> Blue\nGreen -> Yellow\nYellow --> Green')
        if s == 2:
            a.config(text = 'Red --> Yellow\nBlue --> Green\nGreen -> Blue\nYellow --> Red')

def wf_init():
    wf['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    wf['eframe'] = tk.Frame(wf['frame'])
    wf['ldw'] = tk.Label(wf['eframe'], text = 'DISPLAY')
    wf['dw'] = tk.StringVar()
    wf['dw'].trace_add("write", lambda a, b, c: wf_answer())
    wf['edw'] = tk.Entry(wf['eframe'], textvariable = wf['dw'])
    wf['lbw'] = tk.Label(wf['eframe'], text = 'BUTTON')
    wf['bw'] = tk.StringVar()
    wf['bw'].trace_add("write", lambda a, b, c: wf_answer())
    wf['ebw'] = tk.Entry(wf['eframe'], textvariable = wf['bw'])
    wf['alabel'] = tk.Label(wf['frame'], wraplength = 200)

    wf['ldw'].grid(row = 0, column = 0)
    wf['edw'].grid(row = 1, column = 0)
    wf['lbw'].grid(row = 0, column = 1)
    wf['ebw'].grid(row = 1, column = 1)
    wf['eframe'].grid(row = 0, column = 0)
    wf['alabel'].grid(row = 1, column = 0, rowspan = 10)
    
    wf_answer()

def wf_answer():
    display = wf['dw'].get().lower()
    dwords = {'yes' : 'middle left', 'first' : 'top right', 'display' : 'bottom right', 'okay' : 'top right', 'says' : 'bottom right', 'nothing' : 'middle left', '' : 'bottom left', 'blank' : 'middle right', 'no' : 'bottom right', 'led' : 'middle left', 'lead' : 'bottom right', 'read' : 'middle right', 'red' : 'middle right', 'reed' : 'bottom left', 'leed' : 'bottom left', 'hold on' : 'bottom right', 'you' : 'middle right', 'you are' : 'bottom right', 'your' : 'middle right', 'you\'re' : 'middle right', 'ur' : 'top left', 'there' : 'bottom right', 'they\'re' : 'bottom left', 'their' : 'middle right', 'they are' : 'middle left', 'see' : 'bottom right', 'c' : 'top right', 'cee' : 'bottom right'}
    if list(dwords.keys()).count(display) != 1:
        return
    wf['lbw'].config(text = dwords[display].upper() + ' BUTTON')
    
    button = wf['bw'].get().lower()
    bwords = {'ready': 'yes, okay, what, middle, left, press, right, blank, ready, no, first, uhhh, nothing, wait', 'first': 'left, okay, yes, middle, no, right, nothing, uhhh, wait, ready, blank, what, press, first', 'no': 'blank, uhhh, wait, first, what, ready, right, yes, nothing, left, press, okay, no, middle', 'blank': 'wait, right, okay, middle, blank, press, ready, nothing, no, what, left, uhhh, yes, first', 'nothing': 'uhhh, right, okay, middle, yes, blank, no, press, left, what, wait, first, nothing, ready', 'yes': 'okay, right, uhhh, middle, first, what, press, ready, nothing, yes, left, blank, no, wait', 'what': 'uhhh, what, left, nothing, ready, blank, middle, no, okay, first, wait, yes, press, right', 'uhhh': 'ready, nothing, left, what, okay, yes, right, no, press, blank, uhhh, middle, wait, first', 'left': 'right, left, first, no, middle, yes, blank, what, uhhh, wait, press, ready, okay, nothing', 'right': 'yes, nothing, ready, press, no, wait, what, right, middle, left, uhhh, blank, okay, first', 'middle': 'blank, ready, okay, what, nothing, press, no, wait, left, middle, right, first, uhhh, yes', 'okay': 'middle, no, first, yes, uhhh, nothing, wait, okay, left, ready, blank, press, what, right', 'wait': 'uhhh, no, blank, okay, yes, left, first, press, what, wait, nothing, ready, right, middle', 'press': 'right, middle, yes, ready, press, okay, nothing, uhhh, blank, left, first, what, no, wait', 'you': "sure, you are, your, you're, next, uh huh, ur, hold, what?, you, uh uh, like, done, u", 'you are': "your, next, like, uh huh, what?, done, uh uh, hold, you, u, you're, sure, ur, you are", 'your': "uh uh, you are, uh huh, your, next, ur, sure, u, you're, you, what?, hold, like, done", "you're": "you, you're, ur, next, uh uh, you are, u, your, what?, uh huh, sure, done, like, hold", 'ur': "done, u, ur, uh huh, what?, sure, your, hold, you're, like, next, uh uh, you are, you", 'u': "uh huh, sure, next, what?, you're, ur, uh uh, done, u, you, like, hold, you are, your", 'uh huh': "uh huh, your, you are, you, done, hold, uh uh, next, sure, like, you're, ur, u, what?", 'uh uh': "ur, u, you are, you're, next, uh uh, done, you, uh huh, like, your, sure, hold, what?", 'what?': "you, hold, you're, your, u, done, uh uh, like, you are, uh huh, ur, next, what?, sure", 'done': "sure, uh huh, next, what?, your, ur, you're, hold, like, you, u, you are, uh uh, done", 'next': "what?, uh huh, uh uh, your, hold, sure, next, like, done, you are, ur, you're, u, you", 'hold': "you are, u, done, uh uh, you, ur, sure, what?, you're, next, hold, uh huh, your, like", 'sure': "you are, done, like, you're, you, hold, uh huh, ur, sure, u, what?, next, your, uh uh", 'like': "you're, next, u, ur, hold, done, uh uh, what?, uh huh, you, like, sure, you are, your"}
    if list(bwords.keys()).count(button) != 1:
        return
    wf['alabel'].config(text = bwords[button].upper())

def mm_init():
    mm['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    mm['sframe'] = tk.Frame(mm['frame'])
    mm['p'] = [tk.IntVar() for i in range(4)]
    mm['l'] = [tk.IntVar() for i in range(4)]
    mm['l_d'] = tk.Label(mm['frame'], text = 'DISPLAY')
    mm['d'] = tk.IntVar()
    mm['dr'] = [tk.Radiobutton(mm['frame'], text = i, variable = mm['d'], value = i, command = mm_answer) for i in range(5)]
    mm['pr'] = [[tk.Radiobutton(mm['sframe'], text = f"P{i}", variable = mm['p'][i2], value = i, command = mm_answer) for i in range(5)] for i2 in range(len(mm['p']))]
    mm['lr'] = [[tk.Radiobutton(mm['sframe'], text = f"L{i}", variable = mm['l'][i2], value = i, command = mm_answer) for i in range(5)] for i2 in range(len(mm['l']))]
    mm['f'] = [tk.Label(mm['sframe']) for i in range(5)]

    for i1 in range(4):
        for i2 in range(5):
            mm['pr'][i1][i2].grid(row = i1*3, column = i2)
            mm['lr'][i1][i2].grid(row = i1*3+1, column = i2)
    for i in range(5):
        mm['dr'][i].grid(row = 2, column = i)
        mm['f'][i].grid(row = i*3+2, column = 0, columnspan = 5)
    mm['l_d'].grid(row = 1, column = 0, columnspan = 5)
    mm['sframe'].grid(row = 0, column = 0, columnspan = 5)

def mm_answer():
    bp = 0
    bl = 0
    p = [mm['p'][i].get() for i in range(len(mm['p']))]
    l = [mm['l'][i].get() for i in range(len(mm['l']))]
    d = mm['d'].get()
    if d == 0:
        return
    elif p[0] == 0 or l[0] == 0:
        stage = 1
        if d == 1:
            bp = 2
        elif d == 2:
            bp = 2
        elif d == 3:
            bp = 3
        elif d == 4:
            bp = 4
    elif p[1] == 0 or l[1] == 0:
        stage = 2
        if d == 1:
            bl = 4
        if d == 2:
            bp = p[0]
        if d == 3: 
            bp = 1
        if d == 4:
            bp = p[0]
    elif p[2] == 0 or l[2] == 0:
        stage = 3
        if d == 1:
            bl = l[1]
        elif d == 2:
            bl = l[0]
        elif d == 3:
            bp = 3
        elif d == 4:
            bl = 4
    elif p[3] == 0 or l[3] == 0:
        stage = 4
        if d == 1:
            bp = p[0]
        if d == 2:
            bp = 1
        if d == 3:
            bp = p[1]
        if d == 4:
            bp = p[1]
    else:
        stage = 5
        if d == 1:
            bl = l[0]
        if d == 2:
            bl = l[1]
        if d == 3:
            bl = l[3]
        if d == 4:
            bl = l[2]
    
    if bp != 0:
        if stage < 5:
            mm['pr'][stage-1][bp].select()
        mm['f'][stage-1].config(text = f'select button in position {bp}')
    elif bl != 0:
        if stage < 5:
            mm['lr'][stage-1][bl].select()
        mm['f'][stage-1].config(text = f'select button with label {bl}')
    mm['dr'][0].select()

def mc_init():
    mc['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    mc['bframe'] = tk.Frame(mc['frame'])

    i = ImageTk.PhotoImage(Image.open("pictures/mc.jpg").resize((300, 200)))
    mc['i'] = tk.Label(mc['frame'], image = i)
    mc['i'].image = i

    mc['l'] = tk.StringVar()
    mc['l'].trace_add("write", lambda a, b, c: mc_answer())
    mc['l_l'] = tk.Label(mc['bframe'], text = 'enter letters in any order')
    mc['e_l'] = tk.Entry(mc['bframe'], textvariable = mc['l'])
    mc['alabel'] = tk.Label(mc['bframe'])

    mc['l_l'].grid(row = 0, column = 0)
    mc['e_l'].grid(row = 1, column = 0)
    mc['alabel'].grid(row = 2, column = 0)
    mc['bframe'].grid(row = 1, column = 0)
    mc['i'].grid(row = 0, column = 0)

def mc_answer():
    l = mc['l'].get()
    d = {'3.505 MHz': ['s', 'h', 'e', 'l', 'l'], '3.515 MHz': ['h', 'a', 'l', 'l', 's'], '3.522 MHz': ['s', 'l', 'i', 'c', 'k'], '3.532 MHz': ['t', 'r', 'i', 'c', 'k'], '3.535 MHz': ['b', 'o', 'x', 'e', 's'], '3.542 MHz': ['l', 'e', 'a', 'k', 's'], '3.545 MHz': ['s', 't', 'r', 'o', 'b', 'e'], '3.552 MHz': ['b', 'i', 's', 't', 'r', 'o'], '3.555 MHz': ['f', 'l', 'i', 'c', 'k'], '3.565 MHz': ['b', 'o', 'm', 'b', 's'], '3.572 MHz': ['b', 'r', 'e', 'a', 'k'], '3.575 MHz': ['b', 'r', 'i', 'c', 'k'], '3.582 MHz': ['s', 't', 'e', 'a', 'k'], '3.592 MHz': ['s', 't', 'i', 'n', 'g'], '3.595 MHz': ['v', 'e', 'c', 't', 'o', 'r'], '3.600 MHz': ['b', 'e', 'a', 't', 's']}
    found = []
    for i1 in d:
        for i2 in d[i1]:
            found.append(d[i1].count(i2) == list(l).count(i2))
        for i2 in list(l):
            found.append(list(l).count(i2) == d[i1].count(i2))
        if set(found) == {True}:
            mc['alabel'].config(text = i1)
            return
        found = []
    mc['alabel'].config(text = '')

def cw_init():
    cw['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    cw['cframe'] = tk.Frame(cw['frame'])
    cw['r'] = tk.BooleanVar()
    cw['rcb'] = tk.Checkbutton(cw['cframe'], text = 'red', variable = cw['r'], command = cw_answer)
    cw['b'] = tk.BooleanVar()
    cw['bcb'] = tk.Checkbutton(cw['cframe'], text = 'blue', variable = cw['b'], command = cw_answer)
    cw['s'] = tk.BooleanVar()
    cw['scb'] = tk.Checkbutton(cw['cframe'], text = 'star', variable = cw['s'], command = cw_answer)
    cw['l'] = tk.BooleanVar()
    cw['lcb'] = tk.Checkbutton(cw['cframe'], text = 'LED', variable = cw['l'], command = cw_answer)

    cw['l_dep'] = tk.Label(cw['frame'], text = 'dependencies', fg = 'grey')
    cw['edep'] = Swagbutton(cw['frame'], text = '✗ even', fg = 'grey')
    cw['pdep'] = Swagbutton(cw['frame'], text = '✗ parallel port', fg = 'grey')
    cw['bdep'] = Swagbutton(cw['frame'], text = '✗ batteries', fg = 'grey')

    cw['alabel'] = tk.Label(cw['frame'])

    cw['rcb'].grid(row = 0, column = 0)
    cw['bcb'].grid(row = 0, column = 1)
    cw['scb'].grid(row = 0, column = 2)
    cw['lcb'].grid(row = 0, column = 3)
    cw['cframe'].grid(row = 0, column = 0)
    cw['l_dep'].grid(row = 1, column = 0, sticky = 'w')
    cw['edep'].grid(row = 2, column = 0, sticky = 'w')
    cw['bdep'].grid(row = 3, column = 0, sticky = 'w')
    cw['pdep'].grid(row = 4, column = 0, sticky = 'w')
    cw['alabel'].grid(row  = 1, rowspan = 4, column = 0, columnspan = 2)

    cw_answer()

def cw_answer():
    r = cw['r'].get()
    b = cw['b'].get()
    s = cw['s'].get()
    l = cw['l'].get()
    cw['edep'].deselect()
    cw['bdep'].deselect()
    cw['pdep'].deselect()
    if (not r and not b and not s and not l) or (r and not b and s and not l) or (not r and not b and s and not l):
        cw['alabel'].config(text = 'cut')
    if (not r and not b and not s and l) or (r and b and s and l) or (not r and b and s and not l):
        cw['alabel'].config(text = 'do not cut')
    if (not r and b and not s and not l) or (r and not b and not s and not l) or (r and b and not s and not l) or (r and b and not s and l):
        if pph['digit'].get() == 'even':
            cw['alabel'].config(text = 'cut')
        else: 
            cw['alabel'].config(text = 'do not cut')
        cw['edep'].select()
    if (not r and b and not s and l) or (r and b and s and not l) or (not r and b and s and l):
        if pph['pport'].get():
            cw['alabel'].config(text = 'cut')
        else: 
            cw['alabel'].config(text = 'do not cut')
        cw['pdep'].select()
    if (r and not b and not s and l) or (r and not b and s and l) or (not r and not b and s and l):
        if pph['batteries'].get() > 1:
            cw['alabel'].config(text = 'cut')
        else:
            cw['alabel'].config(text = 'do not cut')
        cw['bdep'].select()
    
def ws_init():
    ws['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    ws['l_red'] = tk.Label(ws['frame'], text = 'red')
    ws['a_red'] = tk.Label(ws['frame'])
    ws['red'] = tk.IntVar()
    ws['redrb'] = [tk.Radiobutton(ws['frame'], text = i, variable = ws['red'], value = i, command = ws_answer) for i in range(10)]
    ws['l_blue'] = tk.Label(ws['frame'], text = 'blue')
    ws['a_blue'] = tk.Label(ws['frame'])
    ws['blue'] = tk.IntVar()
    ws['bluerb'] = [tk.Radiobutton(ws['frame'], text = i, variable = ws['blue'], value = i, command = ws_answer) for i in range(10)]
    ws['l_black'] = tk.Label(ws['frame'], text = 'black')
    ws['a_black'] = tk.Label(ws['frame'])
    ws['black'] = tk.IntVar()
    ws['blackrb'] = [tk.Radiobutton(ws['frame'], text = i, variable = ws['black'], value = i, command = ws_answer) for i in range(10)]

    for i in range(10):
        ws['redrb'][i].grid(row = i+1, column = 0)
        ws['bluerb'][i].grid(row = i+1, column = 1)
        ws['blackrb'][i].grid(row = i+1, column = 2)
    ws['l_red'].grid(row = 0, column = 0)
    ws['l_blue'].grid(row = 0, column = 1)
    ws['l_black'].grid(row = 0, column = 2)
    ws['a_red'].grid(row = 11, column = 0)
    ws['a_blue'].grid(row = 11, column = 1)
    ws['a_black'].grid(row = 11, column = 2)

def ws_answer():
    red_answers = ['', 'C', 'B', 'A', 'A, C', 'B', 'A, C', 'A, B, C', 'A, B', 'B']
    blue_answers = ['', 'B', 'A, C', 'B', 'A', 'B', 'B, C', 'C', 'A, C', 'A']
    black_answers = ['', 'A, B, C', 'A, C', 'B', 'A, C', 'B', 'B, C', 'A, B', 'C', 'C']
    ws['a_red'].config(text = red_answers[ws['red'].get()])
    ws['a_blue'].config(text = blue_answers[ws['blue'].get()])
    ws['a_black'].config(text = black_answers[ws['black'].get()])

def mz_init():
    mz['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')
    mz['mframe'] = tk.Frame(mz['frame'])
    mz['circle'] = tk.StringVar()
    mz['mrb'] = [tk.Radiobutton(mz['mframe'], variable = mz['circle'], value = f'{(i//6)+1} {(i%6)+1}', command = mz_answer) for i in range(36)]
    mz['ic'] = tk.Label(mz['frame'])
    mz['img'] = tk.Label(mz['frame'])

    mz['mframe'].grid(row = 1, column = 0)
    for i in range(36):
        mz['mrb'][i].grid(row = i//6, column = i%6)
    mz['ic'].grid(row = 0, column = 0)
    mz['img'].grid(row = 2, column = 0)

def mz_answer():
    c = [int(i) for i in mz['circle'].get().split()]
    mazes = [[[2, 1], [3, 6]], [[4, 2], [2, 5]], [[4, 4], [4, 6]], [[1, 1], [4, 1]], [[3, 5], [6, 4]], [[5, 3], [1, 5]], [[1, 2], [6, 2]], [[4, 3], [1, 4]], [[5, 1], [2, 3]]]
    for i1 in mazes:
        for i2 in i1:
            if c == i2:
                img = ImageTk.PhotoImage(Image.open(f"pictures/mz/{mazes.index(i1)+1}.png").resize((200, 200)))
                mz['img'].config(image = img)
                mz['img'].image = img
                mz['ic'].config(text = '')
                return
    mz['ic'].config(text = f'invalid circle: {c}')
    
def pw_init():
    pw['frame'] = tk.Frame(frame1, borderwidth = 5, relief = 'groove')

    for i in range(1, 6):
        pw[str(i)] = tk.StringVar()
        pw[str(i)].trace_add("write", lambda a, b, c: pw_answer())
        pw['l'+str(i)] = tk.Label(pw['frame'], text = ['first', 'second', 'third', 'fourth', 'fifth'][i-1]+' letters')
        pw['e'+str(i)] = tk.Entry(pw['frame'], textvariable = pw[str(i)])
    pw['alabel'] = tk.Label(pw['frame'], wraplength = 200)

    for i in range(1, 6):
        pw['l'+str(i)].grid(row = (i-1)*2, column = 0)
        pw['e'+str(i)].grid(row = (i-1)*2+1, column = 0)
    pw['alabel'].grid(row = 10, column = 0)

def pw_answer():
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']
    options = words.copy()
    for word in words:
        check = [[True if pw[str(i2+1)].get()[i].lower() == word[i2] else False for i in range(len(pw[str(i2+1)].get()))] for i2 in range(5)]
        if (check[0].count(True) == 0 and len(check[0]) > 0) or (check[1].count(True) == 0 and len(check[1]) > 0) or (check[2].count(True) == 0 and len(check[2]) > 0) or (check[3].count(True) == 0 and len(check[3]) > 0) or (check[4].count(True) == 0 and len(check[4]) > 0):
            options.remove(word)
    if options != words:
        pw['alabel'].config(text = options) 
    else: 
        pw['alabel'].config(text = '')

root = tk.Tk()
frame1 = tk.Frame(root)

def main():
    root.title("KTANE Helper")
    root.geometry("600x500")
    frame1.place(anchor = 'center', relx = 0.5, rely = 0.5)

    init_all()
    root.mainloop()

main()
