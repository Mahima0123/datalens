from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = [
            'id',
            'name',
            'original_file',
            'file_type',
            'status',
            'row_count',
            'column_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'status',
            'row_count',
            'column_count',
            'created_at',
            'updated_at',
        ]