responses=["Welcome to smart calculator","Hello my name is Xarvis","Thank You For Using Me ","Sorry sir this will not work"]
def extract_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def lcm(a,b):
    h=a if a>b else b
    while h<=a*b:
        if h%a==0 and h%b==0:
            return h
        h+=1
def hcf(a,b):
    h=a if a<b else b
    while h>1:
        if a%h==0 and b%h==0:
            return h
        h-=1
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def who():
    print("You Forgot, I am Xarvis a smart calculator")
def help():
    print("I am a calculator which can understand english language\n")
    print("I can perform \naddition,subtraction,multiplication,division,hcf,lcm")
def end():
    print(responses[2])
    input("press enter key")
    exit()

operations={"PLUS":add,"ADDITION":add,"ADD":add,"MINUS":sub,"SUBTRACT":sub,"SUB":sub,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"MULTIPLE":multiply,"INTO":multiply,"DIVIDE":division,"DIVISION":division,"HCF":hcf,"LCM":lcm}
commands={"NAME":myname,"WHO":who,"END":end,"CLOSE":end,"EXIT":end,"HELP":help}
