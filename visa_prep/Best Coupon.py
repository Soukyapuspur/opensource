X = int(input())
after_10_percent_dis = X - (0.10*X)
after_100_percent_dis = X-100
r=min(after_10_percent_dis,after_100_percent_dis)
print(int(r))
