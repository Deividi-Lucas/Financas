

salario = float(input(
    'Digite aqui seu salário: '
))

hora = salario/160
dia = hora *8 
semana = dia *7

print('Colocando uma média horaria de trabalho de 40 horas semanal.')

print(f'Você ganha R${salario:.2f}, Em um mês trabalha cerca de 160 horas.')
print(f'Logo você ganha R${hora:.2f} por hora.')
print(f'Ganha R${dia:.2f} por dia.')
print(f'Ganha R${semana:.2f} por semana.')