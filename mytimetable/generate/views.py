from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import modelformset_factory
from .forms import TotalActivitiesForm
from .models import Subject

import random
import io
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
"""
def generate_timetable(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = ['7:00','8:00','9:00', '10:00', '11:00', '12:00', '13:30', '14:30', '15:30']
    courses = Subject.objects.all()

    timetable = {}
    for day in days:
        for time in times:
            if time == '12:00':
                timetable.setdefault(day, {})[time] = 'Lunch'
            else:
                course = random.choice(courses)
                timetable.setdefault(day, {})[time] = course

    context = {
        'courses': courses,
        'timetable': timetable,
        'days': days,
        'times': times,
        'title': 'Generate',
    }
    
    # Render the timetable webpage as HTML content
    html_content = render_to_string('generate/generate.html', context)
    
    # Create a file-like buffer to receive PDF data
    buffer = io.BytesIO()
    
    # Create the PDF object
    pisa_status = pisa.CreatePDF(html_content, dest=buffer)
    
    if pisa_status.err:
        return HttpResponse('An error occurred while generating the PDF.')
    
    # Set the buffer's file pointer at the beginning
    buffer.seek(0)
    
    # Generate a file name for the PDF
    filename = 'timetable.pdf'
    
    # Create the HttpResponse object with PDF headers
    response = FileResponse(buffer, as_attachment=True, filename=filename)
    
    return response
"""
def generate_timetable(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = ['7:00','8:00','9:00', '10:00', '11:00', '12:00', '13:30', '14:30', '15:30']
    courses = Subject.objects.all()

    timetable = {}
    for day in days:
        for time in times:
            if time == '12:00':
                timetable.setdefault(day, {})[time] = 'Lunch'
            else:
                course = random.choice(courses)
                timetable.setdefault(day, {})[time] = course

    context = {
        'courses': courses,
        'timetable': timetable,
        'days': days,
        'times': times,
        'title': 'Generate',
    }
    return render(request, 'generate/generate.html', context)

def download_timetable(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = ['9:00', '10:00', '11:00', '12:00', '12:30', '13:00', '13:30', '14:00', '15:00']
    courses = Subject.objects.all()

    timetable = {}
    for day in days:
        for time in times:
            if time == '12:30' or time == '13:00' or time == '13:30':
                timetable.setdefault(day, {})[time] = 'Lunch'
            else:
                course = random.choice(courses)
                timetable.setdefault(day, {})[time] = str(course)  # Convert to string

    # Generate PDF
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    # Write timetable to PDF
    y = 750  # Initial Y position for writing
    for time in times:
        x = 50  # Initial X position for writing
        p.drawString(x, y, time)  # Write time
        x += 60  # Increment X position for writing days
        for day in days:
            if timetable[day][time] == 'Lunch':
                p.drawString(x, y, 'Lunch')  # Write lunch
            else:
                p.drawString(x, y, timetable[day][time])  # Write course
            x += 80  # Increment X position for next day
        y -= 20  # Decrement Y position for next time

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='timetable.pdf')


def home(request):
    if request.method == 'POST':
        form = TotalActivitiesForm(request.POST)
        if form.is_valid():
            form.save()
            TotalActivities_instance = form.instance
            total = TotalActivities_instance.total

            url = reverse('choose', args=(total,))
            return redirect(url)
    else:
        form = TotalActivitiesForm()

    context ={
        'form' : form,
        'title' : "Home"
    }

    return render(request, 'generate/home.html',context)

def choose(request, total):
    #Subject.objects.all().delete()
    SubjectFormSet = modelformset_factory(Subject, fields=('name','hours',), extra=total)
    courses = []


    if request.method == 'POST':
        formset = SubjectFormSet(request.POST)
        courses = formset.save()

        return redirect('generate')
    
    else:
        formset = SubjectFormSet()

    context = {
        'total': total,
        'title': "Chosen",
        'formset': formset,
        'courses' : courses,
    }

    return render(request, 'generate/choose.html', context)
