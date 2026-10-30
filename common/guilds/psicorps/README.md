# Psicorps guild

## Power management

Features a built in power management system that lets you configure a set of powers to always be on. All powers are referred to by their in game power abbreviation. Adding a power to the configuration will attempt to always keep it on. The logic is stored in my[implants] for what you have installed and my[powers] stores what is in your hpbar/MIP to compare the two.

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

In the guild heartbeat file, add the new power in the appropriate section. Ex. `_check_power {Vr} {valor};` will check that valor is turned on every heartbeat using the logic specified above.

In the guild aliases file, add the new power in the appropriate section to the show power configuration alias. Ex.   `_show_power {Vr} {valor};` so when you use `showp` it will show if valor is configured or not.

### Creating an alias to create a power configuration set

All powers are stored inside a list called `my[implants]`. There are two values stored, whether it is installed and whether it is active.  Just setup an alias with any name you like and set the my[implants][active] to 0 or 1 as needed. 

Here's an example of a defense setup:

```
#alias {defense} {
  #var my[implants] {};

  #nop -- Defense buffs;

  #var my[implants][Vr][active] 0;
  #var my[implants][Eb][active] 0;
  #var my[implants][Cp][active] 0;
  #var my[implants][Iv][active] 1;
  #var my[implants][IV][active] 1;
  #var my[implants][Ib][active] 1;
  #var my[implants][IB][active] 1;
  #var my[implants][Vg][active] 1;
  #var my[implants][Vv][active] 0;
  #var my[implants][ab][active] 1;

  #nop -- Combat buffs;

  #var my[implants][Sj][active] 1;
  #var my[implants][Bo][active] 1;
  #var my[implants][CP][active] 1;
  #var my[implants][pf][active] 0;

  #nop -- Combat powers;

  #var my[implants][bc][active] 1;
  #var my[implants][rpain][active] 1;
};
```

It is recommended to create a default power set and run this as part your character's tintin++ initialization so that a set of powers is always present.

## Specific powers

### Adapt body

If you add `exa mob` to your pre fight check, it will store the best damage type to use for adapt body. You'll need the right mskill that shows you the mobs damage type first. Then when starting the fight it will change adapt body to use the right damage type if it isn't already.

Make sure to add adapt body to your power configuration with `addp ab`.

### Maint

Sustained powers (valor, verve, vigor, biofeedback, precognition, barriers, jaws, astral constructs, adapt body...) are kept up by the heartbeat when they are picked in `maint` and their implant is on (`addp`). Maint starts on with every power picked, so nothing changes until you `maint del <power>` one. `maint list` shows the names, `maint-help` the commands. Picks save with the character.

### Demoralize, brilliant blast

Single-use powers are strategies: `strategy demoralize`, `strategy bblast`. Brilliant blast is used once per fight, at the start of combat; demoralize is repeated until the target can't be re-demoralized.

Make sure to add them to your power configuration: `addp dm` and `addp bb`. Flaming shroud wears off, so it is a maint power (`addp fs`, `maint del fshroud` to stop it)

### Greater mindlink

Add your greater mind link target to the heartbeat file `greater_mind_link_target` and `addp ML`
