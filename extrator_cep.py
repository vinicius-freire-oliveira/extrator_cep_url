endereco = "Rua da Hora, nº 125, apartamento 1501, Espinheiro, Recife, PE, 50121-770"

import re  # Regular Expression -- RegEx

# Define o padrão de busca para um CEP: 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

# Busca o padrão na string 'endereco'
busca = padrao.search(endereco)  # Match

# Verifica se houve correspondência
if busca:
    # Recupera o CEP encontrado usando o método group()
    cep = busca.group()
    print("CEP: {}".format(cep))
