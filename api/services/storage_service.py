from api.models import fileupload
# from pinecone import PineconeClient
import pinecone
pineconeapi_key="pcsk_5rusEE_UjCevPWD6mAu7tqR9qHYVcYUWTr2ygwwoXpuETLZK4D4JvYyv7NQrM1SzE5TVnT"
# client = PineconeClient(pineconeapi_key)
class pinecone_service:
    def __init__(self,  index_name: str, dimension: int, environment: str = "us-east-1"):
        pinecone.init(api_key=pineconeapi_key, environment=environment)
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(name=index_name, dimension=dimension, metric="cosine")
        self.index = pinecone.Index(index_name)
    def document_upsert(self,doc_id:str,embedding:list,content:str,title:str):
        doc = fileupload.objects.create(title=title, file=fileupload, content=content)
        self.index.upsert(str(doc_id), embedding, metadata={"content": content,"title":title})
        return doc
    def document_query(self, query_embedding: list, top_k: int):
        # Perform similarity search in Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        return results