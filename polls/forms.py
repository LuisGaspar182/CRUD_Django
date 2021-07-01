from django.forms import ModelForm
from polls.models import Pessoas


class PessoasForms(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['nome', 'telefone']