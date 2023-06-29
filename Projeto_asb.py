from Bio import Entrez
import sys

# Set up email so NCBI knows who's accesing 
Entrez.email = 'youremail@example.com'

# Term and database to search the sequences that will be inserted in the terminal
TERM = sys.argv[1]
DATABASE = sys.argv[2]

# Define search function
def esearch(TERM,DATABASE):
    handle = Entrez.esearch(db=DATABASE, term=TERM, usehistory='y')
    results = Entrez.read(handle)
    print(results)
    handle.close()
    return results

# Define fetch function
def efetch(query_key, web_env, DATABASE):
    handle = Entrez.efetch(db=DATABASE, rettype='fasta', query_key=query_key, WebEnv=web_env)
    sequences = handle.read()
    print(sequences)        
    handle.close()
    return sequences
    
# Get query_key and web_env
history = esearch(TERM, DATABASE)
query_key = history['QueryKey']
web_env = history['WebEnv']
efetch(query_key, web_env, DATABASE)
    
