// CI-only preload: make zero-argument Date/Date.now honor BUILD_CLOCK.
// This catches future accidental wall-clock reads without changing the runner clock.
const RealDate = Date;
const rawClock = process.env.BUILD_CLOCK;

if (rawClock) {
  const frozenAt = new RealDate(rawClock).getTime();
  if (!Number.isFinite(frozenAt)) {
    throw new Error(`Invalid BUILD_CLOCK: ${rawClock}`);
  }

  class FrozenDate extends RealDate {
    constructor(...args) {
      super(...(args.length === 0 ? [frozenAt] : args));
    }

    static now() {
      return frozenAt;
    }
  }

  global.Date = FrozenDate;
}
