import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_minimalist_boat():
    # Create a new figure
    fig, ax = plt.subplots()

    # Hull (rectangle)
    hull = patches.Rectangle((0.35, 0.1), 0.3, 0.08, edgecolor='black', facecolor='none', linewidth=1.5)

    # Mast (vertical line), starting on top of hull and going upward
    mast = patches.Polygon([(0.5, 0.18), (0.5, 0.45)], closed=False, edgecolor='black', linewidth=1.5)

    # Sail (right triangle), floating above the hull, not touching it
    sail = patches.Polygon([
        (0.5, 0.45),  # top of mast
        (0.5, 0.25),  # bottom of sail (above hull)
        (0.62, 0.35)  # outer edge of sail
    ], closed=True, edgecolor='black', facecolor='none', linewidth=1.5)

    # Add parts to the plot
    ax.add_patch(hull)
    ax.add_patch(mast)
    ax.add_patch(sail)

    # Set limits and aspect
    ax.set_xlim(0.2, 0.8)
    ax.set_ylim(0.05, 0.55)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis

    plt.show()
    return fig

# Generate and display the boat
figure = draw_minimalist_boat()
