for dan in range(2,5+1):
    if dan == 7:
        break
    print("------------")
    for i in range(1,9+1):
        print("%dx%d = %d" % (dan,i,dan*i))