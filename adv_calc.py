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


class adv_calc():
    def __init___(self):
        self.exp=""
        self.op=""
    def display(self,s):
        tkMessageBox.showinfo("Answer",s)
    def do_stuff(self,op):
        if op=="derivative":
            st=tkSimpleDialog.askstring("Expression","Enter function you wish to derivate")
            self.exp=sympy.diff(sympy.sympify(st),x)
            self.display(self.exp)
        if op=="integrate":
            st=tkSimpleDialog.askstring("Expression","Enter function you wish to derivate")
            self.exp=sympy.integrate(sympy.sympify(st),x)
            self.display(self.exp)
        if op=="solve":
            st=tkSimpleDialog.askstring("Expression","Enter the polynomial in x")
            self.exp=sympy.solve(sympy.sympify(st))
            self.display(self.exp)
        if op=="sin":
            st=tkSimpleDialog.askstring("Sine Value","Enter X (in radians)")
            num=eval(st)
            self.exp=sin(num)
            self.display(self.exp)
        if op=="cos":
            st=tkSimpleDialog.askstring("Cosine Value","Enter X (in radians)")
            try:
                num=eval(st)
                self.exp=cos(num)
                self.display(self.exp)
            except:
                pass
        if op=="tan":
            st=tkSimpleDialog.askstring("Tangent Value","Enter X (in radians)")
            try:
                num=eval(st)
                self.exp=tan(num)
                self.display(self.exp)
            except:
                pass
        if op=="cot":
            st=tkSimpleDialog.askstring("Cotangent Value","Enter X (in radians)")
            num=eval(st)
            self.exp=1/tan(num)
            self.display(self.exp)
        if op=="sec":
            st=tkSimpleDialog.askstring("Secant Value","Enter X (in radians)")
            num=eval(st)
            self.exp=1/cos(num)
            self.display(self.exp)
        if op=="cosec":
            st=tkSimpleDialog.askstring("Cosecant Value","Enter X (in radians)")
            num=eval(st)
            self.exp=1/sin(num)
            self.display(self.exp)
            
        if op=="asin":
            st=tkSimpleDialog.askstring("Sin Inverse Value","Enter X")
            num=eval(st)
            self.exp=asin(num)
            self.display(self.exp)
        
        if op=="acos":
            st=tkSimpleDialog.askstring("Cos Inverse Value","Enter X")
            num=eval(st)
            self.exp=acos(num)
            self.display(self.exp)
            
        if op=="atan":
            st=tkSimpleDialog.askstring("Tan Inverse Value","Enter X")
            num=eval(st)
            self.exp=atan(num)
            self.display(self.exp)
        

        
        

from Tkinter import *
import warnings
import  tkSimpleDialog
import tkMessageBox
from math import *
install_import('sympy')
install_import('numpy')
x=sympy.symbols('x')
root=Tk()
calc=Frame(root)
calc.grid()
root.title("Advanced Calculator")
run=adv_calc()
bttn_d=Button(calc,text="Derivative")
bttn_d["command"]=lambda: run.do_stuff("derivative")
bttn_d.grid(row=1,column=1,pady=10,padx=10)
bttn_i=Button(calc,text="Integrate")
bttn_i["command"]=lambda: run.do_stuff("integrate")
bttn_i.grid(row=1,column=2,pady=10,padx=10)
bttn_solve=Button(calc,text="Solve Polynomial")
bttn_solve["command"]=lambda: run.do_stuff("solve")
bttn_solve.grid(row=1,column=3,padx=10,pady=10)
bttn_s=Button(calc,text="Sine")
bttn_s["command"]=lambda: run.do_stuff("sin")
bttn_s.grid(row=2,column=1,padx=10,pady=10)
bttn_c=Button(calc,text="Cos")
bttn_c["command"]=lambda: run.do_stuff("cos")
bttn_c.grid(row=2,column=2,padx=10,pady=10)
bttn_t=Button(calc,text="Tan")
bttn_t["command"]=lambda: run.do_stuff("tan")
bttn_t.grid(row=2,column=3,padx=10,pady=10)
bttn_cot=Button(calc,text="Cot")
bttn_cot["command"]=lambda: run.do_stuff("cot")
bttn_cot.grid(row=3,column=3,padx=10,pady=10)
bttn_sec=Button(calc,text="Sec")
bttn_sec["command"]=lambda: run.do_stuff("sec")
bttn_sec.grid(row=3,column=2,padx=10,pady=10)
bttn_cosec=Button(calc,text="Cosec")
bttn_cosec["command"]=lambda: run.do_stuff("cosec")
bttn_cosec.grid(row=3,column=1,padx=10,pady=10)
bttn_asin=Button(calc,text="Sin^-1")
bttn_asin["command"]=lambda: run.do_stuff("asin")
bttn_asin.grid(row=4,column=1,padx=10,pady=10)
bttn_acos=Button(calc,text="Cos^-1")
bttn_acos["command"]=lambda: run.do_stuff("acos")
bttn_acos.grid(row=4,column=2,padx=10,pady=10)
bttn_atan=Button(calc,text="Tan^-1")
bttn_atan["command"]=lambda: run.do_stuff("atan")
bttn_atan.grid(row=4,column=3,padx=10,pady=10)
root.mainloop()
