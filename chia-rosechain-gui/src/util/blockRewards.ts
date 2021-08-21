import Big from 'big.js';

// const MOJO_PER_CHIA = Big(1000000000000);
const MOJO_PER_CHIA = Big(1000000000);
const BLOCKS_PER_YEAR = 1681920;

export function calculatePoolReward(height: number): Big {
  if (height === 0) {
    return MOJO_PER_CHIA.times(201710200).times(7 / 8);
  }
  if (height < 3 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(200).times(7 / 8);
  }
  if (height < 6 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(100).times(7 / 8);
  }
  if (height < 9 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(50).times(7 / 8);
  }
  if (height < 12 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(25).times(7 / 8);
  }
  if (height < 15 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(12.5).times(7 / 8);
  }
  return MOJO_PER_CHIA.times(1).times(7 / 8);
}

export function calculateBaseFarmerReward(height: number): Big {
  if (height === 0) {
    return MOJO_PER_CHIA.times(201710200).times(1 / 8);
  }
  if (height < 3 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(200).times(1 / 8);
  }
  if (height < 6 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(100).times(1 / 8);
  }
  if (height < 9 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(50).times(1 / 8);
  }
  if (height < 12 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(25).times(1 / 8);
  }
  if (height < 15 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(12.5).times(1 / 8);
  }
  return MOJO_PER_CHIA.times(1).times(1 / 8);
}
