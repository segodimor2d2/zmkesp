import config
# -----------------------------
# Função de log centralizada
# -----------------------------
def log(*args, **kwargs):
    level = None  # Sem nível por padrão
    if len(args) > 1 and isinstance(args[1], int) and args[1] >= 0:
        level = args[1]
        args = (args[0],) + args[2:]  # Remove o level dos args
    
    debug_level = getattr(config, 'DEBUG', None)
    
    if debug_level is not None and level is not None and level != debug_level:
        return
    
    if debug_level is not None and level is None:
        return
    
    print(*args, **kwargs)
