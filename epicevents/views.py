from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import ClientSerializer, ContractSerializer, EventSerilizer
from .permissions import (
    ClientPermissions,
    IsManager,
    ContractPermissions,
    EventPermissions,
)

from .models import Client, Contract, Event
from users.models import SALES, SUPPORT


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsManager | ClientPermissions]
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["^first_name", "^last_name", "^email"]
    filterset_fields = ["is_client", "date_created", "date_updated", "sales_contact"]

    def get_queryset(self):
        if self.request.user.team.name == SUPPORT:
            return Client.objects.filter(
                contract__event__support_contact=self.request.user
            )
        if self.request.user.team.name == SALES:
            return Client.objects.filter(sales_contact=self.request.user)
        return Client.objects.all()

    def destroy(self, request, *args, **kwargs):
        client = get_object_or_404(Client, id=self.kwargs["pk"])
        client.delete()
        return Response(
            {"detail": "Client sucessfully deleted."}, status=status.HTTP_202_ACCEPTED
        )


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsManager | ContractPermissions]
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        "^client__first_name",
        "^client__last_name",
        "^client__email",
        "^date_created",
        "^payment_due",
    ]
    filterset_fields = ["date_created", "status"]

    def get_queryset(self):
        if self.request.user.team.name == SALES:
            return Contract.objects.filter(sales_contact=self.request.user)
        elif self.request.user.team.name == SUPPORT:
            return Contract.objects.filter(event__support_contact=self.request.user)

    def destroy(self, request, *args, **kwargs):
        contract = get_object_or_404(Contract, id=self.kwargs["pk"])
        contract.delete()
        return Response(
            {"detail": "Contract successfully deleted."},
            status=status.HTTP_202_ACCEPTED,
        )


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerilizer
    permission_classes = [IsAuthenticated, IsManager | EventPermissions]
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        "^client_contract__client__first_name",
        "^client_contract__client__last_name",
        "^client_contract__client__email",
        "^event_date",
    ]
    filterset_fields = ["date_created", "event_status"]

    def get_queryset(self):
        if self.request.user.team.name == SUPPORT:
            return Event.objects.filter(support_contact=self.request.user)
        elif self.request.user.team.name == SALES:
            return Event.objects.filter(client_contract__sales_contact=self.request.user)
        return Event.objects.all()

    def destroy(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=self.kwargs["pk"])
        event.delete()
        return Response(
            {"detail": "Event successfully deleted."}, status=status.HTTP_202_ACCEPTED
        )

