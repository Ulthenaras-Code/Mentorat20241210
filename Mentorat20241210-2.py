import pickle
from Mentorat20241210 import Personnage, Credential

# recupère les données depuis le fichier
with open("personnage_1.pkl", "rb") as perso:
    gandalf = pickle.load(perso)

with open("personnage_2.pkl", "rb") as perso:
    aragorn = pickle.load(perso)

gandalf.se_presenter()
gandalf.attaquer()
aragorn.se_presenter()
aragorn.attaquer()

#recupère les données depuis le stream
with open("credential", "r") as f:
    data = f.read()
    credential = pickle.loads(bytes.fromhex(data))

print(credential)
print(credential.hote)
print(credential.port)
print(credential.user)
print(credential.password)
