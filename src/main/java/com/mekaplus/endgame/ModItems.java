package com.mekaplus.endgame;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.Rarity;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModItems {
    public static final DeferredRegister<Item> ITEMS = 
            DeferredRegister.create(ForgeRegistries.ITEMS, MEKAPLUSEndgame.MOD_ID);

    // Epic rarity items
    public static final RegistryObject<Item> TEMPORAL_ALLOY_INGOT = ITEMS.register("temporal_alloy_ingot",
            () -> new Item(new Item.Properties()
                    .stacksTo(8)
                    .rarity(Rarity.EPIC)
                    .fireResistant()));

    public static final RegistryObject<Item> INFINITE_ENERGY_MATRIX = ITEMS.register("infinite_energy_matrix",
            () -> new Item(new Item.Properties()
                    .stacksTo(16)
                    .rarity(Rarity.EPIC)
                    .fireResistant()));

    public static final RegistryObject<Item> DIMENSIONAL_FUSION_CORE = ITEMS.register("dimensional_fusion_core",
            () -> new Item(new Item.Properties()
                    .stacksTo(8)
                    .rarity(Rarity.EPIC)
                    .fireResistant()));

    public static final RegistryObject<Item> TEMPORAL_CATALYST = ITEMS.register("temporal_catalyst",
            () -> new Item(new Item.Properties()
                    .stacksTo(4)
                    .rarity(Rarity.EPIC)
                    .fireResistant()));

    // Rare rarity items
    public static final RegistryObject<Item> RADIANCE_SHADOW_AMALGAM = ITEMS.register("radiance_shadow_amalgam",
            () -> new Item(new Item.Properties()
                    .stacksTo(16)
                    .rarity(Rarity.RARE)
                    .fireResistant()));

    public static final RegistryObject<Item> ANTIMATTER_STABILIZATION_MATRIX = ITEMS.register("antimatter_stabilization_matrix",
            () -> new Item(new Item.Properties()
                    .stacksTo(16)
                    .rarity(Rarity.RARE)
                    .fireResistant()));

    public static void register(IEventBus eventBus) {
        ITEMS.register(eventBus);
    }
}
