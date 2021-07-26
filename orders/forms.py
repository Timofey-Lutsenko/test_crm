from django import forms

from phonenumber_field.formfields import PhoneNumberField


class OrderForm(forms.Form):

    TYPE_CHOICES = (
        ('RPIR', 'Repair'),
        ('SRVS', 'Service'),
        ('CNST', 'Consultation'),
        ('WRNT', 'Warranty'),
    )

    type_of_order = forms.ChoiceField(
        label='Chose type of order',
        choices=TYPE_CHOICES
    )
    description = forms.CharField(
        max_length=1000,
        label='Description',
        widget=forms.TextInput(
            attrs={'placeholder': 'Description. Up to 1000 characters.'}
        )
    )
    customers_phone_number = PhoneNumberField(
        widget=forms.TextInput(),
        label='Contact number*'
    )


class NewCustomer(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=40)
    phone_number = PhoneNumberField()


class OrderFilter(forms.Form):

    TYPE_CHOICES = (
        ('', ''),
        ('RPIR', 'Repair'),
        ('SRVS', 'Service'),
        ('CNST', 'Consultation'),
        ('WRNT', 'Warranty'),
    )

    STATUS_CHOICES = (
        ('', ''),
        ('RGTR', 'Registered'),
        ('INPR', 'In Progress'),
        ('DONE', 'Order ready'),
        ('CNLD', 'Order canceled')
    )

    by_type = forms.ChoiceField(
        label='Filter by type of order',
        choices=TYPE_CHOICES,
        required=False
    )

    date_from = forms.DateTimeField(
        label='Date from',
        required=False
    )

    date_to = forms.DateTimeField(
        label='to',
        required=False
    )

    by_status = forms.ChoiceField(
        label='Filter by status of order',
        choices=STATUS_CHOICES,
        required=False
    )
