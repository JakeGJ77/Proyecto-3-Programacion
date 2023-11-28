import json

# Cargar datos desde el archivo JSON
with open(r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json", 'r') as file:
    menu_data = json.load(file)

# Crear el HTML dinámicamente
html_content = """
    <!-- ... tu código HTML existente ... -->
"""

for category, products in menu_data.items():
    html_content += f"""
        <div class="menu" id="{category}Menu">
    """

    for product in products:
        html_content += f"""
            <div class="item">
                <div class="item__header">
                    <h3 class="item__title">{product['nombre']}</h3>
                    <span class="item__dots"></span>
                    <span class="item__price">${product['precio']}</span>
                </div>
                <p class="item__description">Calorías: {product['calorias']}</p>
                <img src="{product['imagen']}" alt="{product['nombre']}" class="item__image">
                <p class="item__description">Ingredientes: {', '.join(product['ingredientes'])}</p>
            </div>
        """

    html_content += """
        </div> <!-- End {category} Menu -->
    """

# Agregar el contenido HTML generado al final del archivo
with open(r'C:\Users\Jake\Desktop\Pagina Web menu\menu.html', 'a') as file:
    file.write(html_content)
