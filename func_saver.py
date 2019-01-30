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
import warnings
import pickle
import os
print "Imports Complete!"
import tkSimpleDialog
s=tkSimpleDialog.askstring("Create","Enter your function ")
filename=tkSimpleDialog.askstring("Name","Name your function ")
x = sympy.symbols('x')
f=open('%s.dat'% filename,'wb')
pickle.dump(s,f)
f.close()
 
    

