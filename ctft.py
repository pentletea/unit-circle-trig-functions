import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.patches as patches

fig = plt.figure(figsize=(18, 8))
fig.subplots_adjust(bottom=0.2)
fig.suptitle('Círculo e Funções Trigonométricas', fontsize=16, fontweight='bold')

ax_circle = plt.subplot(1, 3, 1)
ax_sine = plt.subplot(1, 3, 2)
ax_cosine = plt.subplot(1, 3, 3)

ax_circle.set_xlim(-1.5, 1.5)
ax_circle.set_ylim(-1.5, 1.5)
ax_circle.set_aspect('equal')
ax_circle.grid(True, alpha=0.3, linestyle='--')
ax_circle.set_title('Círculo Trigonométrico\n(cos θ, sen θ)', fontsize=12, fontweight='bold')
ax_circle.set_xlabel('cos θ')
ax_circle.set_ylabel('sen θ')
ax_circle.axhline(y=0, color='black', linewidth=0.5, zorder=1)
ax_circle.axvline(x=0, color='black', linewidth=0.5, zorder=1)

circle = patches.Circle((0, 0), 1, fill=False, color='blue', linewidth=2, 
                        linestyle='-', alpha=0.7, zorder=2)
ax_circle.add_patch(circle)

x_range = np.linspace(0, 2*np.pi, 1000)
sine_line, = ax_sine.plot([], [], color='red', linewidth=2, label='y = sen θ', zorder=3)
sine_marker, = ax_sine.plot([], [], 'ro', markersize=8, zorder=4)
ax_sine.set_xlim(0, 2*np.pi)
ax_sine.set_ylim(-1.2, 1.2)
ax_sine.grid(True, alpha=0.3, linestyle='--', zorder=1)
ax_sine.set_title('Função Seno', fontsize=12, fontweight='bold')
ax_sine.set_xlabel('θ (radianos)')
ax_sine.set_ylabel('sen θ')
ax_sine.legend(loc='upper right')
ax_sine.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax_sine.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

ax_sine.axhline(y=0, color='black', linewidth=0.5, zorder=2)

cosine_line, = ax_cosine.plot([], [], color='green', linewidth=2, label='y = cos θ', zorder=3)
cosine_marker, = ax_cosine.plot([], [], 'go', markersize=8, zorder=4)
ax_cosine.set_xlim(0, 2*np.pi)
ax_cosine.set_ylim(-1.2, 1.2)
ax_cosine.grid(True, alpha=0.3, linestyle='--', zorder=1)
ax_cosine.set_title('Função Cosseno', fontsize=12, fontweight='bold')
ax_cosine.set_xlabel('θ (radianos)')
ax_cosine.set_ylabel('cos θ')
ax_cosine.legend(loc='upper right')
ax_cosine.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax_cosine.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

ax_cosine.axhline(y=0, color='black', linewidth=0.5, zorder=2)

point, = ax_circle.plot([], [], 'ro', markersize=10, zorder=4)
radius_line, = ax_circle.plot([], [], 'r-', linewidth=1.5, alpha=0.6, zorder=3)
h_proj, = ax_circle.plot([], [], 'g--', alpha=0.5, linewidth=1, zorder=2)
v_proj, = ax_circle.plot([], [], 'r--', alpha=0.5, linewidth=1, zorder=2)
h_proj_point, = ax_circle.plot([], [], 'go', markersize=6, zorder=3)
v_proj_point, = ax_circle.plot([], [], 'ro', markersize=6, zorder=3)

angle_arc = patches.Arc((0, 0), 0.8, 0.8, angle=0, theta1=0, theta2=0, 
                        color='purple', linewidth=2, alpha=0.8, zorder=3)
ax_circle.add_patch(angle_arc)
angle_text = ax_circle.text(0, 0, '', fontsize=9, fontweight='bold',
                           bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', alpha=0.8),
                           zorder=5)

sine_vline = ax_sine.axvline(x=0, color='red', linestyle='--', alpha=0.7, linewidth=1.5, zorder=5)
cosine_vline = ax_cosine.axvline(x=0, color='green', linestyle='--', alpha=0.7, linewidth=1.5, zorder=5)

value_text = ax_circle.text(-1.4, -1.4, '', fontsize=9,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9),
                           zorder=5)

ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
angle_slider = Slider(
    ax=ax_slider,
    label='Ângulo θ (graus)',
    valmin=0,
    valmax=360,
    valinit=0,
    valstep=1,
    color='purple'
)

ax_angle_display = plt.axes([0.2, 0.01, 0.6, 0.03])
ax_angle_display.axis('off')
angle_display_text = ax_angle_display.text(0.5, 0.5, '', 
                                           transform=ax_angle_display.transAxes,
                                           ha='center', va='center',
                                           fontsize=10, fontweight='bold')

def update(val):
    
    theta_deg = angle_slider.val
    theta_rad = theta_deg * np.pi / 180

    x = np.cos(theta_rad)
    y = np.sin(theta_rad)

    point.set_data([x], [y])
    radius_line.set_data([0, x], [0, y])
    h_proj.set_data([x, x], [0, y])
    v_proj.set_data([0, x], [y, y])
    h_proj_point.set_data([x], [0])
    v_proj_point.set_data([0], [y])

    angle_arc.theta2 = theta_deg
    angle_text.set_text(f'{theta_deg:.0f}°')
    angle_text.set_position((0.6 * x, 0.6 * y))

    value_text.set_text(f'θ = {theta_deg:.0f}° = {theta_rad:.3f} rad\n'
                        f'cos = {x:.3f}\nsen = {y:.3f}')

    x_sine = np.linspace(0, theta_rad, max(2, int(theta_rad * 100) + 1))
    y_sine = np.sin(x_sine)
    sine_line.set_data(x_sine, y_sine)
    sine_marker.set_data([theta_rad], [np.sin(theta_rad)])
    sine_vline.set_xdata([theta_rad, theta_rad])

    x_cosine = np.linspace(0, theta_rad, max(2, int(theta_rad * 100) + 1))
    y_cosine = np.cos(x_cosine)
    cosine_line.set_data(x_cosine, y_cosine)
    cosine_marker.set_data([theta_rad], [np.cos(theta_rad)])
    cosine_vline.set_xdata([theta_rad, theta_rad])

    angle_display_text.set_text(f'Ângulo: {theta_deg:.0f}° ({theta_rad:.3f} rad)')

    fig.canvas.draw_idle()

angle_slider.on_changed(update)

update(0)

fig.subplots_adjust(bottom=0.18, left=0.05, right=0.95, top=0.92)

plt.show()