from django.shortcuts import render
# Create your views here.
num = 0
list_history = {}

def history(request):
    return render(request, "history.html", {'list_history':list_history})



def action_play(request):
    global num
    secret_numbers = [5,6,9,3]
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        num += 1
        context = {
            'numbers': request.POST.get("numbers"),
            }
        try:
            numbers = list(map(int, context['numbers'].split(' ')))
            if len(numbers) == 4:
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
                list_history[num] = f"{numbers} ; bulls: {bull}, cow: {cow}"
            else:
                return render(request, 'error.html')
            return render(request, 'response.html', context)
        except ValueError:
            return render(request, 'error.html')
