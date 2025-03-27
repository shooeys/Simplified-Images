import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_minimalist_bike():
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Define the bike's parts using geometric shapes
    # Main body (rectangular frame)
    frame = patches.Rectangle((0.3, 0.25), 0.4, 0.1, angle=10, edgecolor='black', facecolor='none', linewidth=1.5)
    # Front wheel
    front_wheel = patches.Circle((0.7, 0.25), 0.15, edgecolor='black', facecolor='none', linewidth=1.5)
    # Rear wheel
    rear_wheel = patches.Circle((0.3, 0.25), 0.15, edgecolor='black', facecolor='none', linewidth=1.5)
    # Seat
    seat = patches.Rectangle((0.45, 0.4), 0.1, 0.03, edgecolor='black', facecolor='none', linewidth=1.5)
    # Handlebars
    handlebars = patches.Polygon([(0.7, 0.45), (0.8, 0.45)], closed=False, edgecolor='black', linewidth=1.5)
    # Seat support
    seat_support = patches.Polygon([(0.5, 0.35), (0.5, 0.4)], closed=False, edgecolor='black', linewidth=1.5)
    
    # Add parts to the plot
    ax.add_patch(frame)
    ax.add_patch(front_wheel)
    ax.add_patch(rear_wheel)
    ax.add_patch(seat)
    ax.add_patch(handlebars)
    ax.add_patch(seat_support)
    
    # Set limits and aspect
    ax.set_xlim(0.1, 0.9)
    ax.set_ylim(0.05, 0.55)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis
    
    plt.show()
    return fig

# Generate and display the bike
figure = draw_bike()
