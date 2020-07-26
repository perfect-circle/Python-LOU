import sys

try:
    len(sys.argv) == 2
    gz = int(sys.argv[1])
    s_gz = gz - 5000
    if s_gz <= 3000:
        ns = s_gz * 0.03 - 0
    if s_gz > 3000 and s_gz <= 12000:
        ns = s_gz * 0.1 - 210
    if s_gz > 12000 and s_gz <= 25000:
        ns = s_gz * 0.2 - 1410
    if s_gz > 25000 and s_gz <= 35000:
        ns = s_gz * 0.25 - 2660
    if s_gz > 35000 and s_gz <= 55000:
        ns = s_gz * 0.3 - 4410
    if s_gz > 55000 and s_gz <= 80000:
        ns = s_gz * 0.35 - 7160
    if s_gz > 800000:
        ns = s_gz * 0.45 - 15160
    print("%.2f" % ns)
except:
    print("Parameter Error")
