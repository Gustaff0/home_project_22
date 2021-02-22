from django.shortcuts import render

# Create your views here.

def action_play(request):
    secret_numbers = [5,6,9,3]
    qty = 0
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        qty += 1
        context = {
            'numbers': request.POST.get("numbers"),
            }
        try:
            numbers = list(map(int, context['numbers'].split(' ')))
            cow = 0
            bull = 0
            for i in range(len(numbers)):
                if numbers[i] == secret_numbers[i]:
                    bull += 1
                elif numbers[i] in secret_numbers:
                    cow += 1
                if bull == 4:
                    context['win'] = "You Winner Man!"
                else:
                    context['win'] = "You are looser!"
            context['bulls'] = bull
            context['cows'] = cow
            context['qty_move'] = qty
            return render(request, 'response.html', context)
        except ValueError:
            return render(request, 'error.html')
