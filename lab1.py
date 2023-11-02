#牛顿环
# m：16-20 n:26-30
Dn,Dm = [],[] # Dn : 第m个环的直径
Dln,Dlm = [],[] # Dln: 第m个环左侧的数据
Drn,Drm = [],[] # Drm：第m个环右侧的数据
for i in range(5):
    print(16+i)
    print("L:",end = " ")
    Dln.append(float(input()))
    print("R:",end = " ")
    Drn.append(float(input()))
    print(26+i)
    print("L:",end = " ")
    Dlm.append(float(input()))
    print("R:",end = " ")
    Drm.append(float(input()))
print("请核对原始数据：")
print("16-20\nL:",Dln,"\nR:",Drn,"\n26-30\nL:",Dlm,"\nR:",Drm)

sqD1,sqD2 = [],[]

for i in range(5):
    Dn.append(Dln[i] - Drn[i])
    sqD1.append(Dn[i] ** 2)
    Dm.append(Dlm[i] - Drm[i])
    sqD2.append(Dm[i] ** 2)
print("\n下面输出环的直径与环直径的平方")
print("16-20\n",Dn,"\n",sqD1,"\n26-30\n",Dm,"\n",sqD2)

D_ = [abs(sqD1[i] - sqD2[i]) for i in range(5)]

Dsum = 0
print("对应位置直径平方差：\n",D_)
for i in D_:
    Dsum += i
D_avg = Dsum/5 # D_avg 平方差的平均数

print("平方差的平均数\nD_avg:",D_avg,"\n平方差之和\nsum",Dsum)

print("\n\n**计算曲率半径**")

print("R_avg = D_avg / (40 * 589.3) * 1e-3 = ",D_avg / (40 * 589.3) * 1e3)

print("\n\n**计算A类不确定度**")

sum = 0.0
for i in range(5):
    sum += (D_[i] - D_avg)**2

c = 4*(40*589.3*10**-3)**2  

result = (sum/c)**0.5 * 1.204

print("不确定度:",result)