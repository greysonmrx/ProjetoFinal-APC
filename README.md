<h1 align="center">
    Caça Palavras
</h1>

<h3 align="center">
  Projeto final da disciplina de Algoritmos e Programação de Computadores
</h3>

<p align="center">Prof.: Tacito Neves</p>

<p align="center">
  <a href="#-equipe">Equipe</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-funciona-o-projeto">Como funciona o projeto?</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-executando-o-projeto">Executando o projeto</a>
</p>

## 🎓 Equipe

- Greyson Mascarenhas Santos Filho
- Carlos Daniel de Lima Feitosa
- Gabriel da Silva Pereira

## ❓ Como funciona o projeto?

Primeiro, uma lista é criada com os todos nomes dos aquivos que serão lidos e que serão escritos.

Em seguida, é feita uma iteração com os itens dessa lista, e para cada iteração: 
  1. É criada a variável `words` que tem como valor uma lista com todas as palavras que estão no arquivo para serem procuradas.
  2. É criada a variável `matrix` que recebe uma matriz com todas as letras do caça-palavras.
  3. É criada a variável `positions` que tem como valor uma lista vazia, para posteriormente receber as posições de cada palavra encontrada no caça-palavras.
  4. É feita uma iteração com todas as palavras que estão no arquivo para serem procuradas, e para cada iteração:
      1. É criada a variável `wordPosition` que tem como valor uma lista com as posições de cada letra que compõe a palavra encontrada.
      2. É feita uma verificação para saber se a palavra foi realmente encontrada, e caso ela tenha sido encontrada, vai ser adicionado à variável `positions` as posições de cada letra que compõe a palavra encontrada.
  5. É executado a função `writeFile` que escreve no arquivo de resposta uma matriz com todas as palavras encontradas.

## 💻 Executando o projeto

### Requisitos

- [Python 3+](https://www.python.org/downloads/)

**Clone o projeto e acesse a pasta**

```bash
$ git clone https://github.com/greysonmrx/ProjetoFinal-APC.git && cd ProjetoFinal-APC
```

**Execute o comando abaixo**

```bash
$ python ./projeto_final.py
```
