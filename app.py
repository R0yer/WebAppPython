from flask import Flask, render_template

app = Flask(__name__)

listas = [
    {
        'nombre': 'Compras',
        'slug': 'compras',
        'descripcion': 'Lista de cosas por comprar esta semana.'
    },
    {
        'nombre': 'Estudio',
        'slug': 'estudio',
        'descripcion': 'Temas y tareas para estudiar y practicar.'
    },
    {
        'nombre': 'Proyecto',
        'slug': 'proyecto',
        'descripcion': 'Actividades pendientes del proyecto actual.'
    }
]

@app.route('/')
def home():
    title = 'Mi primera web con Flask'
    mensaje = '¡Bienvenido a mi sitio web básico de python!'
    return render_template('index.html', title=title, mensaje=mensaje, listas=listas)

@app.route('/lista/<slug>')
def detalle_lista(slug):
    lista = next((item for item in listas if item['slug'] == slug), None)
    if lista is None:
        return 'Listado no encontrado', 404

    return render_template('lista.html', title=lista['nombre'], lista=lista)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
