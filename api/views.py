from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.recommendation_service import recommendation_service as rs
class DocumentUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided."}, status=400)
        recommender = rs()
        result = recommender.recommendation_emebbeding(file)
        return Response({"message": result}, status=200)
    def get(self, request, format=None):
        query = request.GET.get('query')
        top_k = int(request.GET.get('top_k', 5))
        if not query:
            return Response({"error": "No query provided."}, status=400)
        recommender = rs()
        recommendations = recommender.get_recommendations(query, top_k)
        return Response({"recommendations": recommendations}, status=200)
    
# Create your views here.
