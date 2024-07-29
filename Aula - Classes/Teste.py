from Pessoa import Pessoa
from Livro import Livro
from Aluno import Aluno
from Conta import Conta
from Funcionario import Funcionario

pessoa1 = Pessoa("Pedro",18,"Rua do Papa - 654")
livro1 = Livro("Pequeno Princípe","Machado de Assís","Saraiva",70)
aluno1 = Aluno("Pedrinho Jonas",200123,6,7,0,0)
conta1 = Conta("Pedroca Martins",123456,345,20000)
func1 = Funcionario("Augustinho","Carrara",6,20)

print() # PESSOA

print(pessoa1.getEndereco())
print(pessoa1.getNome())
pessoa1.setIdade(21)

print() # LIVRO

livro1.getPag()
livro1.setEditora("Penacova")

print() # ALUNO

print(aluno1.mostrarSituacao())

print() # CONTA

conta1.imprimirSaldo()
conta1.depositar(10000)
conta1.imprimirSaldo()
conta1.sacar(40000)
conta1.imprimirSaldo()
conta1.sacar(100)

print() #FUNCIONARIO

print(func1.nomeCompleto())
print(func1.calcularSalario())
func1.incremetentarHoras(4)
print(func1.calcularSalario())