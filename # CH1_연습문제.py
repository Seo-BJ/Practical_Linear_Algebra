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

# 1-2 벡터 Norm 계산

# the function
def normOfVect(v):
  return np.sqrt(np.sum(v*v))

# test it on a unit-norm vector

print("1-2 정답")
print( normOfVect(u) )
# non-unit-norm vector, and confirm using np.linalg.norm
print( normOfVect(v),np.linalg.norm(v) )


# 1-3 단위 벡터 생성
def unitVector(v):
  norm = np.sqrt(np.sum(v*v))
  return v / norm

print("1-3 정답")
print(unitVector(u), unitVector(v))

# 1-4 임의의 크기의 벡터 생성
def setVectorSize(v, norm):
  unitV = v / np.sqrt(np.sum(v*v))
  return unitV * norm

print("1-4 정답")
print(setVectorSize(u, 3), setVectorSize(v, 1))


# 1-5 행벡터를 열벡터로 전치하는 for 루프 작성
def transposeVector(v):
  result = []
  for i in v:
    result.append([i])
  return np.array(result)

print("1-5 정답")
print(u)
print(transposeVector(u))
print(v)
print(transposeVector(v))

# 1-6 벡터의 제곱 Norm은 벡터 자체의 내적과 같다

# some vector
c = np.random.randn(5)

# squared norm as dot product with itself
sqrNrm1 = np.dot(c,c)

# squared norm via our function from exercise 1
sqrNrm2 = normOfVect(c)**2

# print both to confirm they're the same
print("1-6 정답")
print( sqrNrm1 )
print( sqrNrm2 )
     

# 1-7 내적의 교환법칙 증명
a = np.random.randn(3)
b = np.random.randn(3)

print("1-7 정답")
print(np.dot(a,b), np.dot(b,a))

# 1-8 

# the vectors a and b
a = np.array([1,2])
b = np.array([1.5,.5])

# compute beta
beta = np.dot(a,b) / np.dot(a,a)

# compute the projection vector (not explicitly used in the plot)
projvect = b - beta*a


# draw the figure
plt.figure(figsize=(4,4))

# vectors
plt.arrow(0,0,a[0],a[1],head_width=.2,width=.02,color='k',length_includes_head=True)
plt.arrow(0,0,b[0],b[1],head_width=.2,width=.02,color='k',length_includes_head=True)

# projection vector
plt.plot([b[0],beta*a[0]],[b[1],beta*a[1]],'k--')

# projection on a
plt.plot(beta*a[0],beta*a[1],'ko',markerfacecolor='w',markersize=13)

# make the plot look nicer
plt.plot([-1,2.5],[0,0],'--',color='gray',linewidth=.5)
plt.plot([0,0],[-1,2.5],'--',color='gray',linewidth=.5)

# add labels
plt.text(a[0]+.1,a[1],'a',fontweight='bold',fontsize=18)
plt.text(b[0],b[1]-.3,'b',fontweight='bold',fontsize=18)
plt.text(beta*a[0]-.35,beta*a[1],r'',fontweight='bold',fontsize=18)
plt.text((b[0]+beta*a[0])/2,(b[1]+beta*a[1])/2+.1,r'(b-a)',fontweight='bold',fontsize=18)

# some finishing touches
plt.axis('square')
plt.axis([-1,2.5,-1,2.5])
plt.show()

# 1-9 직교벡터 분해 구현

t = np.random.randn(2)
r = np.random.randn(2)

parallel = (np.dot(t,r))/(np.dot(r,r)) * r
perpendicular = t - parallel

print("1-9 정답")
print(t)
print(parallel + perpendicular)
print(np.dot(parallel, perpendicular))