import pytest

from portfolio.models import Project, ProjectCategory


@pytest.fixture
def sample_project_category():
    return ProjectCategory.objects.create(
        name='Categoria de Projeto',
        slug='categoria-de-projeto',
        description='Descrição da categoria de projeto',
    )


@pytest.fixture
def sample_project():
    return Project.objects.create(
        title='Project 1',
        slug='project-1',
        description='Project 1 description',
    )
