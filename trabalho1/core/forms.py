from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    telefone = forms.CharField(label='Telefone')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']
        conteudo = f'Nome: {nome}\nE-mail: {email}\Telefone: {telefone}\nMensagem: {mensagem}'
        mail = EmailMessage(
        subject='E-mail enviado pelo sistema Django',
        body=conteudo,
        from_email=email,
        to=['contato@seudominio.com.br', ],
        headers={'Reply.To':email},
        )
        mail.send()