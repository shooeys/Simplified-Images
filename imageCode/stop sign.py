import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

def draw_minimalist_stop_sign():
    fig, ax = plt.subplots()
    
    # Draw the stop sign (octagon)
    stop_sign = RegularPolygon((0.5, 0.6), numVertices=8, radius=0.2, 
                               orientation=np.pi/8, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(stop_sign)
    
    # Draw the sign pole
    pole = plt.Rectangle((0.48, 0.1), 0.04, 0.5, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(pole)
    
    # Set limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis
    
    plt.show()
    return fig

# Generate and show the minimalist stop sign illustration
figure_stop_sign = draw_minimalist_stop_sign()
