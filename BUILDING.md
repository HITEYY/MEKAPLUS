# Building Instructions

## Prerequisites

1. Java 21
   ```bash
   java -version
   ```
2. Gradle Wrapper (`gradlew`)

## Build

```bash
cd /Users/yuchan/Desktop/프로젝트/MEKAPLUS
./gradlew clean build
```

Build output:
- `build/libs/mekaplus-0.1.0.jar`

## Run In Development

Client:
```bash
./gradlew runClient
```

Server:
```bash
./gradlew runServer
```

## Resource Locations

- Item/block models and textures:
  - `src/main/resources/assets/mekaplus/`
- Recipes and loot:
  - `src/main/resources/data/mekaplus/`

## Install Built Mod

1. Build the project.
2. Copy `build/libs/mekaplus-0.1.0.jar` to your Minecraft `mods` folder.
3. Launch Minecraft 1.21.1 with Forge 52+.

Optional dependency mods:
- Mekanism 10.7+
- Create 6.0+
- Applied Energistics 2 (AE2) 19.0+
