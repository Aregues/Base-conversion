 
def X_To_Ten(x):
    return(int(Middle_Number,x))    

def Ten_To_Y(y):
    a=[0,1,2,3,4,4,5,6,7,8,9,'a','b','c','d','e','f']
    b=[]
    def_Number=Middle_Number
    while True:
        s=def_Number//y
        n=def_Number%y
        b=b+[n]
        if s==0:break
        def_Number=s
    for i in b[::-1]:
        print(a[i],end='')

while True:
    Help="欢迎使用 X-Y 进制转换器"
    print(Help)

    x=int(input("数字是几进制："))
    y=input("将数字转换为几进制：")
    Middle_Number=input("请输入你要转换的数字：")

    Middle_Number=int(X_To_Ten(x))
    Ten_To_Y(int(y))

    