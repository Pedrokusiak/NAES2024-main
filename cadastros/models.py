from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.nome}/{self.estado}"
    
    class Meta:
        ordering = ["nome", "estado"]


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=150)
    nascimento = models.DateField(verbose_name="data de nascimento")
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    rede_social = models.URLField(max_length=255, blank=True,
        null=True, help_text="Informe o link do Instagram, Facebook, LinkedIn ou outra rede social.")
    salario = models.DecimalField(verbose_name="salário",
        decimal_places=2, max_digits=9)
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"
    
class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]

class Professor(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    registro = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]

class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    carga_horaria = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.curso} - {self.ano}/{self.semestre}"
    
    class Meta:
        unique_together = ['curso', 'professor', 'ano', 'semestre']
        ordering = ["ano", "semestre", "curso"]

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    data_matricula = models.DateField(verbose_name="Data de Matrícula")
    
    def __str__(self):
        return f"{self.aluno} - {self.turma}"
    
    class Meta:
        unique_together = ['aluno', 'turma']
        ordering = ["data_matricula"]


class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    nota = models.FloatField()
    data_avaliacao = models.DateField(verbose_name="Data de Avaliação")
    
    def __str__(self):
        return f"{self.aluno} - {self.turma} - {self.nota}"
    
    class Meta:
        ordering = ["data_avaliacao"]
        constraints = [
            models.CheckConstraint(check=models.Q(nota__gte=0) & models.Q(nota__lte=10), name='nota_range')
        ]

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    carga_horaria = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.nome} ({self.curso})"
    
    class Meta:
        unique_together = ['nome', 'curso']
        ordering = ["nome"]


class HorarioAula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    dia_semana = models.PositiveIntegerField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    
    def __str__(self):
        return f"{self.turma} - {self.disciplina} ({self.dia_semana})"
    
    class Meta:
        ordering = ["turma", "disciplina", "dia_semana"]
        constraints = [
            models.UniqueConstraint(fields=['turma', 'disciplina', 'dia_semana', 'hora_inicio'], name='unique_horario_aula')
        ]