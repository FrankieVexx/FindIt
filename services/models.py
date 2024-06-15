import models

def signup(model.models)
    if method = "POST"
    
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(firstname=firstname, lastname=lastname, email=email, password=password)
    user.save()