import pytest

from portfolio.models import Project, ProjectCategory


@pytest.fixture
def sample_project_category():
    """ Exemplo de categoria de projeto

    Returns:
        ProjectCategory : Categoria de projeto
    """
    return ProjectCategory.objects.create(
        name='Categoria de Projeto',
        slug='categoria-de-projeto',
        description='Descrição da categoria de projeto',
    )


@pytest.fixture
def sample_project():
    """ Exemplo de projeto

    Returns:
        Project : Projeto
    """
    return Project.objects.create(
        title='Project 1',
        slug='project-1',
        description='Project 1 description',
    )
