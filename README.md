# Homework
code and readme file for ASB Homework

**Introduction**

We made a code that transform Fasta file into Nexus file and then, we tested each function using pytest.

**Code usage in terminal:**

Converter.py:
```python Converter.py <fasta_file>```

test_Converter.py:
```python test_Converter.py <fasta_file>```

**Function's functionallity**

Function read_file(fasta_file)
```
def read_fasta(fasta_file): #this function takes a fasta file you want to read
    sequences = {} '''it starts with an empty dictionary called sequences to store the name as a key, and the sequences as a value'''
    with open(fasta_file, 'r') as f: # opens file in read mode
        for line in f: #iterates wach line of the file 
            if line.startswith('>'):   #If the line starts with ">", represents the header line for a sequence
                name = line.strip()[1:] #this line extracts everything after the ">" character
                sequences[name] = '' #it stablishes a connection between 'name' as a key and '' as a value
            else:
                sequences[name] += line.strip() '''If the line doesn't start with '>', the function adds the line as value to the "name" key'''
    return sequences #returns dictionary with the names and sequences.
```
Function make_nexus_data_header(sequences)
```
def make_nexus_data_header(sequences): #this function accepts the dictionary 'sequences' as input
    nexus_data_header = 'NEXUS\nBEGIN DATA;\nDIMENSIONS NTAX=' + str(len(sequences)) + ' NCHAR=' + str(len(sequences[list(sequences.keys())[0]])) + ';\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n' '''String that represents the header of a NEXUS format, in which calculates the number of taxas "NTAX" by counting the length of the dictionary. The number of characters "NCHAR" counts the number of nucleotides in each sequence'''
    return nexus_data_header #returns data header in String format
```
function make_nexus_matrix(sequences)
```
def make_nexus_matrix(sequences): #this function accepts the dictionary mentioned before
    nexus_matrix = '' #it starts with an empty String named nexus matrix 
    for name, sequence in sequences.items(): #for loop to interate through key and value in the dictionary
        nexus_matrix += name + ' ' + sequence + '\n' '''String that combine the name of the sequence and the sequence itself'''
    return nexus_matrix 
```
function make_nexus_file(sequences)
```
def make_nexus_file(sequences): #Another function that takes as input the 'sequences' dictionary
    nexus_file = make_nexus_data_header(sequences) + make_nexus_matrix(sequences) + 'END;\n' '''This line combines the nexus header and matrix and 'END;' to define the limit of the NEXUS file'''
    print(nexus_file) #Prints the nexus file to the system output 
    return nexus_file #returns the nexus_file completed.
```
main function
```
if len(sys.argv) < 2: #checks if the length of the sys.argv is less than 2
    print("Usage: python Converter.py <fasta_file>") '''Tutorial of how to use the python converter in the commandline interface'''
    sys.exit(1) #termination of the script
```
