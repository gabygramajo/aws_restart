# path files
path_preproinsulin = '/home/ec2-user/environment/Insulin-analysis-project/preproinsulin-seq.txt'
path_preproinsulin_clean = '/home/ec2-user/environment/Insulin-analysis-project/preproinsulin-seq-clean.txt'
path_isinsulin_clean = '/home/ec2-user/environment/Insulin-analysis-project/lsinsulin-seq-clean.txt'
path_binsulin_clean = '/home/ec2-user/environment/Insulin-analysis-project/binsulin-seq-clean.txt'
path_cinsulin_clean = '/home/ec2-user/environment/Insulin-analysis-project/cinsulin-seq-clean.txt'
path_ainsulin_clean = '/home/ec2-user/environment/Insulin-analysis-project/ainsulin-seq-clean.txt'

def character_valitation(path_file, character_cant):
    with open(path_file, 'r') as file:
         for line in file:
             return str(len(line) == character_cant)

with open(path_preproinsulin, 'r') as preproinsulin, open(path_preproinsulin_clean, 'w') as preproinsulin_clean:
    for line in preproinsulin:
        for word in line.strip().split(" "):
            if word not in ["ORIGIN", "//", "1", "61"]:
                preproinsulin_clean.write(word)

# 110 characters validation
             
print("preproinsulin 110 = " + character_valitation(path_preproinsulin_clean, 110))
             
# isinsulin write 1-24
with open(path_preproinsulin_clean, 'r') as preproinsulin_clean, open(path_isinsulin_clean, 'w') as isinsulin_clean:
     for line in preproinsulin_clean:
         isinsulin_clean.write(line[0:24])
         
print("isinsulin 24 = " + character_valitation(path_isinsulin_clean, 24))
         
# binsulin write 25-54
with open(path_preproinsulin_clean, 'r') as preproinsulin_clean, open(path_binsulin_clean, 'w') as binsulin_clean:
     for line in preproinsulin_clean:
         binsulin_clean.write(line[24:54])

print("binsulin 30 = " + character_valitation(path_binsulin_clean, 30))

# cinsulin write 55-89
with open(path_preproinsulin_clean, 'r') as preproinsulin_clean, open(path_cinsulin_clean, 'w') as cinsulin_clean:
     for line in preproinsulin_clean:
         cinsulin_clean.write(line[54:89])

print("cinsulin 35 = " + character_valitation(path_cinsulin_clean, 35))

# ainsulin write 90-110
with open(path_preproinsulin_clean, 'r') as preproinsulin_clean, open(path_ainsulin_clean, 'w') as ainsulin_clean:
     for line in preproinsulin_clean:
         ainsulin_clean.write(line[89:])

print("ainsulin 21 = " + character_valitation(path_ainsulin_clean, 21))