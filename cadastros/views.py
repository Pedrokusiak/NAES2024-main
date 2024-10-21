from .models import Cidade, Pessoa, Aluno, Professor, Curso, Turma, Matricula, Avaliacao, Disciplina, HorarioAula

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class CidadeCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade') 
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados
        

class CidadeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadadeDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade


class CidadeList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/cidade.html'
    model = Cidade


##############################################################


class PessoaCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados
    

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'salario', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados
    
    
class PessoaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    
    
class PessoaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/pessoa.html'
    model = Pessoa

##############################################################


class AlunoCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-aluno')
    model = Aluno
    fields = ['nome', 'data_nascimento', 'endereco', 'telefone', 'email', 'matricula']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Aluno'
        return dados


class AlunoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-aluno')
    model = Aluno
    fields = ['nome', 'data_nascimento', 'endereco', 'telefone', 'email', 'matricula']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class AlunoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-aluno')
    model = Aluno


class AlunoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/aluno.html'
    model = Aluno


##############################################################


class ProfessorCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-professor')
    model = Professor
    fields = ['nome', 'data_nascimento', 'endereco', 'telefone', 'email', 'registro']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Professor'
        return dados


class ProfessorUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-professor')
    model = Professor
    fields = ['nome', 'data_nascimento', 'endereco', 'telefone', 'email', 'registro']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class ProfessorDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-professor')
    model = Professor


class ProfessorList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/professor.html'
    model = Professor


##############################################################


class CursoCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-curso')
    model = Curso
    fields = ['nome', 'descricao', 'carga_horaria']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Curso'
        return dados


class CursoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-curso')
    model = Curso
    fields = ['nome', 'descricao', 'carga_horaria']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class CursoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-curso')
    model = Curso


class CursoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/curso.html'
    model = Curso


##############################################################


class TurmaCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turma')
    model = Turma
    fields = ['curso', 'professor', 'ano', 'semestre']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Turma'
        return dados


class TurmaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-turma')
    model = Turma
    fields = ['curso', 'professor', 'ano', 'semestre']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.curso} - {self.object.ano}/{self.object.semestre}"
        return dados


class TurmaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-turma')
    model = Turma


class TurmaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/turma.html'
    model = Turma


##############################################################


class MatriculaCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-matricula')
    model = Matricula
    fields = ['aluno', 'turma', 'data_matricula']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Matrícula'
        return dados


class MatriculaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-matricula')
    model = Matricula
    fields = ['aluno', 'turma', 'data_matricula']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar matrícula de {self.object.aluno}"
        return dados


class MatriculaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-matricula')
    model = Matricula


class MatriculaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/matricula.html'
    model = Matricula


##############################################################


class AvaliacaoCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-avaliacao')
    model = Avaliacao
    fields = ['aluno', 'turma', 'nota', 'data_avaliacao']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Avaliação'
        return dados


class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-avaliacao')
    model = Avaliacao
    fields = ['aluno', 'turma', 'nota', 'data_avaliacao']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar avaliação de {self.object.aluno}"
        return dados


class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-avaliacao')
    model = Avaliacao


class AvaliacaoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/avaliacao.html'
    model = Avaliacao


##############################################################


class DisciplinaCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')
    model = Disciplina
    fields = ['nome', 'carga_horaria', 'curso']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Disciplina'
        return dados


class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')
    model = Disciplina
    fields = ['nome', 'carga_horaria', 'curso']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar disciplina {self.object.nome}"
        return dados


class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplina')
    model = Disciplina


class DisciplinaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/disciplina.html'
    model = Disciplina


##############################################################


class HorarioAulaCreate(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-horario')
    model = HorarioAula
    fields = ['turma', 'disciplina', 'dia_semana', 'horario_inicio', 'horario_termino']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Horário de Aula'
        return dados


class HorarioAulaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-horario')
    model = HorarioAula
    fields = ['turma', 'disciplina', 'dia_semana', 'horario_inicio', 'horario_termino']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar horário de {self.object.turma} - {self.object.disciplina}"
        return dados


class HorarioAulaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-horario')
    model = HorarioAula


class HorarioAulaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/horario.html'
    model = HorarioAula
