from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Report, Home_image, Gallery, Gallery_image, Visitor_counter

def Increment_visitor_counter(viewname):
    visitor_counter = Visitor_counter.objects.all().get(name=viewname)
    visitor_counter.count += 1
    visitor_counter.save()

def Home(request):
    Increment_visitor_counter('home')

    event = Event.objects.get(id=1)
    event_text = ''
    if event.show:
        event_text = event.text

    reports = Report.objects.all()
    sorted_reports = reports.order_by('date').reverse()

    home_photos = Home_image.objects.all()
    home_photo_active = home_photos.get(id=1)
    home_photos = home_photos.exclude(id=1)

    galleries = Gallery.objects.all()

    context = {'event': event_text, 'reports': sorted_reports, "home_photo_active": home_photo_active, 'home_photos': home_photos, 'galleries': galleries}
    return render(request, "home.html", context)

def Klub(request):
    Increment_visitor_counter('klub')

    galleries = Gallery.objects.all()

    context = {'galleries': galleries}
    return render(request, "klub.html", context)

def Historie(request):
    Increment_visitor_counter('historie')

def Galerie(request, url):
    Increment_visitor_counter('galerie')

    galleries = Gallery.objects.all()

    contains = False
    for gallery in galleries:
        if url == gallery.name or url == gallery.name.lower():
            curr_galerry_name = gallery.name
            contains = True
            break

    if contains == False:
        message = 'Galerie ' + url + ' na našem webu neexistuje, zkuste to znovu.'
        return render(request, "error.html", {'message': message})

    gallery = Gallery.objects.get(name=curr_galerry_name)
    gallery_images = gallery.gallery_image_set.all()

    context = {'gallery_name': gallery.name, 'gallery_images': gallery_images, 'galleries': galleries}
    return render(request, "gallery.html", context)

def GalerieViews(request, url1, url2):
    galleries = Gallery.objects.all()

    gallery = Gallery.objects.get(name=url1)
    gallery_images = gallery.gallery_image_set.all()

    i = 0
    for img in gallery_images:
        if img.image.name == url2:
            curr_img = img
            prev = i-1
            next = i+1
            break
        i += 1

    if (prev < 0):
        prev_img = gallery_images[len(gallery_images)-1]
    else:
        prev_img = gallery_images[prev]

    if (next > len(gallery_images)-1):
        next_img = gallery_images[0]
    else:
        next_img = gallery_images[next] 

    context = {'gallery_name': gallery.name, 'galleries': galleries, 'gallery_images': gallery_images, 'curr_img': curr_img, 'prev_img': prev_img, 'next_img': next_img}
    return render(request, "gallerycarousel.html", context)

def Error(request, url):
    message = 'Stránka ' + url + ' na našem webu neexistuje, zkuste to znovu.'
    return render(request, "error.html", {'message': message})