from django.contrib.auth.models import User
from django.db.models import Sum, Count, F
from django.shortcuts import render, redirect

from apps.company.models import Bus
from apps.sales.form import passengerForm, journeyForm, addBusForm, buyTicketForm
from apps.sales.models import Passenger, Journey, Trip, Ticket


# Create your views here.
def indexPassenger(request):
    passengers = Passenger.objects.all()

    return render(request, "sales/indexPassenger.html", {'passengers': passengers})


def createPassenger(request):
    form = passengerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('sales:indexPassenger')

    return render(request, 'sales/createPassenger.html', {'form': form})


def editPassenger(request, id_passenger):
    passenger = Passenger.objects.get(id=id_passenger)
    if request.method == 'GET':
        form = passengerForm(instance=passenger)
    else:
        form = passengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
        return redirect('sales:indexPassenger')
    return render(request, 'sales/createPassenger.html', {'form': form})


def deletePassenger(request, id_passenger):
    passenger = Passenger.objects.get(id=id_passenger)
    if request.method == 'POST':
        passenger.delete()
        return redirect('sales:indexPassenger')
    return render(request, 'sales/deletePassenger.html', {'passenger': passenger})


def indexJourney(request):
    journeys = Journey.objects.all()

    return render(request, "sales/indexJourney.html", {'journeys': journeys})

def averageJourney(request):

    #journeys = Trip.objects.filter(journey__state='1').values('journey').annotate(promedio=Sum('ticket'))

    """Ticket.objects.filter(trip__journey__origin='origen',
                          trip__journey__destination='destino'). \
        values('trip', 'trip__bus__license').annotate(
        pasajes=Count('trip'),
        chofer=F('trip__bus__driver__name')).annotate(percent=F('pasajes') * 10).filter(percent__gte='porcent')
        """


    journeys = Ticket.objects.filter(trip__journey__state='1').values('trip', 'trip__journey').annotate(pasajes=Count('trip'))

    journeys = journeys.values('trip__journey', 'pasajes').annotate(Count('trip'))

    #journeys = Ticket.objects.filter(trip__journey__state='1').values('trip__journey', 'trip__journey__origin', 'trip__journey__destination').annotate(pasajes=Count('trip'))

    #journeys = Ticket.objects.filter(trip__journey__state='1').values('trip', 'trip__journey').annotate(ps=Count('trip__journey'), pj=Sum('ps'))

    #journeys = journeys.values('jo')

    journeys = Ticket.objects.values('trip').annotate(a=Count('numSeat'))

    journeys = journeys.values('')



    print(journeys)

    return render(request, "sales/averageJourney.html", {'journeys': journeys})


def viewJourneys(request):
    trips = Trip.objects.filter(journey__state='1')
    promedio = 0

    return render(request, "sales/viewJourneys.html", {'trips': trips, 'prom': promedio})


def viewMyRedirect(request):
    if request.user.is_superuser:
        return redirect('sales:indexJourney')
    else:
        return redirect('sales:viewJourneys')

def createJourney(request):

    if request.method == 'POST':
        form = journeyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:indexJourney')
    else:
        form = journeyForm()

    return render(request, 'sales/createJourney.html', {'form': form})


def editJourney(request, id_journey):
    journey = Journey.objects.get(id=id_journey)
    if request.method == 'GET':
        form = journeyForm(instance=journey)
    else:
        form = journeyForm(request.POST, instance=journey)
        if form.is_valid():
            form.save()
        return redirect('sales:indexJourney')
    return render(request, 'sales/createJourney.html', {'form': form})


def deleteJourney(request, id_journey):
    journey = Journey.objects.get(id=id_journey)
    if request.method == 'POST':
        journey.state = 0
        journey.save()
        return redirect('sales:indexJourney')
    return render(request, 'sales/deleteJourney.html', {'journey': journey})


def addBusJourney(request, id_journey):
    journey = Journey.objects.get(id=id_journey)

    if request.method == 'POST':
        form = addBusForm(request.POST)
        if form.is_valid():
            search_trip = Trip.objects.filter(bus=request.POST['bus'], journey=request.POST['journey'])
            if search_trip.count() != 0:
                pass
            else:
                form.save()
        return redirect('sales:indexJourney')
    else:
        form = addBusForm()
        form.fields['journey'].initial = journey
        form.fields['journey'].widget.attrs['style'] = 'display:none'

    return render(request, 'sales/addBusJourney.html', {'form': form, 'journey': journey})


def buyTicket(request, id_trip):
    trip = Trip.objects.get(id=id_trip)

    form = buyTicketForm(request.POST or None)

    if request.method == 'POST':
        search_seat = Ticket.objects.filter(trip=request.POST['trip'], numSeat=request.POST['numSeat'])
        if search_seat.count() != 0:
            form.add_error('numSeat', 'Este asiento ya se encuentra ocupado.')
        else:
            search_ticket = Ticket.objects.filter(trip=request.POST['trip'], passenger=request.POST['passenger'])

            if search_ticket.count() != 0:
                form.add_error('numSeat', 'El pasajero ya ha comprado un pasaje en este viaje.')
            if form.is_valid():
                form.save()
                return redirect('sales:viewJourneys')
    else:
        form.fields['trip'].initial = trip
        form.fields['passenger'].initial = request.user.id

    form.fields['trip'].widget.attrs['style'] = 'display:none'
    form.fields['passenger'].widget.attrs['style'] = 'display:none'

    return render(request, 'sales/buyTicket.html', {'form': form, 'trip': trip})


def indexTicket(request):
    tickets = Ticket.objects.all()

    return render(request, "sales/indexTicket.html", {'tickets': tickets})


def porcentageCapacity(request):
    journeys = Journey.objects.filter(state='1').values('origin', 'destination')
    buses = None

    if request.method == 'POST':
        origen, destino = str(request.POST['journey']).split('-')
        porcent = str(request.POST['porcent'])
        print(origen, destino, porcent)

        buses = Ticket.objects.filter(trip__journey__origin=origen,
                                      trip__journey__destination=destino).\
            values('trip', 'trip__bus__license').annotate(
            pasajes=Count('trip'),
            chofer=F('trip__bus__driver__name')).annotate(percent=F('pasajes')*10).filter(percent__gte=porcent)
        print(buses)

    return render(request, 'sales/porcentageCapacity.html', {'journeys': journeys, 'buses': buses})
