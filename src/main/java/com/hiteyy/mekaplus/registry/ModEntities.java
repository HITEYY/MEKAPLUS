package com.hiteyy.mekaplus.registry;

import com.hiteyy.mekaplus.MekaplusMod;
import com.hiteyy.mekaplus.entity.SoulBossEntity;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MobCategory;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModEntities {
    public static final DeferredRegister<EntityType<?>> ENTITY_TYPES = DeferredRegister.create(ForgeRegistries.ENTITY_TYPES, MekaplusMod.MOD_ID);

    public static final RegistryObject<EntityType<SoulBossEntity>> SOUL_BOSS = ENTITY_TYPES.register("soul_boss",
            () -> EntityType.Builder.of(SoulBossEntity::new, MobCategory.MONSTER)
                    .sized(1.2f, 3.2f)
                    .clientTrackingRange(8)
                    .build("soul_boss"));
}
