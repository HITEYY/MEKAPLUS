# Recipe Guide - MEKAPLUS Endgame Materials

## Visual Recipe Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        CRAFTING CHAIN                            │
└─────────────────────────────────────────────────────────────────┘

STAGE 1: Create Mixing (Superheated)
┌────────────────────────────────────────┐
│ Refined Radiance                       │
│ Shadow Steel                           │
│ Netherite Ingot                        │
│ Dragon Breath                          │
└───────────────┬────────────────────────┘
                │
                ▼
    ┌───────────────────────────┐
    │ Radiance-Shadow Amalgam   │
    │        (x2)               │
    └───────────┬───────────────┘
                │
                │
STAGE 2: Mekanism Metallurgic Infusing  STAGE 3: Mekanism Combiner
┌────────────────────┐                  ┌─────────────────────────┐
│ Infinity Alloy     │                  │ Radiance-Shadow Amalgam │
│ Antimatter 2000mB  │                  │ Infinite Energy Matrix  │
└──────┬─────────────┘                  └────────┬────────────────┘
       │                                         │
       ▼                                         ▼
┌──────────────────────┐              ┌──────────────────────────┐
│ Infinite Energy      │──────────────│ Antimatter Stabilization │
│ Matrix (x1)          │              │ Matrix (x2)              │
└──────────────────────┘              └────────┬─────────────────┘
                                               │
                                               │
STAGE 4: Create Mechanical Crafting (6x5 grid)
┌─────────────────────────────────────────────────────┐
│  I  R  I  R  I  R    I = Infinity Alloy (6x)       │
│  R  A  S  A  S  R    R = Refined Radiance (6x)     │
│  I  S  A  N  S  I    S = Shadow Steel (6x)         │
│  R  A  S  A  S  R    A = Antimatter Matrix (4x)    │
│  I  R  I  R  I  R    N = Nether Star (1x)          │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
         ┌─────────────────────┐
         │ Dimensional Fusion  │
         │ Core (x1)           │
         └─────────┬───────────┘
                   │
                   │
STAGE 5: Mekanism Reaction Chamber
┌───────────────────────────────────────┐
│ Dimensional Fusion Core               │
│ Heavy Water 1000mB                    │
│ Antimatter 5000mB                     │
│ 100,000 FE                            │
│ Duration: 600 ticks (30 seconds)      │
└──────────────┬────────────────────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Temporal Catalyst    │
    │ (x1)                 │
    │ + Spent Nuclear      │
    │   Waste 100mB        │
    └──────────┬───────────┘
               │
               │
STAGE 6: Create Sequenced Assembly (8 loops)
┌────────────────────────────────────────┐
│ Base: Temporal Catalyst                │
│                                        │
│ Loop Sequence (repeat 8 times):        │
│  1. Deploy Refined Radiance            │
│  2. Deploy Shadow Steel                │
│  3. Deploy Infinity Alloy              │
│  4. Press                              │
└──────────────┬─────────────────────────┘
               │
               ▼
      ┌────────────────────┐
      │ Temporal Alloy     │
      │ Ingot (x1)         │
      └────────────────────┘
```

## Resource Requirements

### To craft 1x Temporal Alloy Ingot, you need:

#### Direct Requirements (Stage 6):
- 1x Temporal Catalyst
- 8x Refined Radiance (for sequencing)
- 8x Shadow Steel (for sequencing)
- 8x Infinity Alloy (for sequencing)

#### Tracing back through all stages:

**Stage 5 Requirements:**
- 1x Dimensional Fusion Core
- 1000mB Heavy Water
- 5000mB Antimatter
- 100,000 FE

**Stage 4 Requirements:**
- 6x Infinity Alloy
- 6x Refined Radiance
- 6x Shadow Steel
- 4x Antimatter Stabilization Matrix
- 1x Nether Star

**Stage 3 Requirements (for 4x Antimatter Matrix):**
- 2x Radiance-Shadow Amalgam
- 2x Infinite Energy Matrix

**Stage 2 Requirements (for 2x Infinite Energy Matrix):**
- 2x Infinity Alloy
- 4000mB Antimatter

**Stage 1 Requirements (for 2x Radiance-Shadow Amalgam):**
- 1x Refined Radiance
- 1x Shadow Steel
- 1x Netherite Ingot
- 1x Dragon Breath

### Total Materials Needed:

| Material | Quantity | Source |
|----------|----------|--------|
| Infinity Alloy | 16 | Mekanism |
| Refined Radiance | 15 | Create |
| Shadow Steel | 15 | Create |
| Netherite Ingot | 1 | Vanilla |
| Dragon Breath | 1 | Vanilla |
| Nether Star | 1 | Vanilla |
| Antimatter Gas | 9000mB | Mekanism |
| Heavy Water | 1000mB | Mekanism |
| Energy (FE) | 100,000 | Any mod |

## Machine Setup Required

1. **Create Mixer** - With Superheated heat source (Blaze Burner with Blaze Cake)
2. **Mekanism Metallurgic Infuser** - With Antimatter supply
3. **Mekanism Combiner** - Basic setup
4. **Create Mechanical Crafter** - 6x5 grid (30 crafters minimum)
5. **Mekanism Pressurized Reaction Chamber** - With power, fluid, and gas inputs
6. **Create Sequenced Assembly** - Deployers and Mechanical Press

## Recipe Tips

### Efficiency Notes:
- **Batch Stage 1**: Each run gives 2x Radiance-Shadow Amalgam, so run it multiple times
- **Bottleneck**: Infinity Alloy is needed in large quantities (16 total)
- **Energy**: The Reaction Chamber needs 100k FE - ensure adequate power generation
- **Automation**: All stages can be fully automated with proper setup

### Recommended Progression:
1. Set up automated Infinity Alloy production (Mekanism)
2. Build Refined Radiance and Shadow Steel farms (Create)
3. Stockpile Antimatter and Heavy Water (Mekanism)
4. Set up the 6x5 Mechanical Crafter grid
5. Build the Sequenced Assembly line
6. Run the full production chain

### Common Mistakes:
- ❌ Not superheating the mixer for Stage 1
- ❌ Insufficient Antimatter storage (need 9000mB total)
- ❌ Wrong pattern in Mechanical Crafter (it's 6x5, not square)
- ❌ Not enough loops in Sequenced Assembly (must be exactly 8)
- ❌ Forgetting to supply power to Reaction Chamber

## Alternative Paths

There are **no alternative recipes**. This is an intentionally linear progression designed for endgame content.

## Recipe IDs (for commands)

```
/give @p mekaplus_endgame:temporal_alloy_ingot
/give @p mekaplus_endgame:infinite_energy_matrix
/give @p mekaplus_endgame:radiance_shadow_amalgam
/give @p mekaplus_endgame:antimatter_stabilization_matrix
/give @p mekaplus_endgame:dimensional_fusion_core
/give @p mekaplus_endgame:temporal_catalyst
```

## Testing Recipes

To test if recipes are loaded correctly:
```
/reload
```

Check JEI (Just Enough Items) or REI (Roughly Enough Items) in-game to view the recipes.

---

**Note:** All items are fire-resistant and will not burn in lava!
