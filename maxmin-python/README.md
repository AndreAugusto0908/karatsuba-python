# Projeto MaxMin Select

O MaxMin Select é um projeto desenvolvido para demonstrar e analisar o algoritmo de seleção simultânea do maior e menor elementos usando a técnica de divisão e conquista. Este projeto implementa uma solução eficiente que encontra o menor e maior elemento de um array com complexidade otimizada.

## Algoritmo MaxMin Select

O algoritmo MaxMin Select utiliza a estratégia de divisão e conquista para encontrar simultaneamente o menor e maior elemento de um array. Esta abordagem é significativamente mais eficiente que métodos ingênuos, reduzindo o número de comparações necessárias de 2n-2 para aproximadamente 3n/2-2.

### Estratégia Divisão e Conquista

A técnica de divisão e conquista divide o problema em subproblemas menores, resolve cada subproblema recursivamente e combina os resultados para obter a solução final. No caso do MaxMin Select:

1. **Dividir**: O array é dividido em duas metades
2. **Conquistar**: Cada metade é processada recursivamente para encontrar seu min e max
3. **Combinar**: Os resultados são combinados para determinar o min e max globais

## Complexidade Assintótica

### Complexidade de Tempo
- **Melhor caso**: O(n)
- **Caso médio**: O(n)
- **Pior caso**: O(n)

### Complexidade de Espaço
- **Espaço**: O(log n) - devido às chamadas recursivas na pilha

### Análise de Comparações
O algoritmo realiza aproximadamente **3n/2 - 2** comparações, que é próximo ao número mínimo teórico necessário para encontrar tanto o menor quanto o maior elemento.

## Casos Base e Recursivos

### Casos Base:
1. **Um elemento**: O elemento é simultaneamente o menor e o maior
2. **Dois elementos**: Uma única comparação determina qual é menor e qual é maior

### Caso Recursivo:
- Arrays com mais de dois elementos são divididos no meio
- Cada metade é processada recursivamente
- Os resultados são combinados com duas comparações adicionais

## Dependências

Este projeto utiliza apenas bibliotecas padrão do Python, não sendo necessária instalação de dependências externas.

## Ambiente Virtual

### Passo 1: Criar e ativar o ambiente virtual

É recomendável usar um ambiente virtual para isolar o projeto:

```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar no macOS e Linux
source .venv/bin/activate

# Ativar no Windows
.venv\Scripts\activate
```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:

```bash
python maxmin_select.py
```

## Versão do Python

Este projeto foi desenvolvido e testado na versão 3.8+ do Python.

## Explicação da Função

### Arquivo: `maxmin_select.py`

**Objetivo**: Implementa o algoritmo MaxMin Select usando divisão e conquista.

#### `maxmin_select(arr, inicio, fim)`

**Descrição**: Função principal que implementa o algoritmo recursivo de seleção simultânea.

**Parâmetros**:
- `arr`: Lista de elementos a serem analisados
- `inicio`: Índice inicial do subarray
- `fim`: Índice final do subarray

**Retorno**: 
- Tupla `(min, max)` contendo o menor e maior elementos do subarray

**Lógica do Algoritmo**:

1. **Caso base - Um elemento** (`inicio == fim`):
   ```python
   return arr[inicio], arr[inicio]
   ```

2. **Caso base - Dois elementos** (`fim - inicio == 1`):
   ```python
   if arr[inicio] < arr[fim]:
       return arr[inicio], arr[fim]
   else:
       return arr[fim], arr[inicio]
   ```

3. **Caso recursivo - Mais de dois elementos**:
   ```python
   meio = (inicio + fim) // 2
   min1, max1 = maxmin_select(arr, inicio, meio)
   min2, max2 = maxmin_select(arr, meio + 1, fim)
   
   min_total = min(min1, min2)
   max_total = max(max1, max2)
   return min_total, max_total
   ```

## Exemplo de Uso

```python
# Array de exemplo
meu_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Chamada da função
menor, maior = maxmin_select(meu_array, 0, len(meu_array) - 1)

print(f"Menor elemento: {menor}")  # Output: 5
print(f"Maior elemento: {maior}")  # Output: 90
```

## Saída da Execução

```
Array: [3, 1, 4, 1, 5, 9, 2, 6, 5]
Menor: 1, Maior: 9

Array: [64, 34, 25, 12, 22, 11, 90, 5]
Menor: 5, Maior: 90

Array: [10, 5, 8, 2, 7, 1, 9]
Menor: 1, Maior: 10

Array: [42]
Menor: 42, Maior: 42

Array: [7, 3]
Menor: 3, Maior: 7
```

## Vantagens do Algoritmo

1. **Eficiência**: Reduz significativamente o número de comparações necessárias
2. **Otimalidade**: Próximo ao número mínimo teórico de comparações
3. **Elegância**: Solução clara e concisa usando divisão e conquista
4. **Escalabilidade**: Desempenho consistente mesmo com arrays grandes

## Comparação com Abordagem Ingênua

| Aspecto | Abordagem Ingênua | MaxMin Select |
|---------|-------------------|---------------|
| Comparações | 2n - 2 | 3n/2 - 2 |
| Complexidade | O(n) | O(n) |
| Implementação | Simples | Moderada |
| Eficiência | Menor | Maior |

## Análise Matemática

Para um array de tamanho n, o número de comparações T(n) segue a recorrência:

```
T(n) = 2T(n/2) + 2    para n > 2
T(2) = 1
T(1) = 0
```

Resolvendo esta recorrência, obtemos: **T(n) = 3n/2 - 2**

## Casos de Teste

O projeto inclui diversos casos de teste que demonstram o funcionamento do algoritmo:

- Arrays com múltiplos elementos
- Array com um único elemento
- Array com dois elementos
- Arrays com elementos negativos
- Arrays com elementos duplicados

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Adicionar novos casos de teste
- Otimizar o código existente

## Licença

Este projeto está licenciado sob a Licença MIT.