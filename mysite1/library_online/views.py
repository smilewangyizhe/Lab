from django.template import Context
from django.shortcuts import render_to_response
from library_online.models import Author,Book

def welcome(request):
    c = Context({"author_list": Author.objects.filter()})
    return render_to_response("welcome.html", c)
def search(request):
    try:
        author = Author.objects.get(Name = request.GET["name"])
        c=Context({"author":author.Name,"book_list":author.book_set.all()})
        return render_to_response('search.html',c)
    except:
        return render_to_response('error.html')
def add_author(request):
    if request.POST:
        post = request.POST
        c = Context({"information":"Wrong information!"})
        try:
            try:
                author = Author.objects.get(AuthorID = post["AuthorID"])
                return render_to_response("add_author.html",c)
            except:
                new_author = Author(
                    AuthorID = post["AuthorID"],
                    Name = post["Name"],
                    Age = post["Age"],
                    Country = post["Country"])   
                if post["Sex"] == 'M':
                    new_author.Sex = True
                else:
                    new_author.Sex = False       
                new_author.save()
                return render_to_response("welcome.html",Context({"author_list": Author.objects.filter()}))   
        except:
            return render_to_response("add_author.html",c)
    else:
        return render_to_response("add_author.html")
def add_book(request):
    if request.POST:
        post = request.POST
        try:
            try:
                book = Author.objects.get(ISBN = post["ISBN"])
                return render_to_response("add_book.html", Context({"information":"Wrong ISBN!"}))
            except:
                try:
                    author = Author.objects.get(AuthorID = post["AuthorID"])
                except:
                    return render_to_response("add_book.html",Context({"information":\
                        "The author doesn't exist! Please add the author first"}))
                new_book = Book(
                    ISBN = post["ISBN"],
                    Title = post["Title"],
                    AuthorID = author,
                    Publisher = post["Publisher"],
                    PublishDate = post["PublishDate"],
                    Price = post["Price"])         
                new_book.save()
                b = Context({"author":author.Name,"book_list":author.book_set.all()})
                return render_to_response('search.html', b)
        except:
            return render_to_response("add_book.html", Context({"information":"Wrong information!"}))
    else:
        return render_to_response("add_book.html")
def detail(request):
    id = request.GET["id"]
    book = Book.objects.get(id=int(id))
    return render_to_response("detail.html",Context({"book":book}))
def update(request):
    id = request.GET["id"]
    book = Book.objects.get(id=int(id))
    if request.POST:
        post = request.POST
        try:
            try:
                author = Author.objects.get(AuthorID = post["AuthorID"])
            except:
                return render_to_response("update.html",id,Context({"information":\
                    "The author doesn't exist! Please add the author first","book":book}))
            new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
                AuthorID = author,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])         
            new_book.save()
            book.delete()
            return render_to_response('detail.html',Context({"book":new_book}))
        except:
            return render_to_response("update.html",id, Context({"information":"Wrong information!","book":book}))
    return render_to_response("update.html",id,Context({"book":book}))
def delete_author(request):
    id = request.GET["id"]
    author_id = Author.objects.get(id = int(id))
    author_id.delete()
    return render_to_response("delete_author.html",id)
def delete_book(request):
    id = request.GET["id"]
    book_id = Book.objects.get(id = int(id))
    book_id.delete()
    return render_to_response("delete_book.html",id,Context({"book":book_id}))
