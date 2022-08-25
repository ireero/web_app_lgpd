from django import forms
from .models import Cadastro
    
    


class CadastroForm(forms.ModelForm):
    
    class Meta:
        model = Cadastro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['nome_empresa'].widget.attrs.update({'class': 'input'})
        self.fields['nome_colaborador'].widget.attrs.update({'class': 'input'})
        self.fields['funcao_colaborador'].widget.attrs.update({'class': 'input'})
        self.fields['email_colaborador'].widget.attrs.update({'class': 'input'})
        self.fields['whatsapp_colaborador'].widget.attrs.update({'class': 'input-number'})
        self.fields['senha'].widget.attrs.update({'class': 'input'})
        self.fields['termo_de_uso'].widget.attrs.update({'id': 'input-check'})


