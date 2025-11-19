# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Build the Mod (2 minutes)

```bash
cd /Users/yuchan/Desktop/java/MEKAPLUS
./gradlew build
```

**Output:** `build/libs/mekaplus_endgame-1.0.0.jar`

### Step 2: Test in Dev Environment (Optional)

```bash
./gradlew runClient
```

This launches Minecraft with your mod loaded for testing.

### Step 3: Install to Minecraft

1. Copy `build/libs/mekaplus_endgame-1.0.0.jar` to your mods folder
2. Ensure you have Mekanism 10.4+ and Create 0.5.1+ installed
3. Launch Minecraft 1.20.1 with Forge

---

## 📦 What You Get

### 6 New Items:
1. **Radiance-Shadow Amalgam** (Rare) - Stack 16
2. **Infinite Energy Matrix** (Epic) - Stack 16
3. **Antimatter Stabilization Matrix** (Rare) - Stack 16
4. **Dimensional Fusion Core** (Epic) - Stack 8
5. **Temporal Catalyst** (Epic) - Stack 4
6. **Temporal Alloy Ingot** (Epic) - Stack 8

All items are **fire-resistant**!

### 6-Stage Recipe Chain:
```
Stage 1: Create Mixing → Radiance-Shadow Amalgam
Stage 2: Mekanism Infusing → Infinite Energy Matrix
Stage 3: Mekanism Combiner → Antimatter Stabilization Matrix
Stage 4: Create Mechanical Crafting → Dimensional Fusion Core
Stage 5: Mekanism Reaction → Temporal Catalyst
Stage 6: Create Sequenced Assembly → Temporal Alloy Ingot
```

See `docs/RECIPE_GUIDE.md` for detailed recipes and flowchart.

---

## ⚡ Quick Commands

### Build Commands
```bash
./gradlew build              # Build the mod
./gradlew clean build        # Clean build (recommended for releases)
./gradlew runClient          # Test in Minecraft
```

### Give Commands (Creative/Testing)
```
/give @p mekaplus_endgame:temporal_alloy_ingot
/give @p mekaplus_endgame:infinite_energy_matrix
/give @p mekaplus_endgame:radiance_shadow_amalgam
/give @p mekaplus_endgame:antimatter_stabilization_matrix
/give @p mekaplus_endgame:dimensional_fusion_core
/give @p mekaplus_endgame:temporal_catalyst
```

---

## 🎨 Adding Textures (Optional)

Create 16x16 PNG images and place them here:
```
src/main/resources/assets/mekaplus_endgame/textures/item/
```

Required files:
- `temporal_alloy_ingot.png`
- `infinite_energy_matrix.png`
- `radiance_shadow_amalgam.png`
- `antimatter_stabilization_matrix.png`
- `dimensional_fusion_core.png`
- `temporal_catalyst.png`

**Note:** Mod works without textures, but items will show missing texture pattern.

See `src/main/resources/assets/mekaplus_endgame/textures/item/README.md` for design suggestions.

---

## 🔧 Requirements

### For Building:
- Java 17
- Internet connection (first build only)

### For Running:
- Minecraft 1.20.1
- Forge 47.2.0+
- Mekanism 10.4+ (with Additions, Generators, Tools)
- Create 0.5.1+

---

## 📚 Documentation

- **README.md** - Full project overview
- **PROJECT_SUMMARY.md** - Complete file listing and details
- **BUILDING.md** - Detailed build instructions and troubleshooting
- **docs/RECIPE_GUIDE.md** - Recipe flowchart and resource calculator
- **CHECKLIST.md** - Completion status and testing checklist

---

## ❓ Troubleshooting

### Build fails with "Java version mismatch"
**Fix:** Install Java 17 and set it as JAVA_HOME

### "Could not find mekanism:Mekanism"
**Fix:** Check internet connection and retry: `./gradlew build --refresh-dependencies`

### Items show purple/black checkerboard in-game
**This is normal** - it means textures haven't been added yet. The mod still works!

### Recipes don't appear in JEI/REI
**Fix:** Ensure Mekanism and Create are installed. Use `/reload` to reload recipes.

---

## 🎯 What to Do Next

1. **Build the mod** - `./gradlew build`
2. **Test recipes** - Use `./gradlew runClient` or install to Minecraft
3. **Create textures** - Design 16x16 PNG files for each item
4. **Share your creation** - Upload to CurseForge or Modrinth!

---

## 🆘 Need Help?

Check these files in order:
1. This file (QUICKSTART.md) - You are here
2. BUILDING.md - Build issues
3. CHECKLIST.md - Verify everything is set up
4. docs/RECIPE_GUIDE.md - Recipe details
5. README.md - Full documentation

---

**Ready?** Run `./gradlew build` and you're good to go! 🎉
