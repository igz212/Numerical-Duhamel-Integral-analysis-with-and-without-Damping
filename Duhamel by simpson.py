import numpy as np

#-----get inital parameters from user-----
n = int(input("clarify the Amount of n? be aware...that should be even : "))
t_initial = 0
print("T_initial is : " + str(t_initial) )
t_end = float(input("clarify t_end : "))
delta_taw = (t_end - t_initial) / n

#calculate a list of t_n
t_n_list = np.linspace( t_initial, t_end, n+1)
print(t_n_list)


#to get list pf p(t) as coloumn 1
p_t_list = [] # a.k.a c1
for i in range(n+1):
    temp = float(input("what is p(" + str(i) +")? :  "))
    p_t_list.append(temp)
print(p_t_list)
c1 = p_t_list


k_hardness = float(input("now clarify the Amount of k : "))
weight = float(input("and now the weight : "))
# g = float(input("g : "))
g = 386.4 / 12
omega = np.sqrt((k_hardness * g)/weight )
m = weight / g
F = delta_taw / (3 * m * omega)

temp = input("do you have parameter Zaay? (y/n)")
zaay = 0
c = 0
if (temp.lower() == "y"):
    zaay = float(input("clarify zaay : "))
else:
    c = float(input("so clarify C : ")) #braucht Formula
    zaay = c / (2 * omega * m)

omega_d = omega * np.sqrt(1 - (zaay ** 2))
if (zaay > 0):
    F = delta_taw / (3 * m * omega_d)


M1 = 4 * np.exp(-1 * zaay * omega * delta_taw)
M2 = 1 * np.exp(-2 * zaay * omega * delta_taw)


print("delta_taw : ", delta_taw)
print("m         : ", m)
print("omega     : ", omega)
print("F         : ",F)
print("M1        : ", M1)
print("M2        : ", M2)


#to calculate column 2
c2 = []
if (zaay > 0 ):
    omega = omega_d
for i in range(n+1):
    temp = np.sin(omega * t_n_list[i])
    c2.append(temp)

print("c2 : ", c2)

#to calculate column 3
c3 = []
for i in range(n+1):
    temp = np.cos(omega * t_n_list[i])
    c3.append(temp)

print("c3 : ", c3)

#to calculate column 4
c4 = []
for i in range(n+1):
    temp = c1[i] * c3[i]
    c4.append(temp)

#to calculate column 11
c11 = []
for i in range(n+1):
    temp = c1[i] * c2[i]
    c11.append(temp)


#to calculate ~A_n_on_F
temp = c1[0] * c3[0] * M2
A_n_on_F = [temp]
for j in range(2, n+1, 2):
    temp_sum = ( c1[0]*c3[0] + c1[j] * c3[j] ) * M2
    for i in range(1, j):
        if (i % 2 == 0):
            temp_sum = temp_sum + ( 2 * M2 * c3[i] * c1[i] )
        else:
            temp_sum = temp_sum + ( M1 * c3[i] * c1[i] )
    A_n_on_F.append(temp_sum)

c18 =[]
list1 = A_n_on_F
list2 = c2[::2]
for num1, num2 in zip(list1, list2):
	c18.append(num1 * num2)

print("A_n_on_F: ", A_n_on_F)


#to calculate ~B_n_on_F
temp = c1[0] + c2[0] * M2
B_n_on_F = [temp]
for j in range(2, n+1, 2):
    temp_sum = ( c1[0]*c2[0] + c1[j] * c2[j] ) * M2
    for i in range(1, j):
        if (i % 2 == 0):
            temp_sum = temp_sum + ( 2 * M2 * c2[i] * c1[i] )
        else:
            temp_sum = temp_sum + ( M1 * c2[i] * c1[i] )
    B_n_on_F.append(temp_sum)

c19 =[]
list1 = B_n_on_F
list2 = c3[::2]
for num1, num2 in zip(list1, list2):
	c19.append(num1 * num2)

print("B_n_on_F: ",B_n_on_F)


c20 = []
zip_object = zip(c18, c19)
for c18_i, c19_i in zip_object:
    c20.append( np.abs(c18_i - c19_i) )

c21 = [ element * F for element in c20]
c22 = [ element * k_hardness for element in c21]

print("---Results---")
print("c18", c18)
print("c19", c19)
print("c20", c20)
print("c21", c21)
print("c22", c22)

f = open("results.txt","w")
f.write( "n     : " + str(n) + "\n" )
f.write( "t_ini : " + str(t_initial) + "\n" )
f.write( "t_end : " + str(t_end) + "\n" )
f.write( "zaay  : " + str(zaay) + "\n" )
f.write( "K     : " + str(k_hardness) + "\n" )
f.write( "g     : " + str(g) + "\n" )
f.write( "W     : " + str(weight) + "\n" )
f.write( "m     : " + str(m) + "\n" )
f.write( "delta : " + str(delta_taw) + "\n" )
f.write( "P(tn) : " + str(c1) + "\n" )
f.write( "M1    : " + str(M1) + "\n" )
f.write( "M2    : " + str(M2) + "\n" )
f.write( "M1    : " + str(M1) + "\n" )
f.write( "F     : " + str(F) + "\n" )
f.write( "~An/F : " + str(A_n_on_F) + "\n" )
f.write( "~Bn/F : " + str(B_n_on_F) + "\n" )
f.write( "c2    : " + str(c2) + "\n" )
f.write( "c3    : " + str(c3) + "\n" )
f.write( "c4    : " + str(c4) + "\n" )
f.write( "c11   : " + str(c11) + "\n" )
f.write( "c18   : " + str(c18) + "\n" )
f.write( "c19:  : " + str(c19) + "\n" )
f.write( "c20:  : " + str(c20) + "\n" )
f.write( "c21:  : " + str(c21) + "\n" )
f.write( "c22:  : " + str(c22) + "\n" )
f.close()