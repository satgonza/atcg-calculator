# ATCG Calculator
This python program outputs the number of genes in a fasta file (if genes are labeled with the ">" symbol) and outputs the % A, T, C, and G
First, we open the file using:
f = open("genes_1.fas", "r")

Next, a for loop counts the number of genes and the number of A, T, C, and G occurences:
for seq in f.readlines():
    if ">" in seq:
       genes_count+=1
    else:
       a_count = a_count+seq.count('A')
       t_count = t_count+seq.count('T')
       c_count = c_count+seq.count('C')
       g_count = g_count+seq.count('G')

f.close()


In order to calculate percentages, we divide the counts of each nucleotide over the total number of counts.
IMPORTANT! In order to return a non-integer value, we must convert at least one of the numbers in the operation into an integer. This can be done as follows:
total_count = a_count + t_count + c_count + g_count
total_count = total_count * 1.0

But there may be a more eloquent way to code this?

Finally, we calculate the proportions and print the results:
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
