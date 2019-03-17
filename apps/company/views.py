from django.shortcuts import render, redirect
from apps.company.forms import driverForm, busForm
from apps.company.models import Driver, Bus


# Create your views here.
def indexDriver(request):
    drivers = Driver.objects.all()

    return render(request, "company/indexDriver.html", {'drivers': drivers})


def createDriver(request):
    form = driverForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('company:indexDriver')

    return render(request, 'company/createDriver.html', {'form': form})


def editDriver(request, id_driver):
    driver = Driver.objects.get(id=id_driver)
    if request.method == 'GET':
        form = driverForm(instance=driver)
    else:
        form = driverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
        return redirect('company:indexDriver')
    return render(request, 'company/createDriver.html', {'form': form})


def deleteDriver(request, id_driver):
    driver = Driver.objects.get(id=id_driver)
    if request.method == 'POST':
        driver.delete()
        return redirect('company:indexDriver')
    return render(request, 'company/deleteDriver.html', {'driver': driver})


def indexBus(request):
    buses = Bus.objects.all()

    return render(request, "company/indexBus.html", {'buses': buses})


def createBus(request):
    form = busForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('company:indexBus')

    return render(request, 'company/createBus.html', {'form': form})


def editBus(request, id_bus):
    bus = Bus.objects.get(id=id_bus)
    if request.method == 'GET':
        form = busForm(instance=bus)
    else:
        form = busForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
        return redirect('company:indexBus')
    return render(request, 'company/createBus.html', {'form': form})


def deleteBus(request, id_bus):
    bus = Bus.objects.get(id=id_bus)
    if request.method == 'POST':
        bus.delete()
        return redirect('company:indexBus')
    return render(request, 'company/deleteBus.html', {'bus': bus})
