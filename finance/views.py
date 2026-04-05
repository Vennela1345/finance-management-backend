from rest_framework import generics, permissions
from .models import Record
from .serializers import RecordSerializer

class RecordListCreateView(generics.ListCreateAPIView):
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Record.objects.filter(user=self.request.user)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
