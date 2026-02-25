package com.hiteyy.mekaplus.event;

import com.hiteyy.mekaplus.MekaplusMod;
import com.hiteyy.mekaplus.entity.SoulBossEntity;
import com.hiteyy.mekaplus.registry.ModEntities;
import net.minecraftforge.event.entity.EntityAttributeCreationEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = MekaplusMod.MOD_ID, bus = Mod.EventBusSubscriber.Bus.MOD)
public class ModEvents {
    @SubscribeEvent
    public static void registerAttributes(EntityAttributeCreationEvent event) {
        event.put(ModEntities.SOUL_BOSS.get(), SoulBossEntity.createAttributes().build());
    }
}
