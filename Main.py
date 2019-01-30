
def install_import(module):
    import importlib
    try:
        importlib.import_module(module)
    except ImportError:
        import pip
        pip.main(['install',module])
        importlib.import_module(module)
    finally:
        if module=='matplotlib.pyplot':
            globals()['mp']=importlib.import_module(module)
        else:
            globals()[module]=importlib.import_module(module)



from Tkinter import *
import tkSimpleDialog
import warnings

def lim_valuesx():
    try:
        d=sympy.diff(exp,x)
        v1=sympy.solve(d)
        l=[]
        for i in v1:
            l.append(i)
        minv=-20
        maxv=20
        for i in l:
            if i>maxv:
                maxv=i
            if i<mnv:
                minv=i
        return [minv-10,maxv+10]
    except:
        return [-20,20]

def lim_y():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        vls=[-50,50]
        limiters1,limiters2=lim_valuesx()
        try:
            if numpy.isnan(lam(limiters1))==False:
                vls.append(lam(limiters1))
            if numpy.isnan(lam(limiters2))==False:
                vls.append(lam(limiters2))
        except:
            pass
        vls.sort()
        return [vls[0],vls[len(vls)-1]]


from Tkinter import *


root=Tk()
home_pg=Frame(root)
home_pg.grid()
root.title("Calculator")
i=0
bttn=[]
prompts=["Basic","Advanced","Graph","Load Function"]
btn_basic=Button(home_pg,text="Basic Calculator")
btn_basic["command"]=lambda:execfile("Basic.py",globals())
btn_basic.grid(row=1,column=1,pady=50)
btn_adv=Button(home_pg,text="Advanced Calculator")
btn_adv["command"]=lambda:execfile("adv_calc.py",globals())
btn_adv.grid(row=2,column=1,pady=50)
btn_graph=Button(home_pg,text="Grapher")
btn_graph["command"]=lambda:execfile("grapher.py",globals())
btn_graph.grid(row=3,column=1,pady=50)
btn_fnc=Button(home_pg,text="Custom Functions")
btn_fnc["command"]=lambda:execfile("Func.py",globals())
btn_fnc.grid(row=4,column=1,pady=50)
root.mainloop()
