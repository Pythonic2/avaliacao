from django import forms
from app.models import Funcionario



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = ['nome','codigo']

    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(ContactForm, self).__init__(*args, **kwargs)
        # you can also remove labels of built-in model properties
        self.fields['nome'].label = ''
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['id'] = 'nome'
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome'

        self.fields['codigo'].label = ''
        self.fields['codigo'].widget.attrs['class'] = 'form-control'
        self.fields['codigo'].widget.attrs['id'] = 'codigo'
        self.fields['codigo'].widget.attrs['placeholder'] = 'exemplo@exemplo.com'

        

# class FuncionarioForm(forms.ModelForm):
    
#     class Meta:
#         model = Funcionario
#         fields = ['nome','codigo']
        
#     def __init__(self, *args, **kwargs):
#         ''' remove any labels here if desired
#         '''
#         super(Funcionario, self).__init__(*args, **kwargs)
#         # you can also remove labels of built-in model properties
#         self.fields['nome'].label = ''
#         self.fields['nome'].widget.attrs['class'] = 'form-control'
#         self.fields['nome'].widget.attrs['id'] = 'nome'
#         self.fields['nome'].widget.attrs['placeholder'] = 'Nome'

#         self.fields['codigo'].label = ''
#         self.fields['codigo'].widget.attrs['class'] = 'form-control'
#         self.fields['codigo'].widget.attrs['id'] = 'text'
#         self.fields['codigo'].widget.attrs['placeholder'] = '53656'

        
# class ComentarioForm(forms.ModelForm):
#     class Meta:
#         model = Comentario
#         fields = ['comentario']


#     def __init__(self, *args, **kwargs):
#         ''' remove any labels here if desired
#         '''
#         super(ComentarioForm, self).__init__(*args, **kwargs)
#         # you can also remove labels of built-in model properties
#         self.fields['comentario'].label = ''
#         self.fields['comentario'].widget.attrs['class'] = 'form-control'
#         self.fields['comentario'].widget.attrs['id'] = 'comentario'
#         self.fields['comentario'].widget.attrs['placeholder'] = 'Achei interessante, o que é isso?'
#         self.fields['comentario'] = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text', 'id': 'comentario','rows':5,'col':10,'placeholder':'Achei legal...'}),label='')


# class ContatoForm(forms.ModelForm):
#     class Meta:
#         model = Contato
#         fields = '__all__'


#     def __init__(self, *args, **kwargs):
#         ''' remove any labels here if desired
#         '''
#         super(ContatoForm, self).__init__(*args, **kwargs)
#         # you can also remove labels of built-in model properties

#         self.fields['nome'].label = ''
#         self.fields['nome'].widget.attrs['class'] = 'form-control'
#         self.fields['nome'].widget.attrs['id'] = 'nome'
#         self.fields['nome'].widget.attrs['placeholder'] = 'Nome'
        
#         self.fields['assunto'].label = ''
#         self.fields['assunto'].widget.attrs['class'] = 'form-control'
#         self.fields['assunto'].widget.attrs['id'] = 'assunto'
#         self.fields['assunto'].widget.attrs['placeholder'] = 'Assunto'


#         self.fields['email'].label = ''
#         self.fields['email'].widget.attrs['class'] = 'form-control'
#         self.fields['email'].widget.attrs['id'] = 'email'
#         self.fields['email'].widget.attrs['placeholder'] = 'exemplo@exemplo.com'


#         self.fields['menssagem'].label = ''
#         self.fields['menssagem'].widget.attrs['class'] = 'form-control'
#         self.fields['menssagem'].widget.attrs['id'] = 'menssagem'
#         self.fields['menssagem'].widget.attrs['placeholder'] = 'Achei legal, O que é isso?'
#         self.fields['menssagem'] = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','type':'text', 'id': 'comentario','rows':5,'col':10,'placeholder':'Achei legal...'}),label='')