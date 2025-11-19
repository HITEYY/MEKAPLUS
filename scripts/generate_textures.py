#!/usr/bin/env python3
"""
MEKAPLUS Endgame Materials - Texture Generator
Generates 16x16 pixel textures for all 6 items using PIL
"""

from PIL import Image, ImageDraw
import os

# Output directory
OUTPUT_DIR = "../src/main/resources/assets/mekaplus_endgame/textures/item"

def create_temporal_alloy_ingot():
    """Epic rarity ingot with temporal/time-based theme - Purple/Blue with clock patterns"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Ingot shape with gradient
    colors = [
        (80, 60, 140, 255),   # Dark purple
        (100, 80, 180, 255),  # Medium purple
        (120, 100, 220, 255), # Light purple
        (140, 160, 255, 255), # Blue highlight
    ]
    
    # Main ingot body
    ingot_shape = [
        (4, 2), (11, 2), (13, 4), (13, 13), (11, 15), (4, 15), (2, 13), (2, 4)
    ]
    draw.polygon(ingot_shape, fill=colors[1])
    
    # Highlights
    draw.polygon([(4, 2), (11, 2), (12, 3), (5, 3)], fill=colors[3])
    draw.polygon([(11, 2), (13, 4), (12, 5), (11, 3)], fill=colors[2])
    
    # Shadows
    draw.polygon([(2, 13), (4, 15), (5, 14), (3, 12)], fill=colors[0])
    
    # Temporal clock pattern
    draw.point([(7, 7), (8, 7), (7, 8), (8, 8)], fill=(200, 220, 255, 255))
    draw.point([(8, 5), (8, 10), (6, 8), (10, 8)], fill=(160, 180, 255, 200))
    
    return img

def create_infinite_energy_matrix():
    """Epic rarity matrix with energy theme - Bright cyan/white with grid overlay"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Core glow
    core_color = (0, 255, 255, 255)  # Cyan
    glow_color = (100, 255, 255, 200)
    outer_glow = (50, 200, 255, 150)
    
    # Central core
    draw.rectangle([6, 6, 9, 9], fill=core_color)
    
    # Glow layers
    draw.rectangle([5, 5, 10, 10], outline=glow_color)
    draw.rectangle([4, 4, 11, 11], outline=outer_glow)
    draw.rectangle([3, 3, 12, 12], outline=(30, 150, 200, 100))
    
    # Grid pattern
    grid_color = (150, 255, 255, 180)
    for i in range(2, 14, 3):
        draw.line([(i, 2), (i, 13)], fill=grid_color)
        draw.line([(2, i), (13, i)], fill=grid_color)
    
    # Energy particles
    particles = [(2, 2), (13, 2), (2, 13), (13, 13), (7, 1), (1, 7), (14, 8), (8, 14)]
    for p in particles:
        draw.point([p], fill=(200, 255, 255, 255))
    
    return img

def create_radiance_shadow_amalgam():
    """Rare rarity - Half gold/yellow, half dark purple/black"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Split orb design
    # Light side (Radiance) - Gold/Yellow
    light_colors = [
        (255, 215, 0, 255),   # Gold
        (255, 235, 100, 255), # Light gold
        (255, 255, 200, 255), # Bright
    ]
    
    # Dark side (Shadow) - Purple/Black
    dark_colors = [
        (20, 0, 40, 255),     # Very dark purple
        (40, 10, 60, 255),    # Dark purple
        (60, 20, 80, 255),    # Medium dark
    ]
    
    # Draw circle shape
    center = (8, 8)
    
    # Left half (Radiance)
    for x in range(3, 8):
        for y in range(3, 13):
            dist = ((x - 7.5) ** 2 + (y - 8) ** 2) ** 0.5
            if dist < 5:
                if dist < 3:
                    img.putpixel((x, y), light_colors[2])
                elif dist < 4:
                    img.putpixel((x, y), light_colors[1])
                else:
                    img.putpixel((x, y), light_colors[0])
    
    # Right half (Shadow)
    for x in range(8, 13):
        for y in range(3, 13):
            dist = ((x - 8) ** 2 + (y - 8) ** 2) ** 0.5
            if dist < 5:
                if dist < 3:
                    img.putpixel((x, y), dark_colors[2])
                elif dist < 4:
                    img.putpixel((x, y), dark_colors[1])
                else:
                    img.putpixel((x, y), dark_colors[0])
    
    # Center line
    draw.line([(8, 3), (8, 13)], fill=(100, 50, 100, 255))
    
    # Sparkles
    draw.point([(5, 5), (6, 8), (5, 11)], fill=(255, 255, 255, 255))
    draw.point([(10, 5), (11, 8), (10, 11)], fill=(80, 40, 100, 255))
    
    return img

def create_antimatter_stabilization_matrix():
    """Rare rarity with antimatter/quantum theme - Dark with red/pink accents"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dark background matrix
    bg_color = (20, 10, 30, 255)
    draw.rectangle([2, 2, 13, 13], fill=bg_color)
    
    # Antimatter cores (red/pink)
    core_color = (255, 50, 100, 255)
    accent_color = (255, 100, 150, 255)
    
    # Four corner stabilizers
    corners = [(4, 4), (11, 4), (4, 11), (11, 11)]
    for corner in corners:
        draw.ellipse([corner[0]-1, corner[1]-1, corner[0]+1, corner[1]+1], fill=core_color)
        draw.point([corner], fill=accent_color)
    
    # Center core
    draw.rectangle([7, 7, 8, 8], fill=core_color)
    
    # Connecting lines
    line_color = (150, 50, 100, 200)
    draw.line([(4, 4), (11, 4)], fill=line_color)
    draw.line([(11, 4), (11, 11)], fill=line_color)
    draw.line([(11, 11), (4, 11)], fill=line_color)
    draw.line([(4, 11), (4, 4)], fill=line_color)
    
    # Diagonal stabilizers to center
    draw.line([(4, 4), (7, 7)], fill=line_color)
    draw.line([(11, 4), (8, 7)], fill=line_color)
    draw.line([(4, 11), (7, 8)], fill=line_color)
    draw.line([(11, 11), (8, 8)], fill=line_color)
    
    # Energy particles
    particles = [(2, 2), (13, 2), (2, 13), (13, 13), (7, 2), (2, 7), (13, 8), (8, 13)]
    for p in particles:
        draw.point([p], fill=(255, 80, 120, 200))
    
    # Border
    draw.rectangle([1, 1, 14, 14], outline=(100, 30, 60, 255))
    
    return img

def create_dimensional_fusion_core():
    """Epic rarity core with dimensional rifts - Multi-colored with portal-like swirls"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Multi-colored dimensional layers
    colors = [
        (150, 50, 200, 255),  # Purple
        (50, 150, 255, 255),  # Blue
        (50, 255, 150, 255),  # Cyan
        (255, 50, 150, 255),  # Magenta
    ]
    
    # Circular core with dimensional rifts
    center = (8, 8)
    
    # Outer ring
    for angle in range(0, 360, 10):
        import math
        x = int(center[0] + 5 * math.cos(math.radians(angle)))
        y = int(center[1] + 5 * math.sin(math.radians(angle)))
        color_idx = (angle // 90) % 4
        if 0 <= x < 16 and 0 <= y < 16:
            img.putpixel((x, y), colors[color_idx])
    
    # Middle rings
    for radius in [4, 3, 2]:
        for angle in range(0, 360, 15):
            import math
            x = int(center[0] + radius * math.cos(math.radians(angle)))
            y = int(center[1] + radius * math.sin(math.radians(angle)))
            color_idx = ((angle + radius * 30) // 90) % 4
            if 0 <= x < 16 and 0 <= y < 16:
                img.putpixel((x, y), colors[color_idx])
    
    # Bright center
    draw.rectangle([7, 7, 8, 8], fill=(255, 255, 255, 255))
    draw.rectangle([6, 6, 9, 9], outline=(200, 200, 255, 255))
    
    # Dimensional "tears" at cardinal points
    tears = [(8, 2), (8, 13), (2, 8), (13, 8)]
    for tear in tears:
        draw.line([(tear[0]-1, tear[1]), (tear[0]+1, tear[1])], fill=(255, 255, 255, 255))
        draw.line([(tear[0], tear[1]-1), (tear[0], tear[1]+1)], fill=(255, 255, 255, 255))
    
    return img

def create_temporal_catalyst():
    """Epic rarity catalyst with time-warp effects - Glowing purple with distortion"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Time-warped crystal shape
    colors = [
        (80, 40, 120, 255),   # Dark purple
        (120, 60, 180, 255),  # Medium purple
        (160, 100, 255, 255), # Bright purple
        (200, 150, 255, 255), # Very bright
        (255, 200, 255, 255), # Pink-purple glow
    ]
    
    # Crystal/catalyst shape (diamond-like)
    points = [
        (8, 2),   # Top
        (12, 8),  # Right
        (8, 14),  # Bottom
        (4, 8),   # Left
    ]
    
    # Main crystal body
    draw.polygon(points, fill=colors[2])
    
    # Top facet
    draw.polygon([(8, 2), (12, 8), (8, 8), (4, 8)], fill=colors[3])
    
    # Bottom facet
    draw.polygon([(4, 8), (8, 8), (12, 8), (8, 14)], fill=colors[1])
    
    # Left/right highlights
    draw.polygon([(4, 8), (8, 2), (8, 8)], fill=colors[4])
    draw.polygon([(12, 8), (8, 14), (8, 8)], fill=colors[0])
    
    # Temporal glow particles (time distortion)
    glow_points = [
        (6, 4), (10, 4), (6, 12), (10, 12),  # Corners
        (3, 8), (13, 8), (8, 1), (8, 15),     # Cardinal
        (5, 6), (11, 6), (5, 10), (11, 10),   # Diagonal
    ]
    
    for i, point in enumerate(glow_points):
        color = colors[3] if i % 2 == 0 else colors[4]
        if 0 <= point[0] < 16 and 0 <= point[1] < 16:
            draw.point([point], fill=color)
    
    # Center power core
    draw.point([(7, 8), (8, 8), (8, 7), (8, 9)], fill=(255, 255, 255, 255))
    
    return img

def save_textures():
    """Generate and save all textures"""
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    textures = {
        'temporal_alloy_ingot.png': create_temporal_alloy_ingot(),
        'infinite_energy_matrix.png': create_infinite_energy_matrix(),
        'radiance_shadow_amalgam.png': create_radiance_shadow_amalgam(),
        'antimatter_stabilization_matrix.png': create_antimatter_stabilization_matrix(),
        'dimensional_fusion_core.png': create_dimensional_fusion_core(),
        'temporal_catalyst.png': create_temporal_catalyst(),
    }
    
    print("🎨 Generating MEKAPLUS Endgame Materials Textures...\n")
    
    for filename, image in textures.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        image.save(filepath, 'PNG')
        print(f"✅ Created: {filename}")
    
    print(f"\n✨ All 6 textures generated successfully!")
    print(f"📁 Location: {OUTPUT_DIR}")
    print("\n🎮 You can now build the mod with textures!")

if __name__ == "__main__":
    save_textures()
