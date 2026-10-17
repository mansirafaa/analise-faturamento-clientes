import pandas as pd
import matplotlib.pyplot as plt


# 1. Seus dados antigos
dados = {
    'Cliente': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Faturamento': [8000, 4200, 2800, 5100, 1900]
}
df = pd.DataFrame(dados)


# 2. Criando o gráfico de forma ultra simples
plt.bar(df['Cliente'], df['Faturamento'], color='tomato')


# 3. Colocando títulos para ficar profissional
plt.title('Faturamento por Cliente')
plt.xlabel('Clientes')
plt.ylabel('Valores em R$')


# 4. Mostrando o gráfico na tela
plt.show()







