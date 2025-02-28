import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_minimalist_dog():
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Define the dog's body parts using geometric shapes
    # Rectangular body
    body = patches.Rectangle((0.3, 0.3), 0.4, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    # Circular head
    head = patches.Circle((0.15, 0.4), 0.1, edgecolor='black', facecolor='none', linewidth=2)
    # Four rectangular legs
    leg1 = patches.Rectangle((0.35, 0.1), 0.05, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    leg2 = patches.Rectangle((0.45, 0.1), 0.05, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    leg3 = patches.Rectangle((0.55, 0.1), 0.05, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    leg4 = patches.Rectangle((0.65, 0.1), 0.05, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    # Tail
    tail = patches.Rectangle((0.7, 0.4), 0.1, 0.05, edgecolor='black', facecolor='none', linewidth=2)
    
    # Add body parts to the plot
    ax.add_patch(body)
    ax.add_patch(head)
    ax.add_patch(leg1)
    ax.add_patch(leg2)
    ax.add_patch(leg3)
    ax.add_patch(leg4)
    ax.add_patch(tail)
    
    # Set limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis
    
    plt.show()
    return fig

# Generate and display the minimalist dog
figure = draw_minimalist_dog()
