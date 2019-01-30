def install_import(module):
    import importlib
    try:
        importlib.import_module(module)
    except ImportError:
        import pip
        pip.main(['install',module])
        importlib.import_module(module)
    finally:
            globals()[module]=importlib.import_module(module)

install_import('sympy')
import pickle
import Tkinter
import tkFileDialog
import tkSimpleDialog
import tkMessageBox
import os

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window
x = sympy.symbols('x')
currdir = "D:\\Rohit_anuj proj\\Final\\Functions"
func_file = tkFileDialog.askopenfile(parent=root, initialdir="D:\\Rohit_anuj proj\\Final\\Functions", title='Please select a file')
func=sympy.sympify(pickle.load(func_file))
lam=sympy.lambdify(x,func)
n=tkSimpleDialog.askfloat("Input Value","Enter the value of x")
ans=str(lam(n))
tkMessageBox.showinfo("Answer",ans)
root.mainloop()

