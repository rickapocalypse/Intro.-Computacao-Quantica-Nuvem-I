# Repositório Git para Disciplina Intro. Computação Quântica na Nuvem I - UFMT
Este repositório foi criado para documentar o conteúdo abordado em sala de aula e servir como referência para os alunos. 

Na disciplina, utilizamos a ferramenta **Qiskit** da IBM para implementar algoritmos quânticos em python, o que permite aos alunos explorar tanto conceitos básicos de programação em Python quanto conceitos abstratos de mecânica quântica, que são fundamentais para os cursos de Física (bacharelado e licenciatura).

## Aula - 1:
Durante a aula, foi incentivado o uso de boas práticas de programação, além de explorar a utilização de pacotes e suas funcionalidades. Também foram abordados conceitos como gerador de estado aleatório e visualização na esfera de Bloch, lógica e sintaxe para a criação de circuitos quânticos, bem como a implementação de um estado aleatório em um circuito quântico.

## Aula - 2:
Durante a aula, foi incentivado o uso de portas de rotação contínua, como Rx, Ry e Rz, em um único qubit. Além disso, foram apresentadas formas de criar estados aleatórios por meio de rotações contínuas em relação aos ângulos $\theta$ e $\phi$, utilizando as portas de rotação Rx, Ry e Rz.

## Aula - 3:
Durante a aula, foi retomado alguns conceitos da aula anterior, na utilização de portas de rotações continuas para criar estados aleatórios a partir dos ângulos $\theta$ e $\phi$, da mesma forma que pode ser feito com a equação da esfera de bloch:

$$
\begin{align}
|\psi\rangle = \cos \frac{\theta}{2} |0\rangle + e^{\imath \varphi} \sin \frac{\theta}{2} |1\rangle.
\end{align}
$$

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

Posteriormente, utilizamos a código super-denso, onde utilizamos um estado emaranhado para enviar dois bits de informação. Aproveitando o emaranhamento, resolvemos aplicar o  teletransporte quântico O teletransporte quântico se trata do envio de informação quântica entre dois destinatários. Imagine a seguinte situação, Alice e Bob compartilham de um estado de Bell, por praticidade, vamos dizer que é o estado $\ket{\beta_{00}}$. Assim, Alice tem um estado $\ket{\phi}$ que pretende enviar certa informação quântica para Bob. Seja o qubit um outro $\ket{\phi}$ desconhecido, vamos descrever como,

$$
\begin{align}
    \ket{\phi} = a\ket{0} + b\ket{1},
\end{align}
$$

onde $a$ e $b$ são números complexos. O estado inicial do problema pode ser descrito como

$$
\begin{eqnarray}
    \ket{\psi_{AAB}} = \ket{\phi}A \otimes \ket{\beta_{00}}_{AB},
\end{eqnarray}
$$

onde os subíndices $A$ e $B$ indicam a quem pertence tal qubit. Rescrevendo

$$
\begin{align}
    \ket{\psi_{AAB}} = (a\ket{0} + b\ket{1}) \otimes (\frac{\ket{00} + \ket{11}}{\sqrt{2}}),
\end{align}
$$

$$
\begin{align}
        =\frac{a}{\sqrt{2}}\ket{000}{AAB} + \frac{a}{\sqrt{2}}\ket{011}{AAB} + \frac{b}{\sqrt{2}}\ket{100}{AAB} + \frac{b}{\sqrt{2}}\ket{111}{AAB}.
\end{align}
$$

Deixando os qubits de Alice em evidencia, temos

$$
\begin{eqnarray}
        \ket{\psi_{AAB}} = \frac{a}{\sqrt{2}}\ket{00}{AA} \otimes    \ket{0}{B} + \frac{a}{\sqrt{2}}\ket{01}{AA} \otimes \ket{1}{B} +
        \frac{b}{\sqrt{2}}\ket{10}{AA} \otimes \ket{0}{B} +
        \frac{b}{\sqrt{2}}\ket{11}{AA} \otimes \ket{1}{B}.
\end{eqnarray}
$$

Rescrevendo os qubits da Alice em termos da base de Bell

$$
\begin{eqnarray*}
        \ket{\psi_{AAB}} = \frac{a}{\sqrt{2}}(\frac{1}{\sqrt{2}}\ket{\beta_{00}}{AA} + \frac{1}{\sqrt{2}}\ket{\beta_{10}}{AA}) \otimes \ket{0}{B} + \frac{a}{\sqrt{2}}(\frac{1}{\sqrt{2}}\ket{\beta_{01}}{AA} + \frac{1}{\sqrt{2}}\ket{\beta_{11}}{AA}) \otimes \ket{1}{B}\\ + \frac{b}{\sqrt{2}}(\frac{1}{\sqrt{2}}\ket{\beta_{01}}{AA} - \frac{1}{\sqrt{2}}\ket{\beta_{11}}{AA}) \otimes \ket{0}{B} + \frac{b}{\sqrt{2}}(\frac{1}{\sqrt{2}}\ket{\beta_{00}}{AA} - \frac{1}{\sqrt{2}}\ket{\beta_{10}}{AA}) \otimes \ket{1}{B},
    \end{eqnarray*}
$$

agora reorganizando os estado $\ket{\beta_{xy}}$, ficamos com

$$
\begin{eqnarray*}
    \ket{\psi_{AAB}} = \frac{1}{2}\ket{\beta_{00}}{AA} \otimes (a\ket{0} + b\ket{1}){B} + \frac{1}{2}\ket{\beta_{10}}{AA} \otimes (a\ket{0} - b\ket{1}){B}\\ + \frac{1}{2}\ket{\beta_{01}}{AA} \otimes (a\ket{1} + b\ket{0}){B} + \frac{1}{2}\ket{\beta_{11}}{AA} \otimes (a\ket{1} - b\ket{0}){B}.
\end{eqnarray*}
$$

Agora Alice tem probabilidade $\frac{1}{4}$ de medir um dos quatro estados de Bell. Dependendo do resultado da medida de Alice o estado vai resultar em um certo estado que está em posse de Bob. As possíveis medidas $xy$ de Alice pode ser vista a seguir

$$
\begin{eqnarray*}
00 \to \ket{\beta_{00}}{A} \otimes ((a\ket{0} + b\ket{1}){B}),\\
        01 \to \ket{\beta_{01}}{A} \otimes ((a\ket{1} + b\ket{0}){B}),\\
        10 \to \ket{\beta_{10}}{A} \otimes ((a\ket{0} - b\ket{1}){B}),\\
        11 \to \ket{\beta_{11}}{A} \otimes ((a\ket{1} - b\ket{0}){B}).
\end{eqnarray*}
$$

Note que os quatro possíveis estados quânticos de Bob são exatamente o estado $\ket{\phi}$ que Alice tinha a menos de um operação unitária de $\textit{X}$ e/ou $\textit{Z}$, como pode ser visto a seguir

$$
\begin{eqnarray*}
    (a\ket{0} + b\ket{1}) = a\ket{0} + b\ket{1},\\
    Z(a\ket{0} - b\ket{1}) = a\ket{0} + b\ket{1},\\
    X(a\ket{1} + b\ket{0}) = a\ket{0} + b\ket{1},\\
    ZX(a\ket{1} - b\ket{0}) = a\ket{0} + b\ket{1}.
\end{eqnarray*}
$$

É importante ressaltar que o teletransporte da informação do estado quântico só é realizado se Alice medir o seu par de qubits na base de Bell e informar classicamente a Bob os bits necessário para que ele possa realizar as transformações necessárias e obter o exato estado que Alice havia enviado.

## Aula 5
Durante a aula, foi proposto a criação de circuitos especificos como o do full adder que realiza a adição de dois bits em um computador clássico. Assim, foi criado um circuito quântico que realiza a mesma tarefa do computador classicos, utilizando portas Toffoli e CNOT (A porta Toffoli pode ser utilizada para simular diversas portas clássicas de forma reversível). Também foi incentivado o uso do oracle para utilizarf o algoritmo de Deutsch e Grover. Por fim, ressaltando a importancia de verificar a quantidade de aplicações do difusor de Grover, para obter uma boa medida.
