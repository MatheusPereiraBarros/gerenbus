from django.db import models
from django.utils import timezone

class Garagem(models.Model):
	idGaragem = models.AutoField(primary_key=True)
	endereco = models.CharField(max_length=255)
	quantVagas = models.IntegerField()
		

class Onibus(models.Model):
	idOnibus = models.AutoField(primary_key=True)
	marcaOnibus = models.CharField(max_length=140, default='')
	modeloOnibus = models.CharField(max_length=140, default='')
	garagem = models.ForeignKey(Garagem, on_delete=models.CASCADE, related_name = 'garagem')


class Rota(models.Model):
	idRota = models.AutoField(primary_key=True)
	destino = models.CharField(max_length=140)
	partida = models.CharField(max_length=140)
	horario = models.DateField()
	valorPassagem = models.BigIntegerField()


class Funcao(models.Model):
	idFuncao = models.AutoField(primary_key=True)
	descricaoFuncao = models.CharField(max_length=140)

class Funcionario(models.Model):
	idFuncionario = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=255)
	CPF = models.IntegerField()
	idFuncao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name = 'funcao')


class Viagem(models.Model):
	idViagem = models.AutoField(primary_key=True)
	horarioPrevisto = models.DateField()
	quantPassageiros = models.IntegerField()
	idRota = models.ForeignKey(Rota, on_delete=models.CASCADE, related_name = 'rota')
	idOnibus = models.ForeignKey(Onibus, on_delete=models.CASCADE, related_name = 'onibus')
	idFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name = 'funcionario')

