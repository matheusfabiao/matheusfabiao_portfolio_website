import pytest
from django.core.exceptions import ValidationError

from portfolio.models import ProjectCategory


@pytest.mark.django_db
def test_project_category_project_creation(sample_project_category):
    """Testa a criação de uma categoria de projeto verificando se os campos
    obrigatórios são preenchidos corretamente.

    Args:
        sample_project_category (ProjectCategory): Instância de categoria
            de projeto criada pela fixture
    """
    assert sample_project_category.id is not None
    assert sample_project_category.created_at is not None
    assert ProjectCategory.objects.count() == 1


@pytest.mark.django_db
def test_project_category_project_details(sample_project_category):
    """Testa se os detalhes da categoria de projeto foram salvos corretamente
    no banco de dados.

    Args:
        sample_project_category (ProjectCategory): Instância de categoria
            de projeto criada pela fixture
    """
    assert ProjectCategory.objects.get(id=1) == sample_project_category
    assert sample_project_category.name == 'Categoria de Projeto'
    assert sample_project_category.slug == 'categoria-de-projeto'
    assert sample_project_category.description == (
        'Descrição da categoria de projeto'
    )


@pytest.mark.django_db
def test_project_category_update(sample_project_category):
    """Testa a atualização dos campos de uma categoria de projeto existente.

    Args:
        sample_project_category (ProjectCategory): Instância de categoria
            de projeto criada pela fixture
    """
    sample_project_category.name = 'Web Development'
    sample_project_category.slug = 'web-development'
    sample_project_category.description = 'Projects related to web development'
    sample_project_category.save()
    assert sample_project_category.name == 'Web Development'
    assert sample_project_category.slug == 'web-development'
    assert sample_project_category.description == (
        'Projects related to web development'
    )
    assert str(sample_project_category) == 'Web Development'
    assert sample_project_category.id == 1


@pytest.mark.django_db
def test_project_category_delete(sample_project_category):
    """Testa a exclusão de uma categoria de projeto verificando se
    o objeto é removido corretamente do banco de dados.

    Args:
        sample_project_category (ProjectCategory): Instância de categoria
            de projeto criada pela fixture
    """
    sample_project_category.delete()
    assert ProjectCategory.objects.count() == 0


@pytest.mark.django_db
def test_project_category_project_str_representation(sample_project_category):
    """Testa se a representação em string da categoria de projeto
    retorna o nome da categoria.

    Args:
        sample_project_category (ProjectCategory): Instância de categoria
            de projeto criada pela fixture
    """
    assert str(sample_project_category) == sample_project_category.name


@pytest.mark.django_db
def test_project_category_project_name_max_length():
    """Testa se o campo 'name' da categoria de projeto respeita
    o limite máximo de caracteres definido no modelo.
    """
    max_length = 100
    field = ProjectCategory._meta.get_field('name')
    assert field.max_length == max_length


@pytest.mark.django_db
def test_project_category_project_required_fields_cannot_be_empty():
    """Testa se a validação impede a criação de uma categoria de projeto
    com campos obrigatórios vazios.
    """
    with pytest.raises(ValidationError):
        ProjectCategory.objects.create().full_clean()


@pytest.mark.django_db
def test_project_category_verbose_name():
    """Testa se os nomes verbosos (singular e plural) da categoria
    de projeto estão definidos corretamente no modelo.
    """
    assert ProjectCategory._meta.verbose_name == 'Categoria'
    assert ProjectCategory._meta.verbose_name_plural == 'Categorias'


@pytest.mark.django_db
def test_project_category_ordering(sample_project_category):
    """Testa se a ordenação das categorias de projeto está funcionando
    corretamente por ordem alfabética do nome.

    Args:
        sample_project_category (ProjectCategory): Instância de categoria
            de projeto criada pela fixture
    """
    project_category = ProjectCategory.objects.create(
        name='A Project Category',
        slug='a-project-category',
        description='A Project Category description',
    )
    assert ProjectCategory._meta.ordering == ['name']
    assert list(ProjectCategory.objects.all()) == [
        project_category,
        sample_project_category,
    ]
    assert project_category.id > sample_project_category.id
