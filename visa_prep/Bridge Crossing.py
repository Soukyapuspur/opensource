X,Y,Z=map(int,input().split())
mangoes_w=Z-Y
max_mangoes_can_be_loaded = mangoes_w // X
print(max_mangoes_can_be_loaded)
