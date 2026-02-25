package com.hiteyy.mekaplus;

import com.hiteyy.mekaplus.event.SoulHeadSummonHandler;
import com.hiteyy.mekaplus.registry.ModBlockEntities;
import com.hiteyy.mekaplus.registry.ModBlocks;
import com.hiteyy.mekaplus.registry.ModCreativeTabs;
import com.hiteyy.mekaplus.registry.ModEntities;
import com.hiteyy.mekaplus.registry.ModItems;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod(MekaplusMod.MOD_ID)
public class MekaplusMod {
    public static final String MOD_ID = "mekaplus";

    public MekaplusMod(FMLJavaModLoadingContext context) {
        IEventBus modBus = context.getModEventBus();
        ModItems.ITEMS.register(modBus);
        ModBlocks.BLOCKS.register(modBus);
        ModBlockEntities.BLOCK_ENTITIES.register(modBus);
        ModEntities.ENTITY_TYPES.register(modBus);
        ModCreativeTabs.CREATIVE_MODE_TABS.register(modBus);

        MinecraftForge.EVENT_BUS.register(new SoulHeadSummonHandler());
    }
}
