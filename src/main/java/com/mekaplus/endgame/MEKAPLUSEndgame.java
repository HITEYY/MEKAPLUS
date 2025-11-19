package com.mekaplus.endgame;

import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Mod(MEKAPLUSEndgame.MOD_ID)
public class MEKAPLUSEndgame {
    public static final String MOD_ID = "mekaplus_endgame";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    public MEKAPLUSEndgame() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();
        
        ModItems.register(modEventBus);
        
        LOGGER.info("MEKAPLUS Endgame Materials initialized!");
    }
}
