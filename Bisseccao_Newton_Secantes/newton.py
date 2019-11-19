
# Metodo de Newton
    # para k = 1, ... , MAXITER
        # 1. calcular Xk = Xk-1 - f(Xk-1)/f'(Xk-1)
        # 2. se suficientemente proximo, retornar o valor
            # se não, voltar para o passo 1

class Newton:

    # Constructor
    def __init__(self, inf, sup, e, MAXITER, root):
        self.lastX = [inf]            # variavel para indicar o Xk-1 (inicialmente X0)

        self.actualX = 0           # variavel para indicar o X atual (Xk)

        self.fxk = []              # variavel para indicar f calculada em xk
        self.dfxk = []             # variavel para indicar f' calculada em xk

        self.e = e                 # valor de comparacao para condicao de parada
        self.ek = []


        if root == "-4/7":
            self.root = -4/7
        else:
            self.root = 1/6


        self.MAXITER = MAXITER     # numero maximo de iteracoes

        self.inf = inf
        self.sup = sup

    def f(self, x):
        # funcao considerada
        return (42*(x**4)+17*(x**3)+164*(x**2)+68*x-16)

    def derivate(self, x):
        # derivada da funcao
        return (168*(x**3)+51*(x**2)+328*x+68)

    def calculateNewtonIter(self):
        self.fxk.append(self.f(self.lastX[-1]))          # calcula f(xk)
        self.dfxk.append(self.derivate(self.lastX[-1]))  # calcula f'(xk)
        
    def calculateXk(self):
        return (self.lastX[-1] - self.fxk[-1]/self.dfxk[-1])       # xk - f(xk)/f'(xk)

    def calculateNextIter(self):
        self.ek.append(abs(self.lastX[-1] - self.root))
        self.lastX.append(self.actualX)

        if ((self.actualX > self.sup) | (self.actualX < self.inf)):
            return "ERROR - Out of interval"

    def stopCondition(self):
        return (abs(self.fxk[-1]) < self.e) | (abs(self.actualX - self.lastX[-1]) < self.e * max(1, abs(self.actualX)))

    def newtonMethod(self):
        for i in range(self.MAXITER):
            self.calculateNewtonIter()
            self.actualX = self.calculateXk()
            if self.stopCondition():
                self.calculateNewtonIter()
                if (self.calculateNextIter()):
                    return "ERROR - Out of interval"
                self.ek.append(abs(self.lastX[-1] - self.root))
                return self.actualX
            if (self.calculateNextIter()):
                return "ERROR - Out of interval"
        return "ERROR"

    def writeValuesToFile(self):
        f = open("newton_saida.txt", "w+")
        f.write("Iteracao        xk           f(xk)            f'(xk))        ek\n")
        [f.write("   {}     {:8.10f}  {:8.10f}  {:8.10f}  {:8.10f}\n"
                 .format(it, xk, fxk, dfxk, ek))
         for  it, xk, fxk, dfxk, ek
         in zip (range (1,100),
                 self.lastX,
                 self.fxk,
                 self.dfxk,
                 self.ek)]
        f.close()

def main():

    print("Método de Newton")
    print("O X0 inicial será o extremo inferior do intervalo desejado")

    print("A função f possui duas raizes reais")
    print("Insira qual raiz deseja encontrar (1/6 ou -4/7)")
    root = input()


    print("Insira o extremo inferior do intervalo")
    inf = input()

    print("Insira o extremo superior do intervalo")
    sup = input()

    print("Insira a precisão desejada")
    error = input()

    print("Insira o número máximo de iterações")
    iter = input()

    method = Newton(float(inf), float(sup), float(error), int(iter), root)
    result = method.newtonMethod()
    method.writeValuesToFile()
    print(result)


if __name__ == "__main__":
    main()
