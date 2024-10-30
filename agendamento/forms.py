from django import forms
from .models import Agendamento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'espaco', 'descricao']
        widgets = {
            'data' : forms.DateInput(attrs={'type': 'date'}),
        }
#                  *argumentos *keyword
    def __init__(self, *args, **kwargs): #Constructor -> Roda assim que a classe é inicializa
        super(AgendamentoForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Agendar'))

