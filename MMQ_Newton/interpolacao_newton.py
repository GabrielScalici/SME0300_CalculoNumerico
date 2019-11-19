import csv
from decimal import Decimal


class Newton:
    def __init__(self, file):
        self.data_cidade = []
        self.newton_f = []  # valores de  f[]
        self.newton_x = []  # valores de xk

        arquivo = open(file)
        linhas = csv.reader(arquivo)

        iteracao = iter(linhas)
        next(iteracao)
        for linha in iteracao:
            self.newton_x.append(linha[0])
            self.data_cidade.append(
                (Decimal(linha[1]), Decimal(linha[0]), Decimal(linha[0]))
            )

    # chama metodo recursivo e transfere valores para newton_f
    def newtonMethod(self):
        method = self.rec_method(self.data_cidade)

        for f in method:
            self.newton_f.append(f[0])

        return

    def rec_method(self, list):
        # condicao de parada
        if len(list) is 1:
            return [list[0]]

        # cria pares para serem calculados
        new_list = []
        pairs = zip(list[::1], list[1::1])

        # cria lista de valores para a proxima iteracao
        for t in pairs:
            new_list.append((self.calc_dif_div(t), t[0][1], t[1][2]))

        return [list[0]] + self.rec_method(new_list)

    # calcula das diferencas divididas
    def calc_dif_div(self, t):
        return (t[1][0] - t[0][0]) / (t[1][2] - t[0][1])

    # debug
    def print_data(self):
        print(self.data_cidade)

    # escreve funcao na tela
    def print_newton(self):
        print("diferenca dividida")

        for i in range(0, len(self.newton_x)):
            for j in range(0, i):
                print(f"(x - {self.newton_x[j]}).*", end="")
            print(f"({self.newton_f[i]}) + ", end="")


def main():

    newton = Newton("Cidade03.csv")  # cria objeto

    newton.newtonMethod()  # realiza o metodo de newton
    newton.print_newton()  # escreve funcao


if __name__ == "__main__":
    main()
