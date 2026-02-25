package com.hiteyy.mekaplus.event;

import com.hiteyy.mekaplus.registry.ModEntities;
import com.hiteyy.mekaplus.registry.ModItems;
import net.minecraft.core.BlockPos;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraftforge.event.entity.player.PlayerInteractEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

public class SoulHeadSummonHandler {

    @SubscribeEvent
    public void onRightClickBlock(PlayerInteractEvent.RightClickBlock event) {
        if (event.getItemStack().getItem() != ModItems.SOUL_HEAD.get()) return;
        Level level = event.getLevel();
        if (level.isClientSide) return;

        BlockPos top = event.getPos().above();
        if (!isWitherLikeSoulSand(level, event.getPos())) return;
        if (!level.getBlockState(top).isAir()) return;

        clearStructure(level, event.getPos());

        EntityType<?> type = ModEntities.SOUL_BOSS.get();
        var boss = type.create(level);
        if (boss != null) {
            boss.moveTo(top.getX() + 0.5, top.getY(), top.getZ() + 0.5, level.random.nextFloat() * 360f, 0f);
            level.addFreshEntity(boss);
            if (!event.getEntity().isCreative()) {
                event.getItemStack().shrink(1);
            }
            event.setCancellationResult(InteractionResult.SUCCESS);
            event.setCanceled(true);
        }
    }

    private boolean isWitherLikeSoulSand(Level level, BlockPos centerBottom) {
        BlockState center = level.getBlockState(centerBottom);
        if (!center.is(Blocks.SOUL_SAND) && !center.is(Blocks.SOUL_SOIL)) return false;

        BlockPos upper = centerBottom.above();
        BlockPos left = upper.west();
        BlockPos right = upper.east();

        return isSoul(level, upper) && isSoul(level, left) && isSoul(level, right);
    }

    private boolean isSoul(Level level, BlockPos pos) {
        BlockState state = level.getBlockState(pos);
        return state.is(Blocks.SOUL_SAND) || state.is(Blocks.SOUL_SOIL);
    }

    private void clearStructure(Level level, BlockPos centerBottom) {
        BlockPos upper = centerBottom.above();
        level.destroyBlock(centerBottom, false);
        level.destroyBlock(upper, false);
        level.destroyBlock(upper.west(), false);
        level.destroyBlock(upper.east(), false);
    }
}
