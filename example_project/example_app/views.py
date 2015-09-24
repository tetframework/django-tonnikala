from django.shortcuts import render


def test_view(request):
    return render(request, "example_app/test.tk", {
        "foo": "bar",
    })
