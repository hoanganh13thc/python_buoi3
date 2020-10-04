# -------------Tính số fibo thứ n----------
def fibo(n):
    "Hàm tính số fibonacci"
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)
print("Nhập n:",end="")
n=int(input())
print(f"Số fibo thứ {n}: {fibo(n)}")