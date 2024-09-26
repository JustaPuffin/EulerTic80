# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python




def prime_sum(limit):
 primes = {2}
 skip = set()
 for i in range(3,limit,2):
  if i in skip:
   continue
  for j in primes:
   if i % j == 0:
    break
   if i > j // 2:
    primes.add(i)
    for k in range(i*3, limit, i*2):
     skip.add(k)
    break
 return sum(primes)
 '''20k = 7.3 s
 primes = {2}
 for i in range(3,limit,2):
  primes.add(i)
 for p in list(primes)[1::]:
  for i in range(p*3,max(primes),p*2):
   primes.discard(i)
 return sum(primes)
 '''
 

trace(f"RESULT: {prime_sum(2000000)}")

if time() < 1000:
 trace(f"TIME  : {time()} ms")
elif time() < 60000:
 trace(f"TIME  : {time()/1000:.2f} s")
elif time() < 3600000:
 trace(f"TIME  : {time()/60000:.2f} min")
else:
 trace(f"TIME  : {time()/3600000:.2f} h")

def TIC():
 exit()

# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>

