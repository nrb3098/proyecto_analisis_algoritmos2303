import csv

def tweets_to_csv(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Usuario', 'ID del tweet', 'Contenido'])  # Encabezado del CSV

        for line in infile:
            line = line.strip()
            if '\t' not in line:  # Verificar si la línea contiene un tabulador
                continue  # Si no lo contiene, saltar la línea

            tweet_id, tweet_content = line.split('\t')
            user = input_filename.split('_')[1].split('.')[0]  # Extraer el nombre de usuario del nombre del archivo
            csv_writer.writerow([user, tweet_id, tweet_content])

if __name__ == "__main__":
    tweets_to_csv("tweets_JDOviedoA.txt", "tweets_JDOviedoA.csv")
    tweets_to_csv("tweets_GustavoBolivar.txt", "tweets_GustavoBolivar.csv")
    tweets_to_csv("tweets_Nicolas_ramos_b.txt", "tweets_Nicolas_ramos_b.csv")
    tweets_to_csv("tweets_Rodrigo_Lara_.txt", "tweets_Rodrigo_Lara_.csv")
    tweets_to_csv("tweets_Diego_Molano.txt", "tweets_Diego_Molano.csv")
    tweets_to_csv("tweets_JERobledo.txt", "tweets_JERobledo.csv")
    tweets_to_csv("tweets_CarlosFGalan.txt", "tweets_CarlosFGalan.csv")
    tweets_to_csv("tweets_ElGeneralVargas.txt", "tweets_ElGeneralVargas.csv")