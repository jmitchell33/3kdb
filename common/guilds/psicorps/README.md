# Psicorps guild

## Power management

Features a built in power management system that lets you configure a set of powers to always be on. All powers are referred to by their in game power abbreviation. Adding a power to the configuration will attempt to always keep it on. 

- If a power is not on, it will be turned on.
- If a power is about to expire, it will be refreshed.

Features smart power management so it removes powers you have not included.

- If a power is on but not in your configuration, it will be turned off.

### Adding a power

`addp <power>` ex. `addp Vr` 

Adds the valor power to your power configuration.

### Removing a power

`remp <power>` ex. `remp Vr`

### Show power configuration

`showp` shows all powers that will be maintained

```
----------------
--- Defense ----
----------------                                                     
Vg - vigor                                                           
```

### Forcing a power to be used

Since psicorps have a 1 power per round limiter, sometimes you want to force a power to be used instead of your normal body adjustment, or body fuel cycle. 

`usep <any power>` will force this command to be used before any other powers are attempted.

This is useful for things like `pset` (guild config) or evaluating a mob.

### Adding a new power

In the guild heartbeat file, add the new power in the appropriate section. Ex. `@check_power{Vr;valor};` will check that valor is turned on every heartbeat using the logic specified above.

In the guild aliases file, add the new power in the appropriate section to the show power configuration alias. Ex.   `@show_power{Vr;valor};` so when you use `showp` it will show if valor is configured or not.

### Creating an alias to create a power configuration set

All powers are stored inside a list called `combat`. Just setup an alias with any name you like and set the power to 0 or 1 as needed. 

Here's an example of a defense setup:

```
#alias {defense} {
  #var combat {};

  #nop -- Defense buffs;

  #var combat[Vr] 0;
  #var combat[Eb] 0;
  #var combat[Cp] 0;
  #var combat[Iv] 1;
  #var combat[IV] 1;
  #var combat[Ib] 1;
  #var combat[IB] 1;
  #var combat[Vg] 1;
  #var combat[Vv] 0;
  #var combat[ab] 1;

  #nop -- Combat buffs;

  #var combat[Sj] 1;
  #var combat[Bo] 1;
  #var combat[CP] 1;
  #var combat[pf] 0;

  #nop -- Combat powers;

  #var combat[bc] 1;
  #var combat[rpain] 1;
};
```

It is recommended to create a default power set and run this as part your character's tintin++ initialization so that a set of powers is always present.

## Specific powers

### Adapt body

If you add `exa mob` to your pre fight check, it will store the best damage type to use for adapt body. You'll need the right mskill that shows you the mobs damage type first. Then when starting the fight it will change adapt body to use the right damage type if it isn't already.

Make sure to add adapt body to your power configuration with `addp ab`.

### Demoralize, brilliant blast

These are used once per fight at the start. For brilliant blast, it'll only do it if it's considered a safe arae. For now that's chessboard, but feel free to modify as you see fit. Eventually, we can add some code around checking number of targets or expand the logic.

If you have both demoralize and brilliant blast, it'll try to chain them in one round.

Make sure to add them to your power configuration: `addp dm` and `addp bb`
Or better yet add them to your power aliases with `#var combat[dm] 1` and `#var combat[bb] 1`.

Also make sure to reset the `_dm` and `_bb` variables to 0 before starting a fight so that the script knows to try to use them. A good place to do that is in the `.pre_fight_check` alias.

### Greater mindlink

Add your greater mind link target to the heartbeat file `greater_mind_link_target` and `addp ML`
