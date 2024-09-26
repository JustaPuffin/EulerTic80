# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python

def factorial(n):
 if n > 1:
  return n * factorial(n-1)
 return 1

def lattice_paths(n):
 binominal = [[1], [1,1], [1,2,1], [1,3,3,1]]
 if n < 2:
  return 2
 if n == 2:
  n -= 1
 elif n > 3:
  for i in range(4,n+1):
   n += 1
 for i in range(n):
  binominal.append([1,1])
  for j in range(1, len(binominal[-2]) // 2+1):
   binominal[-1].insert(j, binominal[-2][j] + binominal[-2][j-1])
   binominal[-1].insert(-j, binominal[-2][j] + binominal[-2][j-1])
  if len(binominal[-2]) % 2 == 0:
   binominal[-1].remove(max(binominal[-1]))
  #trace(binominal[-1])
 return max(binominal[-1])
 
result = lattice_paths(20)
trace(f"RESULT: {result}")


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

