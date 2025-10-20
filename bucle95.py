for maikoll in range(2, 11):
    for daniel in range(2, maikoll):
        if maikoll % daniel == 0:
            break
    else:
        print(maikoll)
