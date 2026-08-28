from django.conf import settings
from django.core.mail import EmailMessage, BadHeaderError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext as _

from .models import Product


def home(request):
    products = list(Product.objects.all())
    chunk_size = 3
    product_pages = [products[i:i + chunk_size] for i in range(0, len(products), chunk_size)] or [[]]
    return render(request, 'pages/home.html', {'product_pages': product_pages})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'pages/product_detail.html', {'product': product})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not (name and email and message):
            return JsonResponse({'ok': False, 'error': _('Bitte fülle alle Felder aus.')}, status=400)

        subject = _('Neue Kontaktanfrage von %(name)s') % {'name': name}
        body = (
            f"{_('Name')}: {name}\n"
            f"{_('E-Mail')}: {email}\n\n"
            f"{_('Nachricht')}:\n{message}"
        )
        try:
            EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECIPIENT_EMAIL],
                reply_to=[email],
            ).send(fail_silently=False)
        except BadHeaderError:
            return JsonResponse({'ok': False, 'error': _('Ungültige Eingabe.')}, status=400)
        except Exception:
            return JsonResponse({'ok': False, 'error': _('Nachricht konnte nicht gesendet werden. Bitte versuche es später erneut.')}, status=500)

        return JsonResponse({'ok': True})

    return render(request, 'pages/contact.html')


def historie(request):
    return render(request, 'pages/historie.html')
