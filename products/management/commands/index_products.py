from django.core.management.base import BaseCommand
from products.models import Product
from products.clip_search import embed_image, get_collection


class Command(BaseCommand):
    help = 'Calcola gli embedding delle foto e li salva in ChromaDB'

    def handle(self, *args, **options):
        collection = get_collection()
        for product in Product.objects.all():
            emb = embed_image(product.image.path)
            collection.upsert(ids=[str(product.pk)], embeddings=[emb])
            self.stdout.write(f'Indicizzato: {product.name}')