from django.shortcuts import render
import operator, collections

# Create your views here.
def home(request):
    words = None
    count = {}
    if request.method == 'POST':
        s = request.POST.get('input_text', '')
        # print(s)
        words = list(s.split())

        if words:
            for i in words:
                # print(i)
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1

    n = 0
    l = 0
    if words:
        n = len(words)
        l = len(count)

        lst = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
        count = collections.OrderedDict(lst)

    dic = {'words': words, 'count':count, 'n':n, 'l':l}
    return render(request, 'count/home.html', context=dic)
