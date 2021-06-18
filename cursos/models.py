from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField('criacao', auto_now_add=True)
    atualizacao= models.DateTimeField('atualizacao', auto_now_add=True)
    ativo = models.BooleanField('status', default=True)

    class  Meta:
        abstract = True

    
class Curso(Base):
    titulo = models.CharField('titulo', max_length=255)
    url= models.URLField('url', unique=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        #ordeing = ['id']

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey( Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField('nome', max_length=255)
    email = models.EmailField()
    comentario = models.TextField('comentario', blank=True, default='')
    nota = models.DecimalField('nota', max_digits=2, decimal_places=1)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email','curso']
        #ordeing = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.nota}'    

# Create your models here.
