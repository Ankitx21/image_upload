from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to clear the form after successful submission
    else:
        form = ImageForm()
    
    # Fetch all images to display
    images = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('home')
    return render(request, 'myapp/confirm_delete.html', {'image': image})
