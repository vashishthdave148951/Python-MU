a=10
b=0

try:
    print(a/b)
except Exception as e:
    print ("its an error",e)
finally:
    print("done!")