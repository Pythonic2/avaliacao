from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.urls import reverse
from django.conf import settings
from django.db import models
from dataclasses import dataclass
from django.contrib.auth.models import User
from time import strftime

from django.db import models




class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    end = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nome} - {self.end}'

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    qrcode = models.ImageField(blank=True, upload_to='qrcode')
    site = models.CharField(max_length=150, default='www.google.com.br/')  
    codigo = models.CharField(max_length=300, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total_avaliacoes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nome} - {self.site}"  

    def save(self, *args, **kwargs):
        # Se o objeto ainda não tem um ID (ou seja, ainda não foi salvo no banco de dados), salve-o primeiro
        if not self.pk:
            super().save(*args, **kwargs)

        # Atualiza o campo codigo com a concatenação de site e id antes de salvar
        self.codigo = f"{self.site}{self.pk}"  
        
        qr_image = qrcode.make(self.codigo)  # Gera o QR code
        qr_offset = Image.new('RGB', (310, 310), 'white')  # Cria uma nova imagem para o QR code
        qr_offset.paste(qr_image)  # Insere o QR code na imagem
        
        # Nome do arquivo utilizando o ID do objeto
        file_name = f'{self.nome}-{self.pk}-qr.png'
        
        # Cria um buffer de memória
        stream = BytesIO()
        
        # Salva a imagem do QR code no buffer
        qr_offset.save(stream, 'PNG')
        
        # Salva o buffer no campo de imagem
        self.qrcode.save(file_name, File(stream), save=False)
        
        super().save(*args, **kwargs)  # Salva as alterações no banco de dados


    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
    

class Avaliacao(models.Model):
    FUNCIONARIO_CHOICES = (
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    )

    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    atendimento = models.CharField(max_length=10, choices=FUNCIONARIO_CHOICES)
    higiene = models.CharField(max_length=10, choices=FUNCIONARIO_CHOICES)
    comentario = models.TextField(blank=True)
    data = models.DateField(default=strftime("%d/%m/%Y"), blank=True)
    def __str__(self):
        return f"Avaliação de {self.funcionario.nome}"
    




class AdministradorUnidade(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)