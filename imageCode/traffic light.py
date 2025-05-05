import matplotlib.pyplot as plt

def draw_minimalist_traffic_light():
    fig, ax = plt.subplots()
    
    # Draw the stoplight pole
    pole = plt.Rectangle((0.45, 0.1), 0.1, 0.8, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(pole)
    
    # Draw the stoplight lights
    light_red = plt.Circle((0.5, 0.8), 0.05, edgecolor='black', facecolor='none', linewidth=2)
    light_yellow = plt.Circle((0.5, 0.6), 0.05, edgecolor='black', facecolor='none', linewidth=2)
    light_green = plt.Circle((0.5, 0.4), 0.05, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(light_red)
    ax.add_patch(light_yellow)
    ax.add_patch(light_green)
    
    # Set limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis
    
    plt.show()
    return fig

# Generate and show the minimalist stoplight illustration
figure_stoplight = draw_minimalist_stoplight()
