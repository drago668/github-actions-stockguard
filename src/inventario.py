def clasificar_stock(stock_actual: int, stock_minimo: int) -> str:
	if stock_actual < 0:
		raise ValueError("El stock actual no puede ser negativo")
	if stock_minimo <= 0:
		raise ValueError("El stock minimo debe ser mayor que cero")
	if stock_actual == 0:
		return "AGOTADO"
	if stock_actual <= stock_minimo * 0.5:
		return "CRITICO"
	if stock_actual <= stock_minimo:
		return "BAJO"
	if stock_actual > (stock_minimo * 5):
		return "SOBRESTOCK"
	return "NORMAL"

def calcular_porcentaje(stock_actual: float, stock_maximo: float) -> float:
    if stock_actual < 0 or stock_maximo < 0:
        raise ValueError("El stock no puede ser negativo")
    if stock_maximo == 0:
        raise ZeroDivisionError("El stock máximo no puede ser cero")
    return (stock_actual / stock_maximo) * 100