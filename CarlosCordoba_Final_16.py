import numpy as np

def modelo(m,b,x):
    return m*x +b
def loglikeli(x_obs,y_obs,sigma,m,b):
    d=y_obs - modelo(m,b,x_obs)
    d=d/sigma
    d=-0.5*np.sum(d**2)
    return d
t_obs=np.array([73,28,59,52,39,137])
x_obs=np.array([4,10,12,80,50,40])
y_obs=np.array([100,5,80,50,50,200])
sigma=1.0;

#Calculamos el valor lineal para la posición en X
lista_m1 = [np.random.random()]
lista_b1 = [np.random.random()]

sigma_delta_m1 = 0.2
sigma_delta_b1 = 1.2

for i in range(1,10000):
    pm  = lista_m1[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_m1)
    pb  = lista_b1[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_b1)
    
    logposv = loglikeli(x_obs, t_obs, sigma, lista_m1[i-1], lista_b1[i-1])
    logposn = loglikeli(x_obs, t_obs, sigma, pm, pb)
    
    r=min(1,np.exp(logposn-logposv))
    a=np.random.random()
    if(a<r):
        lista_m1.append(pm)
        lista_b1.append(pb)
    else:
        lista_m1.append(lista_m1[i-1])
        lista_b1.append(lista_b1[i-1])
        
lista_m1=np.array(lista_m1)
lista_b1=np.array(lista_b1)

#Calculamos el valor lineal para la posición en Y
lista_m2 = [np.random.random()]
lista_b2 = [np.random.random()]

sigma_delta_m2 = 0.2
sigma_delta_b2 = 1.2

for i in range(1,10000):
    pm  = lista_m2[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_m2)
    pb  = lista_b2[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_b2)
    
    logposv = loglikeli(y_obs, t_obs, sigma, lista_m2[i-1], lista_b2[i-1])
    logposn = loglikeli(y_obs, t_obs, sigma, pm, pb)
    
    r=min(1,np.exp(logposn-logposv))
    a=np.random.random()
    if(a<r):
        lista_m2.append(pm)
        lista_b2.append(pb)
    else:
        lista_m2.append(lista_m2[i-1])
        lista_b2.append(lista_b2[i-1])
        
lista_m2=np.array(lista_m2)
lista_b2=np.array(lista_b2)

b1=np.mean(lista_b1)
m1=np.mean(lista_m1)
b2=np.mean(lista_b2)
m2=np.mean(lista_m2)
cb1=np.sqrt(np.var(lista_b1))
cb2=np.sqrt(np.var(lista_b2))
ct=cb2/np.sqrt(np.var(lista_m2))
cv=np.sqrt(np.sqrt(np.var(lista_m1))**2 + np.sqrt(np.var(lista_m2))**2)
print("Coordenada x: " + str(b1) +" +/- " + str(cb1))
print("Coordenada y: " + str(b2) +" +/- " + str(cb2))
print("Tiempo lanzamiento: " + str(b2/m2) +" +/- " + str(ct))
print("Velocidad del Sonido: " + str(np.sqrt(m1**2 + m2**2)) +" +/- " + str(cv))