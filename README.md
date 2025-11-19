# MEKAPLUS Endgame Materials

A Minecraft 1.20.1 Forge mod that adds 6 endgame materials with complex multi-stage crafting chains using Mekanism and Create.

## Features

### Items Added (6 Total)

1. **Temporal Alloy Ingot** - Epic rarity, max stack 8
2. **Infinite Energy Matrix** - Epic rarity, max stack 16
3. **Radiance-Shadow Amalgam** - Rare rarity, max stack 16
4. **Antimatter Stabilization Matrix** - Rare rarity, max stack 16
5. **Dimensional Fusion Core** - Epic rarity, max stack 8
6. **Temporal Catalyst** - Epic rarity, max stack 4

All items are fire-resistant and have custom crafting chains.

## Crafting Chain

### Stage 1: Radiance-Shadow Amalgam
**Machine:** Create Mixing (Superheated)
- Refined Radiance + Shadow Steel + Netherite Ingot + Dragon Breath
- **Output:** 2x Radiance-Shadow Amalgam

### Stage 2: Infinite Energy Matrix
**Machine:** Mekanism Metallurgic Infusing
- Infinity Alloy + 2000mB Antimatter Gas
- **Output:** 1x Infinite Energy Matrix

### Stage 3: Antimatter Stabilization Matrix
**Machine:** Mekanism Combiner
- Radiance-Shadow Amalgam + Infinite Energy Matrix
- **Output:** 2x Antimatter Stabilization Matrix

### Stage 4: Dimensional Fusion Core
**Machine:** Create Mechanical Crafting (6x5 pattern)
- Pattern uses: 6x Infinity Alloy, 6x Refined Radiance, 6x Shadow Steel, 4x Antimatter Matrix, 1x Nether Star
- **Output:** 1x Dimensional Fusion Core

### Stage 5: Temporal Catalyst
**Machine:** Mekanism Reaction Chamber
- Dimensional Fusion Core + 1000mB Heavy Water + 5000mB Antimatter + 100k FE
- Duration: 600 ticks (30 seconds)
- **Output:** 1x Temporal Catalyst + 100mB Spent Nuclear Waste

### Stage 6: Temporal Alloy Ingot
**Machine:** Create Sequenced Assembly (8 loops)
- Base: Temporal Catalyst
- Sequence: Deploy Refined Radiance → Deploy Shadow Steel → Deploy Infinity Alloy → Press
- **Output:** 1x Temporal Alloy Ingot

## Requirements

- Minecraft 1.20.1
- Forge 47.2.0+
- Mekanism 10.4+
- Create 0.5.1+

## Installation

1. Install Forge 1.20.1
2. Install Mekanism and Create mods
3. Download and place this mod in your `mods` folder
4. Launch the game

## Building from Source

```bash
./gradlew build
```

The built JAR will be in `build/libs/`.

## Development

### Structure
- `src/main/java/com/mekaplus/endgame/` - Java source code
- `src/main/resources/assets/mekaplus_endgame/` - Assets (textures, models, lang files)
- `src/main/resources/data/mekaplus_endgame/` - Data files (recipes)

### Textures ✅
All 6 textures are included! Generated using Python PIL.

To regenerate textures:
```bash
cd scripts
python3 generate_textures.py
```

See `TEXTURES_COMPLETE.md` for details.

## License

MIT License

## Credits

Created for modpack integration and endgame progression.
