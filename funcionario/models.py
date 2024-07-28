from django.db import models
from django.urls import reverse
from django.core.files import File
from io import BytesIO
from PIL import Image
import qrcode

from unidade.models import Unidade
from authentication.models import CustomUser

def salvar_no_diretorio_do_user(instance, filename):
    username = instance.usuario.username
    return f'{username}/qrcode/{filename}'

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    qrcode = models.ImageField(blank=True, upload_to=salvar_no_diretorio_do_user)
    site = models.CharField(max_length=150, default='https://primeportalbr.cloudboosterlab.org/avaliacao/')
    codigo = models.CharField(max_length=300, blank=True)
    matricula = models.CharField(max_length=15, blank=True, unique=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_avaliacoes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nome}"

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

        self.codigo = f"{self.site}{self.usuario.id}/{self.matricula}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.codigo)
        qr.make(fit=True)
        
        qr_image = qr.make_image(fill='black', back_color='white')
        qr_image = qr_image.convert('RGB')
        
        size = (410, 410)
        qr_offset = Image.new('RGB', size, 'white')
        
        # Centralizar o QR code na imagem
        pos = ((size[0] - qr_image.size[0]) // 2, (size[1] - qr_image.size[1]) // 2)
        qr_offset.paste(qr_image, pos)
        
        file_name = f'{self.nome}-{self.matricula}-qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qrcode.save(file_name, File(stream), save=False)
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.matricula})
