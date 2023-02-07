def add():
    try:
        result = 1 + '10'
    except:
        print("hey its an error")
    else:
        print("add went well")
        print(result)


add()
