import csv
import numpy as np
import math as mt


class MMQ:
    def __init__(self, file, polynomium_degree):

        self.data_x = []
        self.data_y = []

        # grau do metodo
        self.degree = polynomium_degree

        self.data_xk = []

        # valores do sistema linear
        self.leftmatrix = []
        self.rightvector = []

        # constantes encontradas
        self.constants = []

        arquivo = open(file)
        linhas = csv.reader(arquivo)

        iteracao = iter(linhas)
        next(iteracao)
        for linha in iteracao:
            self.data_x.append(float(linha[0]))
            self.data_y.append(float(linha[1]))

    def calc_xk_trig(self):
        all_xk = []
        new_xi = []

        # calcula primeiro xk (cos(0))
        for j in range(0, len(self.data_x)):
            new_xi.append(mt.cos(0))
        all_xk.append(new_xi)

        # calcula todos os xks
        for i in range(1, self.degree + 1):
            new_xi = []
            for j in range(0, len(self.data_x)):
                new_xi.append(mt.cos(i * self.data_x[j]))
            all_xk.append(new_xi)

            new_xi = []
            for j in range(0, len(self.data_x)):
                new_xi.append(mt.sin(i * self.data_x[j]))
            all_xk.append(new_xi)

        self.data_xk = all_xk
        return

    def createLinearSystem_trig(self):
        new_leftmatrix = []
        new_rightvector = []

        matrix_line = []

        # calcula primeira iteracao para criar as matriz do sistema
        for i in range(0, len(self.data_xk)):
            if i is 0:
                matrix_line.append(len(self.data_x))
            else:
                matrix_line.append(0)

        new_leftmatrix.append(matrix_line)
        new_rightvector.append(self.dot_product(self.data_y, self.data_xk[0]))

        # realiza todas as iteracoes
        for i in range(1, len(self.data_xk)):
            matrix_line = []
            for j in range(0, len(self.data_xk)):
                if j is i:
                    matrix_line.append(len(self.data_x) / 2)
                else:
                    matrix_line.append(0)

            new_leftmatrix.append(matrix_line)
            new_rightvector.append(self.dot_product(self.data_y, self.data_xk[i]))

        self.leftmatrix = new_leftmatrix
        self.rightvector = new_rightvector

        return

    def calc_xk(self):
        all_xk = []

        # calcula todos os xk
        for i in range(0, self.degree + 1):
            new_xi = []
            for j in range(0, len(self.data_x)):
                new_xi.append(pow(self.data_x[j], i))
            all_xk.append(new_xi)

        self.data_xk = all_xk
        return

    def createLinearSystem(self):
        new_leftmatrix = []
        new_rightvector = []

        # cria matriz esquerda e o vetor a direita do sistema linear
        for i in range(0, self.degree + 1):
            matrix_line = []
            for j in range(0, self.degree + 1):
                matrix_line.append(self.dot_product(self.data_xk[j], self.data_xk[i]))

            new_leftmatrix.append(matrix_line)
            new_rightvector.append(self.dot_product(self.data_y, self.data_xk[i]))

        self.leftmatrix = new_leftmatrix
        self.rightvector = new_rightvector

        return

    # produto escalar
    def dot_product(self, a, b):
        if len(a) is not len(b):
            print("o tamanho dos vetores nao sao iguais!")
            return False

        result = 0

        for value1, value2 in zip(a, b):
            result += value1 * value2

        return result

    # utiliza Numpy.linalg.solve() para resolver o sistema
    def solveSystem(self):
        self.constants = np.linalg.solve(self.leftmatrix, self.rightvector)
        return

    # debug
    def print_data(self):
        print(self.data_x)
        print(self.data_y)
        print(self.data_xk)
        print(self.leftmatrix)
        print(self.rightvector)

    # escreve aproximacao trigonometrica encontrada
    def printAproxPolyFunction(self):
        for i in range(0, self.degree + 1):
            print(f"({self.constants[i]}.*x.^{i})", end="")
            if i is not self.degree:
                print(f" + ", end="")

        print()
        return

    # escreve aproximacao polinomial encontrada
    def printAproxTrigFunction(self):
        print(f"({self.constants[0]}) + ", end="")
        for i in range(1, self.degree + 1):
            print(
                f"({self.constants[i*2 -1]}.*cos({i}.*x)) + ({self.constants[i*2]}.*sin({i}.*x)) ",
                end="",
            )
            if i is not self.degree:
                print(f" + ", end="")

        print()
        return


def main():

    mmq = MMQ("Cidade03.csv", 80)  # cria Objeto
    mmq.calc_xk()  # calcula todos os xk
    mmq.createLinearSystem()  # criar sistema linear
    mmq.solveSystem()  # resolve o sistema
    mmq.printAproxPolyFunction()  # escreve funcao


if __name__ == "__main__":
    main()
