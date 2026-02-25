package com.hiteyy.mekaplus.registry;

import com.hiteyy.mekaplus.MekaplusMod;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Rarity;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, MekaplusMod.MOD_ID);

    public static final RegistryObject<Item> STARLIGHT = ITEMS.register("starlight",
            () -> new Item(new Item.Properties().rarity(Rarity.EPIC).fireResistant()));

    public static final RegistryObject<Item> SOUL_HEAD = ITEMS.register("soul_head",
            () -> new Item(new Item.Properties().rarity(Rarity.UNCOMMON).stacksTo(16)));

    public static final RegistryObject<Item> ANTIGEAR = ITEMS.register("antigear",
            () -> new Item(new Item.Properties().rarity(Rarity.RARE).stacksTo(64).fireResistant()));

    public static final RegistryObject<Item> VIBRANIUM = ITEMS.register("vibranium",
            () -> new Item(new Item.Properties().rarity(Rarity.EPIC).fireResistant()));

    public static final RegistryObject<Item> SPEED_MODULE_128X = ITEMS.register("speed_module_128x",
            () -> new Item(new Item.Properties().rarity(Rarity.EPIC).stacksTo(16)));

    public static final RegistryObject<Item> DAMAGE_MODULE = ITEMS.register("damage_module",
            () -> new Item(new Item.Properties().rarity(Rarity.EPIC).stacksTo(16)));

    public static final RegistryObject<Item> ANTIMATTER_SYNTHESIZER_ITEM = ITEMS.register("antimatter_synthesizer",
            () -> new BlockItem(ModBlocks.ANTIMATTER_SYNTHESIZER.get(), new Item.Properties()));
}
