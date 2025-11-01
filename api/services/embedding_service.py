from openai import OpenAI
client=OpenAI(api_key='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')
class embedding_service:
    def get_embedding(self,text,model="text-embedding-3-small"):
        response=client.embeddings.create(
            model=model,
            input=text
        )
        return response['data'][0]['embedding']