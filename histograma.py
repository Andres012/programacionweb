import json
#graficas
import matplotlib.pyplot as plt

from matplotlib import pyplot

archivo=open("histograms.txt","r")

contenido=archivo.read()

#print contenido

histograma=json.loads(contenido)

#print histograma["histograms"]["v_error"]["ys"]

v_error=histograma ["histograms"]["v_error"]
t_error=histograma["histograms"]["t_error"]

plt.plot (v_error["xs"], v_error["ys"])
plt.plot (t_error["xs"], t_error["ys"])


pyplot.title("Representacion de histograma de errores")
plt.xlabel("iteraciones")
plt.ylabel("Valor del error")
plt.legend(["Error de validacion","Error de entrenamiento"])

plt.show()
