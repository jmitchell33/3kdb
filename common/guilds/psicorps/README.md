# Psicorps guild

## Power management

Installed powers come from `gs`: `gs_powers` runs 5 seconds after the guild files load (login, `.reload`, gswap) and again on "Implant: Fully Operational.", and marks every installed power that has a key in data.tin in `my[implants]`. Run `gs_powers` yourself after installing or removing an implant. `my[powers]` holds what is up now, from your hpbar/MIP.

- Sustained powers are kept up by the heartbeat when they are installed and picked in `maint` (see Maint below). `maint list` shows each power: picked, installed, up now.
- Single-use powers are strategies (see below).

### Forcing a power to be used

Since psicorps have a 1 power per round limiter, sometimes you want to force a power to be used instead of your normal body adjustment, or body fuel cycle. 

`usep <any power>` will force this command to be used before any other powers are attempted.

This is useful for things like `pset` (guild config) or evaluating a mob.

### Adding a new power

Give it a key in data.tin (the hpbar code), then in the guild heartbeat file add it in the appropriate section. Ex. `_check_power {Vr} {valor};` checks that valor is up every heartbeat. Add it to `maint_spells`, `maint_order` and the name tables in maintenance.tin so `maint` can pick it.

## Specific powers

### Adapt body

If you add `exa mob` to your pre fight check, it will store the best damage type to use for adapt body. You'll need the right mskill that shows you the mobs damage type first. Then when starting the fight it will change adapt body to use the right damage type if it isn't already.

### Maint

Sustained powers (valor, verve, vigor, biofeedback, precognition, barriers, jaws, astral constructs, adapt body...) are kept up by the heartbeat when they are installed (read from `gs`) and picked in `maint`. Maint starts on with every power picked, so nothing changes until you `maint del <power>` one. `maint list` shows the names, `maint-help` the commands. Picks save with the character.

### Demoralize, brilliant blast, flaming shroud

Single-use powers are strategies: `strategy demoralize`, `strategy bblast`, `strategy fshroud`. Brilliant blast is used once per fight, at the start of combat; flaming shroud has no hpbar flag and lasts Intelligence / 2 rounds, so it is recast when that many combat rounds have passed (Int is read from `score short` the first time, run `fsint` after your Int changes); demoralize is repeated until the target can't be re-demoralized.

### Greater mindlink

Add your greater mind link target to the heartbeat file `greater_mind_link_target`.
