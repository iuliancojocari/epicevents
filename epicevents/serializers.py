from rest_framework import serializers
from .models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ["id", "date_created", "date_updated", "sales_contact"]

    def create(self, validated_data):
        client = Client.objects.create(
            sales_contact=self.context["request"].user, **validated_data
        )
        client.save()
        return client


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ["id", "date_created", "date_updated", "sales_contact"]

    def create(self, validated_data):
        contract = Contract.objects.create(
            sales_contact=self.context["request"].user, **validated_data
        )
        contract.save()
        return contract


class EventSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["id", "date_created", "date_updated"]

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        event.save()
        return event
