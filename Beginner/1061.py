qq1, in1 = map(str, input().split())
in2 = input().split()
qq3, in3 = map(str, input().split())
in4 = input().split()
sd = int(in1)
sh = int(in2[0])
sm = int(in2[2])
ss = int(in2[4])
ed = int(in3)
eh = int(in4[0])
em = int(in4[2])
es = int(in4[4])
if es < ss:
    em-=1
    es+=60
if em < sm:
    eh-=1
    em+=60
if eh < sh:
    ed-=1
    eh+=24
print(f"{ed - sd} dia(s)")
print(f"{eh - sh} hora(s)")
print(f"{em - sm} minuto(s)")
print(f"{es - ss} segundo(s)")