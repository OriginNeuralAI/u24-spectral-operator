#!/usr/bin/env python3
"""
Generate the 24-cell polytope projection SVG for the repository hero image.

The 24-cell is a regular 4-polytope with:
  - 24 vertices (unit quaternions)
  - 96 edges (connecting vertices at distance sqrt(2))

Output: assets/hero-24cell.svg (1440x480, navy background, gold vertices)

No dependencies required (pure Python + math).
"""

import math
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT = os.path.join(REPO_DIR, "assets", "hero-24cell.svg")

WIDTH, HEIGHT = 1440, 480
BG = "#0A2540"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"

# 24-cell vertices: 8 permutations of (+-1,0,0,0) + 16 of (+-1/2,+-1/2,+-1/2,+-1/2)
def get_vertices():
    verts = []
    # 8 axis-aligned vertices
    for axis in range(4):
        for sign in [1, -1]:
            v = [0.0, 0.0, 0.0, 0.0]
            v[axis] = sign
            verts.append(tuple(v))
    # 16 half-integer vertices
    for s0 in [0.5, -0.5]:
        for s1 in [0.5, -0.5]:
            for s2 in [0.5, -0.5]:
                for s3 in [0.5, -0.5]:
                    verts.append((s0, s1, s2, s3))
    return verts


def dist4(a, b):
    return math.sqrt(sum((ai - bi)**2 for ai, bi in zip(a, b)))


def get_edges(verts):
    edges = []
    n = len(verts)
    for i in range(n):
        for j in range(i+1, n):
            d = dist4(verts[i], verts[j])
            if abs(d - 1.0) < 0.01:
                edges.append((i, j))
    return edges


def rotate_4d(v, angle1=0.4, angle2=0.25):
    """Apply two 4D rotations for an interesting projection angle."""
    x, y, z, w = v
    # XW rotation
    c, s = math.cos(angle1), math.sin(angle1)
    x, w = c*x - s*w, s*x + c*w
    # YZ rotation
    c, s = math.cos(angle2), math.sin(angle2)
    y, z = c*y - s*z, s*y + c*z
    return (x, y, z, w)


def project_to_2d(v):
    """Orthographic projection from 4D to 2D (drop z, w)."""
    return (v[0], v[1])


def generate_svg():
    verts = get_vertices()
    edges = get_edges(verts)

    # Apply 4D rotation
    rotated = [rotate_4d(v) for v in verts]
    projected = [project_to_2d(v) for v in rotated]

    # Scale to SVG coordinates
    cx, cy = WIDTH / 2, HEIGHT / 2
    scale = 160

    pts = [(cx + p[0] * scale, cy + p[1] * scale) for p in projected]

    # Depth (z-coordinate) for opacity modulation
    depths = [rotated[i][2] for i in range(len(rotated))]
    min_d, max_d = min(depths), max(depths)

    # GUE pair correlation waveform R2(r) = 1 - (sin(pi*r)/(pi*r))^2
    wave_points = []
    for px in range(100, WIDTH - 100):
        r = (px - 100) / (WIDTH - 200) * 3.0 + 0.01
        sinc = math.sin(math.pi * r) / (math.pi * r)
        R2 = 1 - sinc * sinc
        wy = cy + 60 - R2 * 120
        wave_points.append(f"{px},{wy:.1f}")
    wave_path = " ".join(wave_points)

    # Select "highlight" edges — those closest to front
    avg_depths = []
    for i, j in edges:
        avg_z = (depths[i] + depths[j]) / 2
        avg_depths.append(avg_z)
    depth_threshold = sorted(avg_depths, reverse=True)[min(20, len(avg_depths)-1)]

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">')
    svg_lines.append(f'  <defs>')
    svg_lines.append(f'    <filter id="glow">')
    svg_lines.append(f'      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>')
    svg_lines.append(f'      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    svg_lines.append(f'    </filter>')
    svg_lines.append(f'  </defs>')
    svg_lines.append(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>')

    # Spectral waveform
    svg_lines.append(f'  <polyline points="{wave_path}" fill="none" stroke="{GOLD}" stroke-width="1.5" opacity="0.25"/>')

    # Edges
    for idx, (i, j) in enumerate(edges):
        x1, y1 = pts[i]
        x2, y2 = pts[j]
        if avg_depths[idx] >= depth_threshold:
            svg_lines.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GOLD}" stroke-width="0.8" opacity="0.5"/>')
        else:
            svg_lines.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{WHITE}" stroke-width="0.5" opacity="0.15"/>')

    # Vertices (gold dots with glow)
    for i, (x, y) in enumerate(pts):
        depth_frac = (depths[i] - min_d) / (max_d - min_d + 0.001)
        r = 2.5 + depth_frac * 3
        opacity = 0.4 + depth_frac * 0.6
        svg_lines.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{GOLD}" opacity="{opacity:.2f}" filter="url(#glow)"/>')

    # Title
    svg_lines.append(f'  <text x="{WIDTH/2}" y="70" text-anchor="middle" font-family="Georgia, serif" font-size="56" fill="{WHITE}" font-weight="bold">U\u2082\u2084</text>')
    svg_lines.append(f'  <text x="{WIDTH/2}" y="110" text-anchor="middle" font-family="Georgia, serif" font-size="24" fill="{GOLD}">Spectral Operator</text>')

    svg_lines.append('</svg>')

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))

    print(f"Generated: {OUTPUT}")
    print(f"  24 vertices, {len(edges)} edges")


if __name__ == "__main__":
    generate_svg()
