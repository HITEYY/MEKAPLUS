package com.hiteyy.mekaplus.block.entity;

import com.hiteyy.mekaplus.registry.ModBlockEntities;
import com.hiteyy.mekaplus.registry.ModItems;
import net.minecraft.core.BlockPos;
import net.minecraft.core.NonNullList;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.world.ContainerHelper;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;

public class AntimatterSynthesizerBlockEntity extends BlockEntity {
    private NonNullList<ItemStack> inventory = NonNullList.withSize(2, ItemStack.EMPTY);
    private int progress;

    public AntimatterSynthesizerBlockEntity(BlockPos pos, BlockState state) {
        super(ModBlockEntities.ANTIMATTER_SYNTHESIZER_BE.get(), pos, state);
    }

    public static void tick(AntimatterSynthesizerBlockEntity be) {
        if (be.level == null || be.level.isClientSide) return;

        ItemStack input = be.inventory.get(0);
        ItemStack output = be.inventory.get(1);

        if (input.getItem() == ModItems.ANTIGEAR.get() && input.getCount() >= 8 && (output.isEmpty() || (output.getItem() == ModItems.VIBRANIUM.get() && output.getCount() < output.getMaxStackSize()))) {
            be.progress++;
            if (be.progress >= 200) {
                input.shrink(8);
                if (output.isEmpty()) {
                    be.inventory.set(1, new ItemStack(ModItems.VIBRANIUM.get()));
                } else {
                    output.grow(1);
                }
                be.progress = 0;
                be.setChanged();
            }
        } else {
            be.progress = 0;
        }
    }

    @Override
    protected void saveAdditional(CompoundTag tag) {
        super.saveAdditional(tag);
        ContainerHelper.saveAllItems(tag, inventory);
        tag.putInt("Progress", progress);
    }

    @Override
    public void load(CompoundTag tag) {
        super.load(tag);
        inventory = NonNullList.withSize(2, ItemStack.EMPTY);
        ContainerHelper.loadAllItems(tag, inventory);
        progress = tag.getInt("Progress");
    }
}
