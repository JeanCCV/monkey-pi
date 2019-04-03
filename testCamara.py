from camara import ColorTracker

tracker = ColorTracker(debug=False)

UbicacionAzul = tracker.FindColor("azul")
print("*** El objeto azul esta en: {0}".format(UbicacionAzul))

UbicacionRojo = tracker.FindColor("rojo")
print("*** El objeto rojo esta en: {0}".format(UbicacionRojo))