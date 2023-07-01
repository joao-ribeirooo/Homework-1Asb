from Bio import Entrez
import sys

# Set up email so NCBI knows who's accessing
Entrez.email = 'your.email.01@example.com'

# Define search function
def esearch(termo, database):
    handle = Entrez.esearch(db=database, term=termo, usehistory='y')
    results = Entrez.read(handle)
    handle.close()
    return results

# Define fetch function
def efetch(query_key, web_env, database):
    handle = Entrez.efetch(db=database, rettype='fasta', query_key=query_key, WebEnv=web_env)
    sequences = handle.read()
    print(sequences)
    handle.close()
    return sequences

# Term and database to search the sequences that will be inserted in the terminal
term = sys.argv[1]
database = sys.argv[2]

# Get query_key and web_env
history = esearch(term, database)
query_key = history['QueryKey']
web_env = history['WebEnv']

efetch(query_key, web_env, database)
