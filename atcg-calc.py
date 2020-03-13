a_count = 0
t_count = 0
c_count = 0
g_count = 0

genes_count = 0

f = open("genes_1.fas", "r")

for seq in f.readlines():
    if ">" in seq:
       genes_count+=1
    else:
       a_count = a_count+seq.count('A')
       t_count = t_count+seq.count('T')
       c_count = c_count+seq.count('C')
       g_count = g_count+seq.count('G')

f.close()

total_count = a_count + t_count + c_count + g_count
total_count = total_count * 1.0

a_prop = round(a_count/total_count, 2)
t_prop = round(t_count/total_count, 2)
c_prop = round(c_count/total_count, 2)
g_prop = round(g_count/total_count, 2)

print("The total number of genes is: ", genes_count)                          
print("The file contains:")
print(a_prop, "% A ")
print(t_prop, "% T ")
print(c_prop, "% C ")
print(g_prop, "% G ")


