# Repositório Git para Disciplina Intro. Computação Quântica na Nuvem I - UFMT
Este repositório foi criado para documentar o conteúdo abordado em sala de aula e servir como referência para os alunos. 

Na disciplina, utilizamos a ferramenta **Qiskit** da IBM para implementar algoritmos quânticos em python, o que permite aos alunos explorar tanto conceitos básicos de programação em Python quanto conceitos abstratos de mecânica quântica, que são fundamentais para os cursos de Física (bacharelado e licenciatura).

## Aula - 1:
Durante a aula, foi incentivado o uso de boas práticas de programação, além de explorar a utilização de pacotes e suas funcionalidades. Também foram abordados conceitos como gerador de estado aleatório e visualização na esfera de Bloch, lógica e sintaxe para a criação de circuitos quânticos, bem como a implementação de um estado aleatório em um circuito quântico.

## Aula - 2:
Durante a aula, foi incentivado o uso de portas de rotação contínua, como Rx, Ry e Rz, em um único qubit. Além disso, foram apresentadas formas de criar estados aleatórios por meio de rotações contínuas em relação aos ângulos $\theta$ e $\phi$, utilizando as portas de rotação Rx, Ry e Rz.

## Aula - 3:
Durante a aula, foi retomado alguns conceitos da aula anterior, na utilização de portas de rotações continuas para criar estados aleatórios a partir dos ângulos $\theta$ e $\phi$, da mesma forma que pode ser feito com a equação da esfera de bloch:
$$ |\psi\rangle = \cos \frac{\theta}{2} |0\rangle + e^{\imath \varphi} \sin \frac{\theta}{2} |1\rangle. $$.
Por fim, realizamos medida dos valores médios de spin nas $x,y$ e $z$.

## Aula - 4:
Durante essa aula, começamos a utilizar portas controladoras, aprendendo sobre qubit de controle e alvo. Com isso, criamos os primeiros estados de Bell, e como gerar todos os outros três estados a partir de rotações do estado $\ket{\beta_{00}}$, sendo os estados:
$$
\begin{align}
    |\beta_{00}\rangle  &= \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)\\
    |\beta_{01}\rangle &= \frac{1}{\sqrt{2}} (|01\rangle + |10\rangle)\\
    |\beta_{10}\rangle &= \frac{1}{\sqrt{2}} (|00\rangle - |11\rangle)\\
    |\beta_{11}\rangle &= \frac{1}{\sqrt{2}} (|01\rangle - |10\rangle).
\end{align}
$$ 
Posteriormente, utilizamos a código super-denso, onde utilizamos um estado emaranhado para enviar dois bits de informação.