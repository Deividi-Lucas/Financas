import Project as ts

# Programa Principal
try:
    ts.simulacao()
# Se houver algum erro com o programa
except:
    print('\n\n\033[1;31mHOUVE ALGUM ERRO!!\033[m')
# Não importa se deu certo ou errado mostrará se o programa foi rodado.
else:
    print('PROGRAMA RODADO COM SUCESSO!')
