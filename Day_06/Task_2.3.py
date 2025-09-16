import os


def lister_fichiers(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))
    return os.listdir(repertoire)


print(lister_fichiers("/Users/delly/Documents/wading_pool"))
