package com.hiteyy.mekaplus.registry;

import com.hiteyy.mekaplus.MekaplusMod;
import com.hiteyy.mekaplus.block.AntimatterSynthesizerBlock;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModBlocks {
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, MekaplusMod.MOD_ID);

    public static final RegistryObject<Block> ANTIMATTER_SYNTHESIZER = BLOCKS.register("antimatter_synthesizer",
            () -> new AntimatterSynthesizerBlock(BlockBehaviour.Properties.of().mapColor(MapColor.COLOR_PURPLE).strength(8.0f, 1200.0f).sound(SoundType.NETHERITE_BLOCK).requiresCorrectToolForDrops()));

}
