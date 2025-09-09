from django import forms
from cars.models import Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Descreva as características do veículo...',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna o campo bio opcional
        if 'bio' in self.fields:
            self.fields['bio'].required = False
            self.fields['bio'].help_text = 'Deixe em branco para gerar automaticamente'


    def clean_value(self):
        value = self.cleaned_data['value']#captura os dados de valor do formulário 
        if value < 10000:
            self.add_error('value', 'O valor minimo é R$ 10.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        if factory_year < 1975:
            self.add_error('factory_year', 'Não aceitamos carros com ano de fabricação menor que 1975')
        return factory_year