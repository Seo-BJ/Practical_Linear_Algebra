# CH1_연습문제
# 정답 링크 : https://github.com/Sancho-kim/LinAlg4DS

# import libraries
import numpy as np
import matplotlib.pyplot as plt


# NOTE: these lines define global figure properties used for publication.
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats('svg') # display figures in vector format
plt.rcParams.update({'font.size':14}) # set global font size

u = np.array([0,0,1])
v = np.array([1,2,3])
# 1-1



# 1-2


# the function
def normOfVect(v):
  return np.sqrt(np.sum(v*v))

# test it on a unit-norm vector

print( normOfVect(u) )

# non-unit-norm vector, and confirm using np.linalg.norm

print( normOfVect(v),np.linalg.norm(v) )


# 1-3
def unitVector(v):
  norm = np.sqrt(np.sum(v*v))
  return v / norm

print(unitVector(u), unitVector(v))

