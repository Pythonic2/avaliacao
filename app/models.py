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


from django.db import models



class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    qrcode = models.ImageField(blank=True, upload_to='qrcode')
    site = models.CharField(max_length=150, default='www.google.com.br/')  
    codigo = models.CharField(max_length=300, blank=True)  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
