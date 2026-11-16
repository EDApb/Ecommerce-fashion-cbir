import torch
import open_clip
import chromadb
from PIL import Image
from django.conf import settings

WEIGHTS_PATH = settings.BASE_DIR / 'weights' / 'finetuned_clip.pt'
CHROMA_PATH = settings.BASE_DIR / 'chroma_db'

_model = None
_preprocess = None
_tokenizer = None


def load_model():
    """Carica il modello una sola volta e lo riusa."""
    global _model, _preprocess, _tokenizer
    if _model is None:
        _model, _, _preprocess = open_clip.create_model_and_transforms('ViT-B-32')
        checkpoint = torch.load(WEIGHTS_PATH, map_location='cpu')
        _model.load_state_dict(checkpoint['CLIP'])
        _model.eval()
        _tokenizer = open_clip.get_tokenizer('ViT-B-32')
    return _model, _preprocess, _tokenizer


def embed_image(path):
    model, preprocess, _ = load_model()
    image = preprocess(Image.open(path).convert('RGB')).unsqueeze(0)
    with torch.no_grad():
        emb = model.encode_image(image)
        emb = emb / emb.norm(dim=-1, keepdim=True)
    return emb[0].tolist()


def embed_text(text):
    model, _, tokenizer = load_model()
    tokens = tokenizer([f'a photo of a {text}'])
    with torch.no_grad():
        emb = model.encode_text(tokens)
        emb = emb / emb.norm(dim=-1, keepdim=True)
    return emb[0].tolist()


def get_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    return client.get_or_create_collection(name='products')


def search(text, k=5):
    results = get_collection().query(query_embeddings=[embed_text(text)], n_results=k)
    return [int(pk) for pk in results['ids'][0]]