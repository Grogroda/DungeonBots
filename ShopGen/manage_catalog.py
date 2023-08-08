import pandas as pd

catalog=pd.read_csv("item_catalog.txt", sep=' ', index_col=None)

def add_item():
    return None

def print_catalog():
    print(catalog)
    return None

if __name__=="__main__":
    opt=-1
    while opt!=0:
        opt=int(input("\n0 - Exit\n1 - Print Catalog\n2 - Add Item\nChoose an option: "))

        if opt==1:
            print_catalog()
        elif opt==2:
            add_item()
