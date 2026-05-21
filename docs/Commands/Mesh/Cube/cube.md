---
title: Cube Commands
order: 3
---

> ⚠️ **Note**
>
> All parameter values in this tool follow Blender’s scene unit system (default: meters).
>
> For example:
> `M.c 2` will create a cube with a size of **2 meters**.
>
> If you want to use different units (e.g., mm or cm), you must change the **Scene Unit Settings** in Blender.
>
> All commands below assume the default unit is **meters (m)**.


# Cube Commands

Create and control cubes instantly using **Command Master Pro** – no menus, no clicks.

##  Command Syntax

```bash
m.c size locX locY locZ rotX rotY rotZ scaleX scaleY scaleZ
```

All parameters are positional and optional (defaults to zero/origin/1).

Parameter Type Description Default
locX locY locZ float Cube location in 3D space 0 0 0
rotX rotY rotZ float Rotation in degrees 0 0 0
scaleX scaleY scaleZ 1 1 1 

---

## Basic Examples

**🔹 Default cube at origin**

```bash
m.c
```

Adds a cube at (0,0,0).

**🔹 Cube with custom location**

```bash
m.c 2  2 1 2
```

Cube size 2m location X=2m, Y=1m, Z=2m.

**🔹 Cube with location + rotation**

```bash
m.c 2  2 1 2  3 4 5
```

Size (2m) Position (2m,1m,2m), rotation (3°,4°,5°).

**🔹 Full control (size + location + rotation + scale )**

```bash
m.c 2  2 1 2  3 4 5  6 2 1 
```

What Values
Size (2m)
Location (2m, 1m, 2m)
Rotation (3°, 4°, 5°)
Scale (6m, 2m, 1m)

✅ One command = fully modeled cube

---

## Practical Use Cases

**🏠 Create a wall (wide + thin)**

```bash
m.c 2 0 0 0  0 0 0  2 0.2 1
```

*Syntax*
m.c [size] [locX locY locZ] [rotX rotY rotZ] [scaleX scaleY scaleZ]

Size 2m,
Location X=0m, Y=0m, Z=0m
Rotation X=0deg, Y=0deg, Z=0deg
Scale X=2m, Y=0.2m Z=1m 
→ wide flat wall.

**🧱 Create a floor**

```bash
m.c 2 0 0 0  0 0 0  5 5 0.2
```

*Syntax*
m.c [size] [locX locY locZ] [rotX rotY rotZ] [scaleX scaleY scaleZ]

Size 2m,
Location X=0m, Y=0m, Z=0m
Rotation X=0deg, Y=0deg, Z=0deg
Scale X=5m, Y=5m Z=0.2m 
 → Large flat plane.

**🏢 Create a pillar (tall)**

```bash
m.c 2  0 0 0  0 0 0  0.5 0.5 4
```

*Syntax*
m.c [size] [locX locY locZ] [rotX rotY rotZ] [scaleX scaleY scaleZ]


Size 2m,
Location X=0m, Y=0m, Z=0m
Rotation X=0deg, Y=0deg, Z=0deg
Scale X=0.5m, Y=0.5m Z=4m 
 → tall pillar.
 
 ---

## Why Use This?

Manual workflow Command Master Pro
Add cube → move → rotate → scale → adjust settings m.c 2  1 2 3  4 5 6  2 0.1 2
Multiple clicks and panels One line, half a second
Repetitive for each cube Instant reuse

---

## Pro Tips

· Leave trailing parameters empty to use defaults:
    m.c 2 1 → only posX and posY set, rest default.
· Use decimals for precise control: 0.05 for micro bevels.

---

🏁 Summary

```bash
m.c [size] [locX locY locZ] [rotX rotY rotZ] [scaleX scaleY scaleZ]
```

Type once → cube created instantly 😎
No clicks. No delays. Just Command Master Pro.

---

Need more? Check out All Features or Raise an issue.

```

---
