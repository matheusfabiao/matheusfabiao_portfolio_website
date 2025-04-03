from django.db import models


# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    slug = models.SlugField(verbose_name='Slug', unique=True)
    description = models.TextField(blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    slug = models.SlugField(verbose_name='Slug', unique=True)
    description = models.TextField(blank=True, verbose_name='Descrição')
    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.PROTECT,
        verbose_name='Categoria'
    )
    image = models.ImageField(upload_to='projects/', verbose_name='Imagem')
    live_link = models.URLField(blank=True, verbose_name='Link do Projeto')
    github_link = models.URLField(blank=True, verbose_name='Link do Github')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
