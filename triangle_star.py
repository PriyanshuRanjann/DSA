def right_triangle():
    try:
        for i in range (0,5):
            i=i+1
            print(i*"*")
    except Exception as e:
        raise e
if __name__=="__main__":
    right_triangle()