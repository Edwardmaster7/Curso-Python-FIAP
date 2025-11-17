## Cenário

Você é responsável pelo backend de um e-commerce. Precisa analisar os logs de acesso da API REST para gerar um relatório de uso. O arquivo de log tem 100.000 linhas.

---

### Exemplo de linha do log

```
"2024-10-11 10:23:45|GET|/api/products/123|200|150ms|user_456"
```
Formato: `timestamp|método|endpoint|status|tempo_resposta|user_id`


```python
logs = [ 
    "2024-10-11 10:23:45|GET|/api/products/123|200|150ms|user_456", 
    "2024-10-11 10:23:46|POST|/api/orders|201|300ms|user_789", 
    "2024-10-11 10:23:47|GET|/api/products/456|404|50ms|user_456",
    "2024-10-11 10:23:48|GET|/api/users/789|200|100ms|user_123", 
    "2024-10-11 10:23:49|DELETE|/api/orders/999|500|500ms|user_789", 
    # ... mais 99.995 linhas 
]
```

---

## O que precisa extrair:


- **Total de requisições por método HTTP** (GET, POST, etc.)
- **Total de erros** (status >= 400)
- **Endpoint mais acessado**
- **Usuário com mais requisições**

---

## Restrições/Orientações

- Use **geradores** para processar os logs (não carregar tudo na memória)
- Use **Counter** para contagens
- Use **defaultdict** onde apropriado

---

## Saída esperada

Relatório em formato de dicionário com as métricas.


---

## Exemplo de código


```python
def analisar_logs(logs):
    """
    Analisa logs de API e retorna métricas

    Retorna:
        dict: {
            "total_requisicoes": int,
            "por_metodo": dict,
            "total_erros": int,
            "endpoint_mais_acessado": str,
            "usuario_mais_ativo": str
        }
    """
    from collections import Counter, defaultdict

    # Dica: Itere sobre os logs e faça split por '|'
    # Use Counter para contagens simples
    # Use defaultdict(int) para totais

    metricas = {
        "total_requisicoes": 0,
        "por_metodo": {},
        "total_erros": 0,
        "endpoint_mais_acessado": "",
        "usuario_mais_ativo": ""
    }

    # SEU CÓDIGO AQUI

    return metricas

# Teste básico
resultado = analisar_logs(logs)
print(resultado)
```

---

### Critérios de avaliação

- ✅ **Uso correto de estruturas de dados** (40%)
- ✅ **Eficiência** (geradores, Counter) (30%)
- ✅ **Código pythônico e legível** (20%)
- ✅ **Resultado correto** (10%)

---

**Tempo sugerido:** 20 minutos
