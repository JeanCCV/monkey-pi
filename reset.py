import pickle

'''
Reniciar pickle a valores de posicion inicial del dobot
'''
stepsForce = { "_baseSteps": 0, "_rearSteps": 0, "_frontSteps": 0}
pickle_out = open("steps.pickle","wb")
pickle.dump(stepsForce, pickle_out)
pickle_out.close()

'''
Verificar pickle creado
'''
# pickle_in = open("steps.pickle","rb")
# stepsPickle = pickle.load(pickle_in)
# print(stepsPickle)