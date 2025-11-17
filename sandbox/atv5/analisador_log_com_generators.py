# - **Total de requisições por método HTTP** (GET, POST, etc.)
# - **Total de erros** (status >= 400)
# - **Endpoint mais acessado**
# - **Usuário com mais requisições**

from itertools import count
from operator import indexOf
from collections import Counter, defaultdict

def log_iterator(logs):
    """Generator que itera sobre os logs"""
    for log in logs:
        yield log


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
        "usuario_mais_ativo": "",
    }
    
    # Contadores para acumular dados
    count_methods = Counter()
    count_access_by_endpoint = Counter()
    count_users = Counter()
    total_requests = 0
    total_errors = 0

    for log in log_iterator(logs):
        partes = log.split("|")

        total_requests += 1

        # Assumindo formato: timestamp|método|endpoint|status|usuário
        metodo = partes[1]
        endpoint = partes[2]
        status = int(partes[3])
        usuario = partes[4] if len(partes) > 4 else "unknown"

        count_methods[metodo] += 1
        count_access_by_endpoint[endpoint] += 1
        count_users[usuario] += 1

        if status >= 400:
            total_errors += 1

    # Preencher métricas finais
    metricas["total_requisicoes"] = total_requests
    metricas["por_metodo"] = dict(count_methods)
    metricas["total_erros"] = total_errors
    metricas["endpoint_mais_acessado"] = count_access_by_endpoint.most_common(1)[0][0] if count_access_by_endpoint else ""
    metricas["usuario_mais_ativo"] = count_users.most_common(1)[0][0] if count_users else ""

    return metricas

