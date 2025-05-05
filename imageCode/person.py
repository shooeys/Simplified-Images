import matplotlib.pyplot as plt

def draw_minimalist_person():
    fig, ax = plt.subplots()
    
    # Draw the body
    body = plt.Rectangle((0.4, 0.4), 0.2, 0.4, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(body)
    
    # Draw the head
    head = plt.Circle((0.5, 0.85), 0.1, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(head)
    
    # Draw the arms
    arm1 = plt.Rectangle((0.2, 0.6), 0.2, 0.05, edgecolor='black', facecolor='none', linewidth=2)
    arm2 = plt.Rectangle((0.6, 0.6), 0.2, 0.05, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(arm1)
    ax.add_patch(arm2)
    
    # Draw the legs
    leg1 = plt.Rectangle((0.4, 0.2), 0.05, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    leg2 = plt.Rectangle((0.55, 0.2), 0.05, 0.2, edgecolor='black', facecolor='none', linewidth=2)
    ax.add_patch(leg1)
    ax.add_patch(leg2)
    
    # Set limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis
    
    plt.show()
    return fig

# Generate and show the adjusted minimalist person illustration
figure_person_adjusted = draw_minimalist_person()
