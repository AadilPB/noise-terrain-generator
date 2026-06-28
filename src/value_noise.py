import numpy as np

def smoothstep(edge0, edge1, x):
    t = np.clip((x-edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def value_1D(x):
    i = int(np.floor(x))
    f = x - int(np.floor(x))
    a = np.random.rand()
    b = np.random.rand()
    y = a + (b - a) * smoothstep(0, 1, f)
    
    return y



def value_2D(pos):
    perm = np.arange(256)
    np.random.shuffle(perm)
    perm = np.concatenate([perm, perm])

    i = np.floor(pos).astype(int)
    f = pos - np.floor(pos)

    a = np.random.rand()
    b = np.random.rand()
    c = np.random.rand()
    d = np.random.rand()
   

    u = f * f * (3.0 - 2.0 * f)
    
    return (a + (b-a) * u[0]) + (c - a) * u[1] * (1.0 - u[0]) + (d-b) * u[1] * u[0]
