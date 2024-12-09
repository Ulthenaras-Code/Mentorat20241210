from dataclasses import dataclass
import json
import pickle

data_dict = {"nom": "MATHIEU", "prenom": "Stephane", "profession": "Dev Python"}

#Permet d'écrire dans un fichier json
with open("data_dict.json", "w") as f:
    json.dump(data_dict, f, indent=4)

# Permet de convertir en objet json
objet_json = json.dumps(data_dict)
print(type(objet_json))

# Permet d'appeler un fichier json en dictionaire
with open("data_dict.json", "r") as f:
    data_dict_2 = json.load(f)

print(data_dict_2)
print(type(data_dict_2))

# Permet de convertir un objet json en dictionaire
data_dict_3 = json.loads(objet_json)

print(data_dict_3)
print(type(data_dict_3))

class Personnage():

    def __init__(self, nom, classe, points_de_vie):
        self.nom = nom
        self.classe = classe
        self.points_de_vie = points_de_vie

    def attaquer(self):
        if self.classe == "Guerrier":
            print("Je frappe avec mon épée")
        elif self.classe == "Magicien":
            print("Je lance un sort")

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, je suis un {self.classe}, et j'ai {self.points_de_vie} points de vie")


gandalf = Personnage("Gandalf", "Magicien", 50)
aragorn = Personnage("Aragorn", "Guerrier", 100)

with open("personnage_1.pkl", "wb") as perso:
    pickle.dump(gandalf, perso)


with open("personnage_2.pkl", "wb") as perso:
    pickle.dump(aragorn, perso)

@dataclass
class Credential():
    hote: str
    port: int
    user: str
    password: str

ma_bdd = Credential("127.0.0.1", 3306, "root", "toor123456")

print(pickle.dumps(ma_bdd))
with open("credential", "w") as data:
    data.write(pickle.dumps(ma_bdd).hex())

