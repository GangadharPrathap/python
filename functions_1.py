def fun(s):
    if s>10:
        return
    print(s)
    fun(s+1)
fun(1)    