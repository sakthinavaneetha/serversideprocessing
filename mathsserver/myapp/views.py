from django.shortcuts import render

def volumecalculation(request):
    context ={}
    context["volume"]='0'
    context["h"]='0'
    context["l"]='0'
    context["w"]='0'
    if request.method == 'POST':
    
        h=request.POST.get('height','0')
        l=request.POST.get('length','0')
        w=request.POST.get('width','0')
        volume=int(h)*int(l)*int(w)
        context['volume'] = volume
        context['l']=l
        context['h']=h
        context['w']=w
    return render(request,"myapp/math.html",context)