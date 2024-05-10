from functools import partial

class SimpleOperations():
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return price * (1 - discount)


    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return price * (1 + tax_rate)

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
# Aplicar descuento del 20%
apply_20_percent_discount = partial(operations.apply_discount, discount=0.20)

# Calcular el impuesto al valor agregado (IVA)
calculate_vat_tax = partial(operations.calculate_tax, tax_rate=0.21)

# Precio original
precio_original = 100

# Usar las funciones preconfiguradas.
precio_con_descuento = apply_20_percent_discount(precio_original)
impuesto_vat = calculate_vat_tax(precio_con_descuento)

# Imprimir el precio con descuento y el impuesto VAT resultante
print("Precio con descuento del 20%:", precio_con_descuento)
print("Impuesto al valor agregado (VAT):", impuesto_vat)
