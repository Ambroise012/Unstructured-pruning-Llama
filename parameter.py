# from transformers import AutoModel

# model = AutoModel.from_pretrained("pruned_models/llama/magnitude-0")
# config = model.config
# print(config)

import torch
import pandas as pd

# Charger le modèle à partir du fichier .bin
model = torch.load("pruned_models/llama/magnitude-0/pytorch_model-00001-of-00002.bin", map_location=torch.device('cpu'))

# Extraire les poids des paramètres du modèle
model_weights = {}
for name, param in model.items():
    model_weights[name] = param.data.numpy()

# Convertir le dictionnaire en DataFrame
df = pd.DataFrame.from_dict(model_weights, orient='index')

# Enregistrer le DataFrame dans un fichier CSV
df.to_csv("modele_params.csv")