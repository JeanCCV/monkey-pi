from camara import ColorTracker

tracker = ColorTracker(debug=False)

UbicacionRojo = tracker.FindColor("rojo")

print("*** El objeto rojo esta en: {0}".format(UbicacionRojo))

if (UbicacionRojo[0] > 320):
    print("*** Rojo esta a la izquierda: {0}".format(UbicacionRojo[0]))
else:
    print("*** Rojo esta a la derecha: {0}".format(UbicacionRojo[0]))


# UbicacionAzul = tracker.FindColor("azul")
# print("*** El objeto azul esta en: {0}".format(UbicacionAzul))