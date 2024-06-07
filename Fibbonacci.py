def fibonnac(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonnac(n-1) + fibonnac(n-2)