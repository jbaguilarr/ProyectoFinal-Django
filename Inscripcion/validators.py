from django.core.exceptions import ValidationError


def validar_correo(value):
    if '@' not in value:
        raise ValidationError(
            '%(value)s no es un correo valido',
            params={'value': value}
        )

def validar_telefono(value):
    if len(value) != 8:
        raise ValidationError(
            '%(value)s no es un numero valido, debe contener 8 digitos',
            params={'value': value}
        )