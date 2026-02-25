package com.hiteyy.mekaplus.registry;

import com.hiteyy.mekaplus.MekaplusMod;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

public class ModCreativeTabs {
    public static final DeferredRegister<CreativeModeTab> CREATIVE_MODE_TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MekaplusMod.MOD_ID);

    public static final RegistryObject<CreativeModeTab> MAIN_TAB = CREATIVE_MODE_TABS.register("main", () -> CreativeModeTab.builder()
            .title(Component.translatable("itemGroup.mekaplus.main"))
            .icon(() -> ModItems.STARLIGHT.get().getDefaultInstance())
            .displayItems((parameters, output) -> {
                output.accept(ModItems.STARLIGHT.get());
                output.accept(ModItems.SOUL_HEAD.get());
                output.accept(ModItems.ANTIGEAR.get());
                output.accept(ModBlocks.ANTIMATTER_SYNTHESIZER.get());
                output.accept(ModItems.VIBRANIUM.get());
                output.accept(ModItems.SPEED_MODULE_128X.get());
                output.accept(ModItems.DAMAGE_MODULE.get());
            })
            .build());
}
