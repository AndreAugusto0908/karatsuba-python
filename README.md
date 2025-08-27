# Projeto KaratsubaMultiplication

## 📌 Sobre o Projeto

O **KaratsubaMultiplication** é um projeto educativo desenvolvido para demonstrar o funcionamento do algoritmo de Karatsuba, um método eficiente de multiplicação de inteiros grandes. Diferente da multiplicação tradicional (com complexidade quadrática), o algoritmo de Karatsuba utiliza apenas **três chamadas recursivas** em vez de quatro, tornando-se mais eficiente para números grandes.

---

## 🧮 O que é o algoritmo de Karatsuba?

O algoritmo de **Karatsuba** foi desenvolvido por Anatoly Karatsuba em 1960 e é considerado um dos primeiros algoritmos de multiplicação mais rápidos que o método tradicional.  

Enquanto a multiplicação convencional de números de \(n\) dígitos tem complexidade:

\[
O(n^2)
\]

O algoritmo de Karatsuba reduz a complexidade para:

\[
O(n^{\log_2 3}) \approx O(n^{1.585})
\]

Isso o torna vantajoso para cálculos com números muito grandes.

---

## ⚙️ Como o algoritmo funciona?

Dado dois números \(x\) e \(y\), o algoritmo segue os seguintes passos:

1. **Caso base**: Se \(x\) ou \(y\) forem menores que 10, retorna o produto direto.
2. **Divide os números**:  
   Se \(x = A \cdot 10^q + B\) e \(y = C \cdot 10^q + D\), onde:  
   - \(A, C\): partes mais significativas (alta ordem).  
   - \(B, D\): partes menos significativas (baixa ordem).
3. **Calcula três multiplicações recursivas**:  
   - \(z2 = A \times C\)  
   - \(z0 = B \times D\)  
   - \(z1 = (A+B)(C+D) - z2 - z0\)
4. **Combina os resultados**:  
   \[
   resultado = (z2 \cdot 10^{2q}) + (z1 \cdot 10^q) + z0
   \]

---

Aqui está o README no formato Markdown pronto para ser salvo como `README.md`:

## ▶️ Como executar o projeto

### 1. Criar e ativar ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv .venv
```

Ativar:

* **Linux/macOS**:

  ```bash
  source .venv/bin/activate
  ```
* **Windows**:

  ```bash
  .venv\Scripts\activate
  ```

### 2. Rodar o script

Como não há dependências externas, basta rodar o arquivo:

```bash
python main.py
```

### 3. Versão utilizada

O projeto foi desenvolvido em **Python 3.13.0**, mas deve funcionar em versões ≥ 3.8.

---

## 📊 Relatório Técnico

### Complexidade do algoritmo

* **Multiplicação tradicional**:

  $$
  O(n^2)
  $$
* **Karatsuba**:

  $$
  O(n^{\log_2 3}) \approx O(n^{1.585})
  $$

### Pontos fortes

✅ Mais rápido que o método tradicional para números grandes.
✅ Usa apenas chamadas recursivas e operações básicas.
✅ Base teórica sólida para algoritmos mais avançados como Toom-Cook e FFT.

### Pontos fracos

⚠️ Para números pequenos, o overhead da recursão torna-o mais lento que a multiplicação simples.
⚠️ Implementações práticas modernas (como em bibliotecas de álgebra computacional) utilizam variações mais sofisticadas.

---

## 📌 Saída de Execução

```
Resultado do algoritmo de Karatsuba: 1082152022374638
Resultado da multiplicação normal:   1082152022374638
```

Ambos os resultados são iguais, validando a implementação.

---

## 📜 Licença

Este projeto está licenciado sob a **Licença MIT**.

```

Agora, basta copiar esse conteúdo e salvar no arquivo `README.md` dentro do seu repositório!
```
