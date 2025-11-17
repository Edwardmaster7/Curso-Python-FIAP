# - **Total de requisições por método HTTP** (GET, POST, etc.)
# - **Total de erros** (status >= 400)
# - **Endpoint mais acessado**
# - **Usuário com mais requisições**

from itertools import count
from operator import indexOf
from collections import Counter, defaultdict

def analisar_logs(logs: list):
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

    total_req = Counter(log for log in logs).total()

    logs = [log.split("|") for log in logs]
    sum_by_method = dict(Counter(log[1] for log in logs))
    total_err = Counter(log[3] for log in logs if int(log[3]) >= 400).total()
    most_accessed_endpoint = max(dict(Counter(log[2] for log in logs)))
    user_with_more_requests = max(dict(Counter(log[5] for log in logs)))

    metricas["total_requisicoes"] = total_req
    metricas["por_metodo"] = sum_by_method
    metricas["total_erros"] = total_err
    metricas["endpoint_mais_acessado"] = most_accessed_endpoint
    metricas["usuario_mais_ativo"] = user_with_more_requests


    return metricas


if __name__ == "__main__":
    logs = [ 
    "2024-10-11 10:23:45|GET|/api/products/123|200|150ms|user_456", 
    "2024-10-11 10:23:46|POST|/api/orders|201|300ms|user_789", 
    "2024-10-11 10:23:47|GET|/api/products/456|404|50ms|user_456",
    "2024-10-11 10:23:48|GET|/api/users/789|200|100ms|user_123", 
    "2024-10-11 10:23:49|DELETE|/api/orders/999|500|500ms|user_789", 
    ]

    # Teste básico
    resultado = analisar_logs(logs)

    print(resultado)
