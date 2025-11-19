# Building Instructions

## Prerequisites

1. **Java 17** - Required for Minecraft 1.20.1
   ```bash
   java -version  # Should show version 17
   ```

2. **Gradle** - Included via Gradle Wrapper (gradlew)

## First Time Setup

### Option 1: Using IntelliJ IDEA (Recommended)
1. Open IntelliJ IDEA
2. File → Open → Select the `MEKAPLUS` folder
3. Wait for Gradle to sync (this will download dependencies)
4. IntelliJ will automatically configure the project

### Option 2: Using Eclipse
1. Open Eclipse
2. File → Import → Gradle → Existing Gradle Project
3. Select the `MEKAPLUS` folder
4. Wait for Gradle to sync

### Option 3: Command Line Only
```bash
cd /Users/yuchan/Desktop/java/MEKAPLUS
./gradlew build --no-daemon
```

Note: On Windows, use `gradlew.bat` instead of `./gradlew`

## Building the Mod

### Quick Build
```bash
./gradlew build
```

The compiled JAR will be in: `build/libs/mekaplus_endgame-1.0.0.jar`

### Clean Build (Recommended for releases)
```bash
./gradlew clean build
```

## Testing in Development

### Launch Client
```bash
./gradlew runClient
```

This will:
- Start Minecraft with your mod loaded
- Create a `run` folder with the game files
- Allow you to test the mod in-game

### Launch Server
```bash
./gradlew runServer
```

### Generate Data (for datagen if needed)
```bash
./gradlew runData
```

## Common Issues

### Issue: "Could not find mekanism:Mekanism"
**Solution:** The Maven repository may be temporarily unavailable. Try again later or check your internet connection.

### Issue: "Java version mismatch"
**Solution:** Ensure Java 17 is installed and set as your JAVA_HOME:
```bash
export JAVA_HOME=/path/to/java17
```

### Issue: "Could not resolve dependencies"
**Solution:** Run with `--refresh-dependencies`:
```bash
./gradlew build --refresh-dependencies
```

### Issue: Gradle daemon issues
**Solution:** Stop all Gradle daemons:
```bash
./gradlew --stop
```

## Adding Textures Before Building

Before your first build, add 16x16 PNG textures to:
```
src/main/resources/assets/mekaplus_endgame/textures/item/
```

Required files:
- temporal_alloy_ingot.png
- infinite_energy_matrix.png
- radiance_shadow_amalgam.png
- antimatter_stabilization_matrix.png
- dimensional_fusion_core.png
- temporal_catalyst.png

The mod will build without textures, but items will appear as purple/black checkerboard patterns in-game.

## Installing Built Mod

1. Build the mod: `./gradlew build`
2. Locate JAR: `build/libs/mekaplus_endgame-1.0.0.jar`
3. Copy to Minecraft mods folder:
   - Windows: `%APPDATA%\.minecraft\mods\`
   - macOS: `~/Library/Application Support/minecraft/mods/`
   - Linux: `~/.minecraft/mods/`
4. Ensure you have:
   - Minecraft 1.20.1
   - Forge 47.2.0 or later
   - Mekanism 10.4+
   - Create 0.5.1+
5. Launch Minecraft

## Development Workflow

1. Make code changes
2. Test with `./gradlew runClient`
3. Fix any issues
4. Build release with `./gradlew clean build`
5. Test in actual Minecraft instance

## Gradle Tasks Reference

```bash
./gradlew tasks              # List all available tasks
./gradlew build              # Build the mod
./gradlew clean              # Clean build artifacts
./gradlew runClient          # Run Minecraft client
./gradlew runServer          # Run Minecraft server
./gradlew runData            # Run data generators
./gradlew idea               # Generate IntelliJ IDEA files
./gradlew eclipse            # Generate Eclipse files
./gradlew --refresh-dependencies  # Refresh all dependencies
./gradlew --stop             # Stop Gradle daemon
```

## Performance Tips

### Speed up builds
Add to `gradle.properties`:
```properties
org.gradle.jvmargs=-Xmx4G
org.gradle.parallel=true
org.gradle.caching=true
```

### Disable daemon for CI/CD
```bash
./gradlew build --no-daemon
```

## Troubleshooting Build Errors

### Check Gradle version
```bash
./gradlew --version
```

### View dependency tree
```bash
./gradlew dependencies
```

### Run with debug info
```bash
./gradlew build --debug
```

### Run with stack traces
```bash
./gradlew build --stacktrace
```

## Next Steps After Building

1. Test all 6 recipes in-game
2. Verify item tooltips show correct rarity colors
3. Test that items are fire-resistant (throw in lava)
4. Verify stack sizes are correct
5. Test with actual Mekanism and Create setups

Happy modding! 🎮
