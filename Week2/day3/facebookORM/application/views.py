from django.shortcuts import render, HttpResponse
from .models import Author, Book
# Create your views here.
def index(request):

    my_book = Book.objects.get(id=2)
    my_book.title = "Hello World"
    my_book.save()

    new_book = Book.objects.create(
        title="The Water Dancer",
        description="A book about telepathy and antebellum south",
        author=Author.objects.get(id=2)
        )
    
    context = {
        "authors": Author.objects.all()
    }
    # first_author = Author.objects.first()
    # first_author_books = first_author.books.all()

    return render(request, "index.html", context)

def processMoney(request):
    # Make a dictionary, the key is location, value
    location = request.POST['which_location']
    
    goldFrom = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50)
        }

    request.session['goldCount'] += goldFrom[location]
    if goldFrom[location] > 0:
        request.session['messageLog'].append(
            {
                "message":f"You gain {goldFrom[location]} gold!", 
                "class": "green"
            }
        )
    else:
        request.session['messageLog'].append(
            {
                "message":f"You lose {goldFrom[location]} gold!", 
                "class": "red"
            }
        )

    return redirect('/')