
# Metodo da biseccao
    # Dado um intervalo [a,b], cujo os valores de f(a) e f(b) sao opostos
    # 1. calcula-se c, o ponto medio entre [a,b]
    # 2. calcula-se f(c)
    # 3. se f(c) suficientemente pequeno, retorna o valor
         # caso contrario, substitui c por a ou b. Va para o passo 1


class Bisection:

    # Constructor
    def __init__(self, a, b, e, MAXITER, root):
        self.a = [a]          # numero a para o intervalo [a,b]
        self.b = [b]          # numero b para o intervalo [a,b]
        self.xk = []          # novo intervalo dado pela media de a e b

        self.fa = []         # valor de f(a)
        self.fb = []         # valor de f(b)
        self.fxk = []         # valor de f(c)
        
        self.e = e  # intervalo suficiente para parar
        self.ek = []


        if root == "-4/7":
            self.root = -4/7
        else:
            self.root = 1/6

        self.MAXITER = MAXITER

    def f(self, x):
        #funcao para ser feito
        return (42*(x**4)+17*(x**3)+164*(x**2)+68*x-16)

    def stopCondition(self):
        return (abs(self.fxk[-1]) < self.e) | (abs(self.xk[-1] - self.a[-1]) < self.e * max(1, self.xk[-1]))

    def calculateBisectionIter(self):
        self.fa.append(self.f(self.a[-1]))
        self.fb.append(self.f(self.b[-1]))
        self.xk.append((self.a[-1]+self.b[-1])/2)
        self.fxk.append(self.f(self.xk[-1]))
        self.ek.append(abs(self.xk[-1] - self.root))
        return


    def getNewInterval(self):
        if (self.fa[-1]*self.fxk[-1]) >= 0:
                self.a.append(self.xk[-1])
                self.b.append(self.b[-1])
        else:
                self.a.append(self.a[-1])
                self.b.append(self.xk[-1])
        return


    def bisectionMethod(self, i):
        if i < self.MAXITER:
            self.calculateBisectionIter()
            if self.stopCondition():
                return (self.xk[-1])
            else:
                self.getNewInterval()
                return self.bisectionMethod(i+1)
        return "ERROR"

    def writeValuesToFile(self):
        f = open("bissecao_saida.txt", "w+")
        f.write("Iteracao        xk           f(xk)            ak            bk           ek\n")
        [f.write("   {}     {:8.10f}  {:8.10f}  {:8.10f}  {:8.10f}  {:8.10f}\n"
                 .format(it, xk, fxk, ak, bk, ek))
         for  it, xk, fxk, ak, bk, ek
         in zip (range (1,100),
                 self.xk,
                 self.fxk,
                 self.a,
                 self.b,
                 self.ek)]
        f.close()



def main():
    print("Método da Bisseção")
    
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

    method = Bisection(float(inf), float(sup), float(error), int(iter), root)
    result = method.bisectionMethod(0)

    method.writeValuesToFile()
    print(result)


if __name__ == "__main__":
    main()
