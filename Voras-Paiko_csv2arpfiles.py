import csv

def convert_csv_to_arp(csv_file, arp_file):
    #diavazei data apo .csv arxeia 
    sample_data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        sample_data = list(reader)

    with open(arp_file, 'w') as file:
        # kanei write ta sections
        file.write("[Profile]\n")
        file.write("Title=\"fagus almopia\"\n")
        file.write("NbSamples=2\n")
        file.write("DataType=MICROSAT\n")
        file.write("GenotypicData=1\n")
        file.write("GameticPhase=0\n")
        file.write("LocusSeparator=WHITESPACE\n\n")

        
        file.write("[Data]\n")

        # duo listes gia ta vouna ksexwrista
        voras_data = []
        paiko_data = []

        for sample_row in sample_data:
            population = sample_row['Population']
            tree = sample_row['Tree']
            genotypes = [sample_row[key] for key in sample_row.keys() if key.startswith('GOT') or key.startswith('FIR') or key.startswith('FcC')]
            sample_size = len(genotypes)

            if population == 'Voras':
                voras_data.append((tree, genotypes))
            elif population == 'Paiko':
                paiko_data.append((tree, genotypes))

        
        file.write("[[Samples]]\n")
        file.write("SampleName='Voras'\n")
        file.write("SampleSize={}\n".format(len(voras_data)))
        file.write("SampleData={\n")

        for data in voras_data:
            tree = data[0]
            genotypes = data[1]

            file.write("\t{}\t{}\n".format(tree, ' '.join(genotypes[::2])))
            file.write("\t\t{}\n".format(' '.join(genotypes[1::2])))

        file.write("}\n\n")

        
        file.write("[[Samples]]\n")
        file.write("SampleName='Paiko'\n")
        file.write("SampleSize={}\n".format(len(paiko_data)))
        file.write("SampleData={\n")

        for data in paiko_data:
            tree = data[0]
            genotypes = data[1]

            file.write("\t{}\t{}\n".format(tree, ' '.join(genotypes[::2])))
            file.write("\t\t{}\n".format(' '.join(genotypes[1::2])))

        file.write("}\n\n")

    print("Conversion completed successfully.")


csv_file = '/content/data_fagus_almopia.csv'


arp_file = '/content/data_fagus_almopia.arp'


convert_csv_to_arp(csv_file, arp_file)
