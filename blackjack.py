def black(a,b,c):
     summ = sum([a,b,c])
     if summ <= 21:
          return summ
     if summ > 21 and 11 in [a,b,c]:
          return (summ - 10)
     if summ > 21:
          return 'BUST'
