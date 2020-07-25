"""
POrque graficar?

Reconocimiento de patrones
Prediccion de una serie
Simplicar la interpretacion y las conclusiones acerca de los datos

Bokeh permite graficas complejas de manea rapida y con comnados simples.
Permite exportar a varios formato como html, notebooks, imagenes, etc.
Bokeh se puede utilizar en el servidor con Flask y Django.

docs.bokeh.org
"""
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('Graficar.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)