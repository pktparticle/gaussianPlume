import matplotlib.pyplot as plt
import numpy as np
from gaussian_plume_model import x,y,C1

def overlay_on_map():
    import scipy.io as sio

    # Overlay concentrations on map
    plt.ion()
    mat_contents = sio.loadmat('map_green_lane')
    plt.figure()
    plt.imshow(mat_contents['A'], \
       extent=[np.min(mat_contents['ximage']), \
               np.max(mat_contents['ximage']), \
               np.min(mat_contents['yimage']), \
               np.max(mat_contents['yimage'])])
               
    plt.xlabel('x (m)') 
    plt.ylabel('y (m)') 
    cs=plt.contour(x,y,np.mean(C1,axis=2)*1e6, cmap='hot')
    plt.clabel(cs,cs.levels,inline=True, fmt='%.1f',fontsize=5)

    plt.show(block=False)
    plt.pause(0)
    plt.close()

    return
    
if __name__ == "__main__":
    overlay_on_map()
