def askint():
    try:
        val = int(input("enter interger number"))
    except Exception as e:
        print("you have not entered an integer")
        try:
            val = int(input("enter integer num"))
        except:
            print("we are able to handle your mistake second time")
        finally:
            print("finally will execute anyhow")
askint()