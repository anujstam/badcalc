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

import tkFileDialog,os
from Tkinter import *
import Tkinter as tk
import tkSimpleDialog
def load_file():
    currdir = os.getcwd()
    func_file = tkFileDialog.askopenfile(parent=root, initialdir=currdir, title='Please select a file')
    return func_file


def get_exp():
    exp=tkSimpleDialog.askstring("Expression","Type in equation")
    return exp




install_import('sympy')
install_import('numpy')
install_import('mpmath')
import pickle
import warnings
import matplotlib.pyplot as mp

def work_getpar():
    exp=get_exp()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        x = sympy.symbols('x')
        exp=sympy.sympify(exp)
        lam=sympy.lambdify(x,exp,modules=["numpy"])
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


    axes = mp.gca()
    xlimiters1,xlimiters2=lim_valuesx()
    limiters=lim_y()
    axes.set_ylim(limiters[0],limiters[1])
    x_vals = numpy.linspace(xlimiters1,xlimiters2,5000)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        y_vals1=[]
        for i in(x_vals):
            try:
                if lam(i)<limiters[0] or lam(i)>limiters[1]:
                    y_vals1.append(numpy.nan)
                else:
                    y_vals1.append(lam(i))
            except NameError:
                y_vals1="nonc"
        mp.figure(1)
        mp.grid(True)   
        mp.switch_backend('TkAgg')
        mp.axhline(color='black')
        mp.axvline(color='black')
        if y_vals1=="nonc":
            print "Cannot Graph. Sorry!"
        else:
           mp.plot(x_vals, y_vals1,'g',aa=True)
        mng = mp.get_current_fig_manager()
        mng.window.state('zoomed') 
        mp.show()


def work_loadpar():
    t_f=load_file()
    exp=pickle.load(t_f)
    print exp
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        x = sympy.symbols('x')
        exp=sympy.sympify(exp)
        lam=sympy.lambdify(x,exp,modules=["numpy"])
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


    axes = mp.gca()
    xlimiters1,xlimiters2=lim_valuesx()
    limiters=lim_y()
    axes.set_ylim(limiters[0],limiters[1])
    x_vals = numpy.linspace(xlimiters1,xlimiters2,5000)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        y_vals1=[]
        for i in(x_vals):
            try:
                if lam(i)<limiters[0] or lam(i)>limiters[1]:
                    y_vals1.append(numpy.nan)
                else:
                    y_vals1.append(lam(i))
            except NameError:
                y_vals1="nonc"
        
        mp.figure(1)
        mp.title(exp)
        mp.grid(True)   
        mp.switch_backend('TkAgg')
        mp.axhline(color='black')
        mp.axvline(color='black')
        if y_vals1=="nonc":
            print "Cannot Graph. Sorry!"
        else:
           mp.plot(x_vals, y_vals1,'g',aa=True)
        mng = mp.get_current_fig_manager()
        mng.window.state('zoomed') 
        mp.show()

print "Imports Complete!"
root=Tk()
graph_int=Frame(root)
graph_int.grid()
root.title("Grapher")
btn_enter1=Button(graph_int,text="Enter a function manually",command=lambda:work_getpar())
btn_enter1.grid(row=1,column=1,padx=10)
btn_enter2=Button(graph_int,text="Load a pre-existing Function",command=lambda:work_loadpar())
btn_enter2.grid(row=2,column=1,padx=10)
root.mainloop()



        
    

    
