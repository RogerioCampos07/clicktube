# --Clicktube--

Aplicativo desenvolvido para uso em terminal para realizar downloads de videos e audios de uma famosa plataforma de videos.:smiley:

---

## Instalação

O app foi desenvolvido na linguagem **Python** e com a biblioteca **Click**

Obs: necessário a instalação do gerenciador de dependencias python ***Poetry***
> [poetry.org](https://python-poetry.org/ "Poetry")

Verificar a lista de pacotes usados no app, no arquivo **pyproject.toml**

Após instalação e configuração do Poetry siga os passos abaixo:

### Ambiente virtual

Habilitar o ambiente virtual

```python
>> poetry shell
```

### Instalação dos Pacotes

Instalação dos pacotes listados no arquivo pyproject.toml

```python
>> poetry install
```

---

## Como usar

Digite no terminal:
clicktube (a funcionalidade) e o link do video que quer extrair.

### Downnload de Video

```python
>> clicktube video link
```

### Download de audio

```python
>> clicktube audio link
```
