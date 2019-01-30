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
n=raw_input("Enter Module Name ")
install_import(n)

