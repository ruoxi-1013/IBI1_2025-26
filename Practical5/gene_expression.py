#create the gene expression dictionary
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
#print the dictionary
print("original gene expression dictionary:"+ str(gene_expression))
#add new gene to the dictionary
gene_expression["MYC"] = 11.6
#print new dictionary
print("new gene expression dictionary:" + str(gene_expression))
#import the plotting library
import matplotlib.pyplot as plt
#draw the bar chart
genes = list(gene_expression.keys())
expression_values = list(gene_expression.values())
plt.bar(genes, expression_values, color="blue")
plt.xlabel("Gene Name")
plt.ylabel("Expression Values")
plt.title("Gene Expression Values")
plt.show()
#creat a variable to print expression value
gene_to_query = "TP53"
if gene_to_query in gene_expression:
    print(gene_expression[gene_to_query])
else:
    print("The gene was not found in the dataset.")
#calculate the average value of all genes in the dataset
average = sum(gene_expression.values())/len(gene_expression)
print("The average value of all genes in the dataset is"+ str(average))