from django.urls import path
# Importe suas views
from .views import CidadeCreate, CidadeUpdate, CidadadeDelete, CidadeList
from .views import PessoaCreate, PessoaUpdate, PessoaDelete, PessoaList

from .views import AlunoCreate, AlunoUpdate, AlunoDelete, AlunoList
from .views import ProfessorCreate, ProfessorUpdate, ProfessorDelete, ProfessorList
from .views import CursoCreate, CursoUpdate, CursoDelete, CursoList
from .views import TurmaCreate, TurmaUpdate, TurmaDelete, TurmaList
from .views import MatriculaCreate, MatriculaUpdate, MatriculaDelete, MatriculaList
from .views import AvaliacaoCreate, AvaliacaoUpdate, AvaliacaoDelete, AvaliacaoList
from .views import DisciplinaCreate, DisciplinaUpdate, DisciplinaDelete, DisciplinaList
from .views import HorarioAulaCreate, HorarioAulaUpdate, HorarioAulaDelete, HorarioAulaList

urlpatterns = [
    # Crie suas urls para as views
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadadeDelete.as_view(), name='excluir-cidade'),
    path('listar/cidades/', CidadeList.as_view(), name='listar-cidade'),
    
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('listar/pessoas/', PessoaList.as_view(), name='listar-pessoa'),


  # URLs para Aluno
    path('cadastrar/aluno/', AlunoCreate.as_view(), name='cadastrar-aluno'),
    path('editar/aluno/<int:pk>/', AlunoUpdate.as_view(), name='editar-aluno'),
    path('excluir/aluno/<int:pk>/', AlunoDelete.as_view(), name='excluir-aluno'),
    path('listar/alunos/', AlunoList.as_view(), name='listar-aluno'),

    # URLs para Professor
    path('cadastrar/professor/', ProfessorCreate.as_view(), name='cadastrar-professor'),
    path('editar/professor/<int:pk>/', ProfessorUpdate.as_view(), name='editar-professor'),
    path('excluir/professor/<int:pk>/', ProfessorDelete.as_view(), name='excluir-professor'),
    path('listar/professores/', ProfessorList.as_view(), name='listar-professor'),

    # URLs para Curso
    path('cadastrar/curso/', CursoCreate.as_view(), name='cadastrar-curso'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar-curso'),
    path('excluir/curso/<int:pk>/', CursoDelete.as_view(), name='excluir-curso'),
    path('listar/cursos/', CursoList.as_view(), name='listar-curso'),

    # URLs para Turma
    path('cadastrar/turma/', TurmaCreate.as_view(), name='cadastrar-turma'),
    path('editar/turma/<int:pk>/', TurmaUpdate.as_view(), name='editar-turma'),
    path('excluir/turma/<int:pk>/', TurmaDelete.as_view(), name='excluir-turma'),
    path('listar/turmas/', TurmaList.as_view(), name='listar-turma'),

    # URLs para Matrícula
    path('cadastrar/matricula/', MatriculaCreate.as_view(), name='cadastrar-matricula'),
    path('editar/matricula/<int:pk>/', MatriculaUpdate.as_view(), name='editar-matricula'),
    path('excluir/matricula/<int:pk>/', MatriculaDelete.as_view(), name='excluir-matricula'),
    path('listar/matriculas/', MatriculaList.as_view(), name='listar-matricula'),

    # URLs para Avaliação
    path('cadastrar/avaliacao/', AvaliacaoCreate.as_view(), name='cadastrar-avaliacao'),
    path('editar/avaliacao/<int:pk>/', AvaliacaoUpdate.as_view(), name='editar-avaliacao'),
    path('excluir/avaliacao/<int:pk>/', AvaliacaoDelete.as_view(), name='excluir-avaliacao'),
    path('listar/avaliacoes/', AvaliacaoList.as_view(), name='listar-avaliacao'),

    # URLs para Disciplina
    path('cadastrar/disciplina/', DisciplinaCreate.as_view(), name='cadastrar-disciplina'),
    path('editar/disciplina/<int:pk>/', DisciplinaUpdate.as_view(), name='editar-disciplina'),
    path('excluir/disciplina/<int:pk>/', DisciplinaDelete.as_view(), name='excluir-disciplina'),
    path('listar/disciplinas/', DisciplinaList.as_view(), name='listar-disciplina'),

    # URLs para Horário de Aula
    path('cadastrar/horarioaula/', HorarioAulaCreate.as_view(), name='cadastrar-horarioaula'),
    path('editar/horarioaula/<int:pk>/', HorarioAulaUpdate.as_view(), name='editar-horarioaula'),
    path('excluir/horarioaula/<int:pk>/', HorarioAulaDelete.as_view(), name='excluir-horarioaula'),
    path('listar/horariosaula/', HorarioAulaList.as_view(), name='listar-horarioaula'),
]
