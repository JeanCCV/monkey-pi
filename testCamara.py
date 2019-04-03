from camara import ColorTracker

tracker = ColorTracker(debug=True)

Ubicacion = tracker.FindColor("rojo")

print("El objeto rojo esta en: {0}".format(Ubicacion))