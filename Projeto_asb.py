from Bio import Entrez

# Set up email so NCBI knows who's accesing 
Entrez.email = 'jcrribeiro1010@gmail.com'

# Term and database to search the sequences
TERM = "Psammodromus algirus[organism], cytb[gene]"
DATABASE = 'nucleotide'

# Define search function
def esearch():
    handle = Entrez.esearch(db=DATABASE, term=TERM, usehistory='y')
    results = Entrez.read(handle)
    print(results)
    handle.close()
    return results

# Get query_key and web_env
history = esearch()
query_key = history['QueryKey']
web_env = history['WebEnv']

# Print of the querykey and webenv
def history():
    
    print(query_key, web_env)

history()

# Define fetch function
def efetch(query_key, web_env):
    handle = Entrez.efetch(db=DATABASE, rettype='fasta', query_key=query_key, WebEnv=web_env)
    sequences = handle.read()
    print(sequences)

# Open the file to write the sequences
    with open("sequences.fasta", "w") as f:
        f.write(sequences)
        
    handle.close()
    return sequences

efetch(query_key, web_env)

