
import numpy as np
from Bio import SeqIO
import os

def getPSSM(path, fasta):
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
            final = []
            for i in range(3, 3 + len(fasta)):
                line = lines[i].rstrip().split(' ')
                line = [s for s in line if s][2:-2-20]
                final.append(line)
        return np.array(final).astype('float')
    except:
        return None

output_dir = 'data/pssm_by_protein'
os.makedirs(output_dir, exist_ok=True)

with open('data/full_sequences/all_sequence_cleaned.fasta', 'r') as fasta:
    for record in SeqIO.parse(fasta, 'fasta'):
        pdb_id = record.id
        sequence = str(record.seq)
        
        protein_dir = os.path.join(output_dir, pdb_id)
        os.makedirs(protein_dir, exist_ok=True)

        rows = getPSSM('Final dataset/all_pssms/' + pdb_id + '.pssm', sequence)
        if rows is not None:
            for i, row in enumerate(rows):
                site_file = os.path.join(protein_dir, f'site_{i+1}.npy')
                np.save(site_file, row)
            print('PSSM found and saved for', pdb_id)
        else:
            print('No PSSM found for', pdb_id)
        

        
        