from django.db.models import Count
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *


'''
Flight Views
'''
class FlightListAPIView(generics.ListAPIView):
    """
    List of flights using GET method
    """
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class FlightSearchAPIView(generics.ListAPIView):
    """
    Search flights by origin, destination and dates
    """
    serializer_class = FlightSerializer

    def get_queryset(self):
        # Get parameters from request
        origin = self.request.query_params.get('origin', None)
        destination = self.request.query_params.get('destination', None)
        departure_date = self.request.query_params.get('departure_date', None)

        # Filter flights by search parameters
        queryset = Flight.objects.all()

        if origin:
            queryset = queryset.filter(origin__icontains=origin)

        if destination:
            queryset = queryset.filter(destination__icontains=destination)

        if departure_date:
            queryset = queryset.filter(departure_date__date=departure_date)

        return queryset


class TopReservationsAPIView(generics.ListAPIView):
    """
    Get the list of airlines with the most reservations
    """  
    serializer_class = TopReservationsSerializer

    def get_queryset(self):
        
        return (
            Flight.objects
            .values('airline') # Like SELECT DISTINCT in SQL. Returns a list of airlines
            .annotate(total_reservations=Count('reservation')) # Add a new field and count reservation model instances
            .order_by('-total_reservations')[:15] # DESC
        )
    

class CountAirlinesAPIView(generics.ListAPIView):
    """
    Get the list of airlines with the most reservations
    """
    def get(self, request, *args, **kwargs):
        count_airline = Flight.objects.values('airline').annotate(count=Count('airline')) # dict with airline and count

        return Response({
            'number_of_airlines': len(count_airline),
        })


class FlightCreateAPIView(generics.CreateAPIView):
    """
    Create a flight using POST method
    """
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()

    def perform_create(self, serializer):
        # Validate that the arrival date is not earlier than the departure date
        departure_date = serializer.validated_data['departure_date']
        arrival_date = serializer.validated_data['arrival_date']
        price = serializer.validated_data['price']

        if arrival_date < departure_date:
            raise serializers.ValidationError("The arrival date cannot be before the departure date.")
        
        if price < 0:
            raise serializers.ValidationError("Price must be a positive number")
        
        # Object creation
        super().perform_create(serializer)


class FlightRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a flight using GET method
    """
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class FlightDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a flight using DELETE method
    """
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


'''
User Views
'''
class UserCreateAPIView(generics.CreateAPIView):
    """
    Create a user using POST method
    """
    serializer_class = UserSerializer


'''
Reservation Views
'''

class ReservationCreateAPIView(generics.CreateAPIView):
    """
    Create a reservation using POST method
    """
    serializer_class = ReservationSerializer