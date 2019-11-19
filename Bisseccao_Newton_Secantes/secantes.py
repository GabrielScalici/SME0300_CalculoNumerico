# Metodo da Secante

class Secante:

    def __init__(self, X0, X1, e, MAXITER, root):
        self.x0 = [X0]
        self.x1 = [X1]
        self.x = []
        self.e = e

        self.fx  = []
        self.fx0 = []
        self.fx1 = []
        self.ek = []

        if root == "-4/7":
            self.root = -4/7
        else:
            self.root = 1/6


        self.MAXITER = MAXITER

    def f(self, x):
        return (42*(x**4)+17*(x**3)+164*(x**2)+68*x-16)

    def calculatex(self):
        self.fx0.append(self.f(self.x0[-1]))
        self.fx1.append(self.f(self.x1[-1]))
        return ((self.x0[-1] * self.fx1[-1] - self.x1[-1] * self.fx0[-1] )
                / (self.fx1[-1] - self.fx0[-1]))

    def stopCondition(self):
        return (abs(self.fx[-1]) < self.e) | (abs(self.x[-1] - self.x1[-1]) < self.e * max(1, abs(self.x[-1])))

    def calculateSecantIter(self):
        self.x.append(self.calculatex())
        self.fx.append(self.f(self.x[-1]))
        self.ek.append(abs(self.x[-1] - self.root))
            

    def calculateNextIter(self):
        self.x1.append(self.x0[-1])
        self.x0.append(self.x[-1])

    def secanteMethod(self):
        i = 0
        while i <= self.MAXITER:
            self.calculateSecantIter()
            if self.stopCondition():
                return self.x[-1]
            self.calculateNextIter()
        return "ERROR"

    def writeValuesToFile(self):
        f = open("secantes_saida.txt", "w+")
        f.write("Iteracao        xk           f(xk)            e\n")
        [f.write("   {}     {:8.10f}  {:8.10f}  {:8.12f}\n"
                 .format(it, xk, fxk, e))
         for  it, xk, fxk, e 
         in zip (range (1,100),
                 self.x,
                 self.fx,
                 self.ek)]
        f.close()


def main():

    print("Método das Secantes")

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

    method = Secante(float(inf), float(sup), float(error), int(iter), root)
    result = method.secanteMethod()
    print(str(result))
    method.writeValuesToFile()

if __name__ == "__main__":
    main()
