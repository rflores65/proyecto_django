from django.core.exceptions import ValidationError

def mayor_edad(value):
    if value > 80 or value < 18:
        raise ValidationError("%(value)s no puede ser arrendatario",
                              params={'value':value})