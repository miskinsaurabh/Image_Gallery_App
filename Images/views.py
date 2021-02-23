from django.shortcuts import render,redirect
from .models import Category,Image

# Creating gallery views.
def gallery(request):

    #for filtering image according to categories
    category = request.GET.get('category')
    if category == None :
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name == category) 

    images = Image.objects.all()
    categories = Category.objects.all()
    context = {'categories' : categories , 'images' : images}
    return render(request, "Images/gallery.html",context) # render the request to html page to display image with category

# display full size image views.
def viewImage(request, x):
    image = Image.objects.get(id=x)
    context = { "image" : image}
    return render(request, "Images/view_image.html",context)# render the request to html page to display full size image

# creating view for uploading image
def addImage(request):
    categories = Category.objects.all()

    #for selecting categories, if it is not in dropdown list then create new category otherwise 
    # image will be diplayed with no category
    if request.method == 'POST':
        data = request.POST
        photo = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        
        for x in photo:
            image = Image.objects.create(
                category=category,
                img=x,
            )

        return redirect('gallery')#to redirect image into gallery

    context = {'categories' : categories}
    return render(request, "Images/add_image.html", context) # render the request to html page to add image
''
    