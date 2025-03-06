import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_bike():
    fig, ax = plt.subplots()
    
    # Set equal aspect ratio for consistent proportions
    ax.set_aspect('equal')
    
    # Remove axes for a clean minimalist look
    ax.axis('off')
    
    # Main body (rectangular frame) - thinner, slightly tilted rectangle
    # Bottom-left at (0.3, 0.25), width 0.4, height 0.1, slight 10° tilt
    frame = patches.Rectangle((0.3, 0.25), 0.4, 0.1, angle=10, edgecolor='black', facecolor='none', linewidth=1.5)
    ax.add_patch(frame)
    
    # Wheels (two circles attached to the frame)
    # Front wheel: center at (0.7, 0.25), radius 0.15, touches frame's front bottom
    front_wheel = patches.Circle((0.7, 0.25), 0.15, edgecolor='black', facecolor='none', linewidth=1.5)
    # Rear wheel: center at (0.3, 0.25), radius 0.15, touches frame's rear bottom
    rear_wheel = patches.Circle((0.3, 0.25), 0.15, edgecolor='black', facecolor='none', linewidth=1.5)
    ax.add_patch(front_wheel)
    ax.add_patch(rear_wheel)
    
    # Seat (small rectangle attached to frame)
    # Bottom-left at (0.45, 0.4), above frame
    seat = patches.Rectangle((0.45, 0.4), 0.1, 0.03, edgecolor='black', facecolor='none', linewidth=1.5)
    ax.add_patch(seat)
    
    # Handlebars (short line attached to front of frame)
    # Horizontal line from (0.7, 0.45) to (0.8, 0.45)
    handlebars = patches.Polygon([(0.7, 0.45), (0.8, 0.45)], closed=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(handlebars)
    
    # Connecting line for cohesion
    # Seat support: line from frame (0.5, 0.35) to seat bottom (0.5, 0.4)
    seat_support = patches.Polygon([(0.5, 0.35), (0.5, 0.4)], closed=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(seat_support)
    
    # Set plot limits to frame the bike nicely
    ax.set_xlim(0.1, 0.9)
    ax.set_ylim(0.05, 0.55)
    
    # Display the plot
    plt.show()
    
    return fig

# Generate and display the bike illustration
bike_figure = draw_bike()
