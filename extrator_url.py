# Importando o módulo re para trabalhar com expressões regulares
import re

class ExtratorURL:
    # Método construtor __init__ que recebe a URL como parâmetro
    def __init__(self, url):
        # Atribui a URL fornecida após chamar o método sanitiza_url para limpar a string da URL
        self.url = self.sanitiza_url(url)
        # Chama o método valida_url para garantir que a URL não está vazia e é válida
        self.valida_url()

    # Método sanitiza_url para remover espaços desnecessários no início e no final da URL
    def sanitiza_url(self, url):
        # Verifica se o parâmetro 'url' é uma string
        if type(url) == str:
            # Retorna a URL limpa (sem espaços no início e no final)
            return url.strip()
        else:
            # Se 'url' não for uma string, retorna uma string vazia
            return ""

    # Método valida_url para verificar se a URL não está vazia e corresponde a um padrão específico
    def valida_url(self):
        # Verifica se a URL está vazia (ou seja, uma string vazia)
        if not self.url:
            # Se a URL estiver vazia, lança um ValueError com a mensagem "A URL está vazia"
            raise ValueError("A URL está vazia")

        # Define um padrão de URL válido usando expressões regulares
        padrao_url = re.compile('(http(s)?://)?(www.)?unitconverter.com(.br)?')
        # Verifica se a URL fornecida corresponde ao padrão definido
        match = padrao_url.match(url)
        # Se a URL não corresponder ao padrão, lança um ValueError com a mensagem "A URL não é válida."
        if not match:
            raise ValueError("A URL não é válida.")

    # Método para obter a base da URL (antes do primeiro "?")
    def get_url_base(self):
        # Encontra o índice do primeiro "?"
        indice_interrogacao = self.url.find('?')
        # Extrai a parte da URL antes do primeiro "?"
        url_base = self.url[:indice_interrogacao]
        # Retorna a base da URL
        return url_base

    # Método para obter os parâmetros da URL (depois do primeiro "?")
    def get_url_parametros(self):
        # Encontra o índice do primeiro "?"
        indice_interrogacao = self.url.find('?')
        # Extrai a parte da URL depois do primeiro "?"
        url_parametros = self.url[indice_interrogacao + 1:]
        # Retorna os parâmetros da URL
        return url_parametros

    # Método para obter o valor de um parâmetro específico da URL
    def get_valor_parametro(self, parametro_busca):
        # Encontra o índice do parâmetro na URL usando o método find
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        # Calcula o índice do início do valor do parâmetro
        indice_valor = indice_parametro + len(parametro_busca) + 1
        # Encontra o próximo "&" a partir do índice do valor
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        
        # Verifica se há mais "&" após o valor do parâmetro
        if indice_e_comercial == -1:
            # Se não houver mais "&" após o valor, o valor é tudo até o final da URL
            valor = self.get_url_parametros()[indice_valor:]
        else:
            # Se houver mais "&" após o valor, o valor é tudo até o próximo "&"
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        
        # Retorna o valor do parâmetro buscado
        return valor

    # Método especial __len__ que retorna o tamanho da URL
    def __len__(self):
        return len(self.url)

    # Método especial __str__ que retorna uma representação em string do objeto ExtratorURL
    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    # Método especial __eq__ que verifica se duas instâncias de ExtratorURL são iguais
    def __eq__(self, other):
        return self.url == other.url

url = "unitconverter.com/temperature?quantity=25&unitFrom=celsius&unitTo=fahrenheit&scale=1"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print("O tamanho da URL é: ", len(extrator_url))

# Imprime a representação em string do objeto ExtratorURL
print("URL completa: ", extrator_url)

# Verifica se duas instâncias com a mesma URL são iguais
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

# Busca o valor do parâmetro quantity
valor_quantidade = extrator_url.get_valor_parametro("quantity")
print("Valor do parâmetro 'quantity': ", valor_quantidade)

