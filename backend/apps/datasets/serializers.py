from pathlib import Path
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
            'file_type',
            'status',
            'row_count',
            'column_count',
            'created_at',
            'updated_at',
        ]

    def validate_original_file(self, value):
        extension = Path(value.name).suffix.lower()

        allowed_extensions = {
            ".csv": "csv",
            ".xlsx": "xlsx",
            ".xls": "xls",
        }

        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Unsupported file type. Please upload a CSV or Excel file."
            )

        max_size = 50 * 1024 * 1024  # 50 MB
        if value.size > max_size:
            raise serializers.ValidationError(
                "File size exceeds the maximum limit of 50 MB."
            )
        return value

    def create(self, validated_data):
        file = validated_data['original_file']
        extension = Path(file.name).suffix.lower()

        file_type = {
            ".csv": "csv",
            ".xlsx": "xlsx",
            ".xls": "xls",
        }[extension]

        validated_data['file_type'] = file_type
        return super().create(validated_data)