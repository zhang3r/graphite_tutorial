from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.Serializer):
	pk =  serializers.IntegerField(read_only=True)

	def create(self, validated_data):
		return Quote.objects.create(**validated_data)