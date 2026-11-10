import torch
import open_clip
from PIL import Image

# 1. Crea la struttura del modello (architettura ViT-B/32), ancora "vuota"
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32')

# 2. Carica i pesi di OpenFashionCLIP dentro quella struttura
checkpoint = torch.load('weights/finetuned_clip.pt', map_location='cpu')
model.load_state_dict(checkpoint['CLIP'])
model.eval()

tokenizer = open_clip.get_tokenizer('ViT-B-32')

# 3. Prepara la foto e le frasi
image = preprocess(Image.open('media/products/pexels-dayong-tien-681073045-18257675.jpg ')).unsqueeze(0)
texts = tokenizer(['a photo of a white t-shirt',
                   'a photo of a hoodie',
                   'a photo of a red dress'])

# 4. Calcola gli embedding e la similarità
with torch.no_grad():
    image_emb = model.encode_image(image)
    text_emb = model.encode_text(texts)
    image_emb = image_emb / image_emb.norm(dim=-1, keepdim=True)
    text_emb = text_emb / text_emb.norm(dim=-1, keepdim=True)
    similarity = (image_emb @ text_emb.T)

print(similarity)