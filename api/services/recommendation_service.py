from api.services import document_service as ds
import tempfile
import os
from api.services.embedding_service import embedding_service as es
from api.services.storage_service import pinecone_service as ps
from api.models import fileupload as fu
class recommendation_service:
    def recommendation_emebbeding(self,file):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name

        docs_extractor=ds.extarctor(temp_file_path)
        if docs_extractor.file_ext=='.pdf':
            document_text=docs_extractor.is_file_extractor_pdf()
        elif docs_extractor.file_ext=='.docx':
            document_text=docs_extractor.is_file_extractor_docx()
        else:
            document_text="Unsupported file format"
        embedding = es()
        document_embedding = embedding.get_embedding(document_text)
        ps.document_upsert(file.name, document_embedding, content=document_text, title=file.name)   
        file_record=fu(
            inputfile=file,
            inputfile_name=file.name,
            inputfile_content=document_text,
            inputfile_author="Unknown"
        )
        file_record.save()
        os.remove(temp_file_path)
        return "File processed and embedding stored successfully."
    def get_recommendations(self,query,top_k=5):
        query_embedding=es.get_embedding(query)
        recommended_files=ps.document_query(query_embedding,top_k)
        return recommended_files