# Psicorps guild

## Power management

Installed powers come from `gs`: `gs_powers` runs 5 seconds after the guild files load (login, `.reload`, gswap) and again on "Implant: Fully Operational.", and marks every installed power that has a key in data.tin in `my[implants]`. Run `gs_powers` yourself after installing or removing an implant. `my[powers]` holds what is up now, from your hpbar/MIP. The heartbeat keeps every installed sustained power up.

### Forcing a power to be used

Since psicorps have a 1 power per round limiter, sometimes you want to force a power to be used instead of your normal body adjustment, or body fuel cycle. 

`usep <any power>` will force this command to be used before any other powers are attempted.

This is useful for things like `pset` (guild config) or evaluating a mob.

### Adding a new power

Give it a key in data.tin (the hpbar code), then in the guild heartbeat file add it in the appropriate section. Ex. `_check_power {Vr} {valor};` checks that valor is up every heartbeat.

## Specific powers

### Adapt body

If you add `exa mob` to your pre fight check, it will store the best damage type to use for adapt body. You'll need the right mskill that shows you the mobs damage type first. Then when starting the fight it will change adapt body to use the right damage type if it isn't already.

Make sure to add adapt body to your power configuration with `addp ab`.

### Demoralize, brilliant blast

These are used once per fight at the start. For brilliant blast, it'll only do it if it's considered a safe area. For now that's chessboard, but feel free to modify as you see fit. Eventually, we can add some code around checking number of targets or expand the logic.

If you have both demoralize and brilliant blast, it'll try to chain them in one round.

Make sure to add them to your power configuration: `addp dm` and `addp bb`

### Greater mindlink

Add your greater mind link target to the heartbeat file `greater_mind_link_target`.
