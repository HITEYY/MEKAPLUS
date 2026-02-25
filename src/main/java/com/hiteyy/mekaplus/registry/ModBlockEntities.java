package com.hiteyy.mekaplus.registry;

import com.hiteyy.mekaplus.MekaplusMod;
import com.hiteyy.mekaplus.block.entity.AntimatterSynthesizerBlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModBlockEntities {
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, MekaplusMod.MOD_ID);

    public static final RegistryObject<BlockEntityType<AntimatterSynthesizerBlockEntity>> ANTIMATTER_SYNTHESIZER_BE =
            BLOCK_ENTITIES.register("antimatter_synthesizer", () -> BlockEntityType.Builder.of(AntimatterSynthesizerBlockEntity::new, ModBlocks.ANTIMATTER_SYNTHESIZER.get()).build(null));
}
