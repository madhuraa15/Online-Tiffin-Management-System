from django.shortcuts import redirect, render
from django.urls import reverse_lazy

def match(request):
    page='match'
    context = {'page': page}
    return render(request, 'pincode_search/match.html')

def notmatch(request):
    page='notmatch'
    context = {'page': page}
    return render(request, 'pincode_search/notmatch.html')


def pincode_search(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode')
        
        # List of valid pincodes
        valid_pincodes = ['402107', '400007', '402123']
        
        # Check if the entered pincode is in the list of valid pincodes
        if pincode in valid_pincodes:
            return render(request, 'pincode_search/match.html')
        else:
            return render(request, 'pincode_search/notmatch.html')
            
    else:
        return render(request, 'pincode_search/pincode_search.html')

    



    

# Create your views here.
