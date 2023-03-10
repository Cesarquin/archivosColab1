#!/usr/bin/env python
# coding: utf-8

# # Ecuaciones latex:
# 
# $$ \sigma=\sqrt{a^2+b^2}  $$
# $$ \Delta$$
# $$ \alpha $$
# $$ \sum_0^\infty(x) $$
# $$ \begin{vmatrix}1&2\\3&4\end{vmatrix} $$
# 
# \begin{equation*}
# \left( \sum_{k=1}^{n} x^k \right) \times \sum_{k=0}^{\infty} {x^{k+1}} 
# \end{equation*}
# ## Video:
# [video](https://www.youtube.com/watch?v=p2I0Al8rhmk)

# In[27]:


get_ipython().system('where jupyter ')
# el iniciar con el caracter: '!', permite comandos de consola
print("\n\nA continuación se muestran las carpetas del directorio HOME: \n\n")
get_ipython().system('dir')
# es decir, desde aca se puede dar 'pip install paquete'


# $$ \text{La Fórmula Cuadrática es }x = \frac {-b \pm \sqrt {b^2 - 4ac}}{2a} $$
# 
# $$ \left( \frac{a}{b} \right) ^{2}$$
# 
# La Fórmula Cuadrática es $ x = \frac {-b \pm \sqrt {b^2 - 4ac}}{2a}$
# 
# $$ a x^2 + b x + c = 0 $$
# 
# $$ x_{1/2} = \frac {-b \pm \sqrt {b^2 - 4ac}}{2a} $$
# 
# $$ \lim_{x \to \infty} \left( \frac{1}{x} \right)$$
# 
# $$ r_\alpha \cdot s_\beta = \left( r \cdot s \right)_{\alpha + \beta }$$
# 
# $$ \overline{AB}$$
# 
# $$ \int_{a}^{b} x dx$$
# 
# $$ \sum_{i=1}^{n} i^2$$
# 
# $$
# \frac{1}{2}\\
# e^{i \pi}+1=0\\
# \sqrt[n]{3^5}
# $$
# 
# 
# # Otros simbolos
# #### Ángulos:
# Angulo izq : $\langle$
# 
# Ángulo Der : $\rangle$
# 
# Ángulo entre dos vectores u y v	: $\langle \vec{u},\vec{v}\rangle$	
# 
# $$ \vec{AB} \, \cdot \, \vec{CD} =0  \Rightarrow  \vec{AB} \, \perp\, \vec{CD}$$
# 
# ### Conjuntos y lógica
# 
# $$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$
# 
# #### Operadores:
# 
# ![image](https://miro.medium.com/max/422/1*8qpYLNPmlvEoEMaoksfINA.png)
# 
# ![image](https://miro.medium.com/max/482/1*IgyFkP0Z9Dk6QQumL5sClQ.png)
# 
# ![image](https://miro.medium.com/max/429/1*ODvw1B-e_Kpgl4iQ93O86A.png)
# 
# 
# #### Función signo: 
# $$
# sign(x) = \left\{
#     \begin{array}\\
#         1 & \mbox{if } \ x \in \mathbf{N}^* \\
#         0 & \mbox{if } \ x = 0 \\
#         -1 & \mbox{else.}
#     \end{array}
# \right.
# $$
# 
# 
# 
# $$
#  \left.
#     \begin{array} \\
#         \alpha^2 = \sqrt5 \\
#         \alpha \geq 0 
#     \end{array}
# \right \}\alpha = 5 
# $$
# 
# #### Matrices:
# 
# Sin paréntesis:
# \begin{matrix}
# 1 & 2 & 3\\
# a & b & c
# \end{matrix}
# 
# Paréntesis circular:
# \begin{pmatrix}
# 1 & 2 & 3\\
# a & b & c
# \end{pmatrix}
# 
# Corchetes:
# \begin{Bmatrix}
# 1 & 2 & 3\\
# a & b & c
# \end{Bmatrix}	
# 
# Barras:
# \begin{vmatrix}
# 1 & 2 & 3\\
# a & b & c
# \end{vmatrix}
# 
# Doble barra:
# \begin{Vmatrix}
# 1 & 2 & 3\\
# a & b & c
# \end{Vmatrix}
# 
# 

# In[28]:


def inver(b):
    a=0
    while b%10!=0:
        c=b%10
        b=int(b/10)
        a+=c
    
    return a
b=restica(8,3)
caract=["genial","guapo","pilo","el mejor profesor"]
print(caract[3])
caract.sort()
print(caract)
var1=f"Cesar es {caract[3]}"
print(var1)
caract.append("maravilloso")
b=int(input("Ingrese el número a revertir: "))
print(inver(b))
print(caract)


# In[33]:


dic={"nombre":["Cesar","Augusto"],"Apellido":["Quintero","Obando"]}
print(dic["nombre"])


# In[ ]:




