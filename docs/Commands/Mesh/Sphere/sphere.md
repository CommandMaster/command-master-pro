---
title: Sphere Commands
order: 5
---

> ⚠️ **Note**
>
> All parameter values in this tool follow Blender’s scene unit system (default: meters).
>
> For example:
> `m.sc 2` will create a sphere with a radius of **2 meters**.
>
> If you want to use different units (e.g., mm or cm), you must change the **Scene Unit Settings** in Blender.
>
> All commands below assume the default unit is **meters (m)**.

# Sphere Commands

Create and control spheres instantly using **Command Master Pro** – no menus, no clicks.

## Command Syntax

```bash
m.sc radius segments rings  locX locY locZ  rotX rotY rotZ  scaleX scaleY scaleZ
```

## Parameters

All parameters are positional and optional (defaults shown below).

| Parameter                  | Type  | Description                                      | Default     |
|---------------------------|-------|--------------------------------------------------|-------------|
| radius                    | float | Sphere radius                                    | 1.0         |
| segments                  | int   | Number of horizontal segments (longitude)        | 32          |
| rings                     | int   | Number of vertical rings (latitude)              | 16          |
| locX locY locZ            | float | Sphere location in 3D space                      | 0 0 0       |
| rotX rotY rotZ            | float | Rotation in degrees                              | 0 0 0       |
| scaleX scaleY scaleZ      | float | Scale factor                                     | 1 1 1       |

> Note: Segments control smoothness around the equator; rings control smoothness from pole to pole.

---

## Basic Examples

**🔹 Default sphere at cursor**

```bash
m.s
```

Creates sphere with default parameters radius=1m, segments=32, rings=16.

**🔹 Custom radius**

```bash
m.s 2
```

Radius = 2m, other parameters default.

**🔹 Radius + segments**

```bash
m.sc 2 24
```

Radius 2m,  segments 24 (less smooth – faceted look), other parameters default.

**🔹 Radius + segments + rings**

```bash
m.sc 2 24 12
```

Radius 2m, segments 24, rings 12.


**🔹 Radius + segments + rings + location**

```bash
m.sc 2 24 12  0 2 0
```

Radius 2m, segments 24, rings 12, location (X = 0, Y = 2m, Z = 0).

**🔹 Radius + segments + rings + location + rotation**

```bash
m.sc 2 24 12  0 2 0  45 0 0
```

Radius 2m, segments 24, rings 12, location (X = 0, Y = 2, Z = 0), rotation(X = 45, Y = 0, Z = 0)
 Rotated 45° around X axis.

**🔹 Full control (radius + segments + rings + location + rotation + scale)**

```bash
m.sc 2 24 12  0 2 0  45 0 0  2 2 2
```

What Values <br>
- Radius 2m
- Segments 24
- Rings 12
- Location (X = 0, Y = 2m, Z = 0)
- Rotation (X = 45°, Y = 0°, Z = 0°)
- Scale (X = 2, Y = 2, Z = 2) → final size 4m diameter

✅ One command = fully modeled sphere with transform.

---

## Practical Use Cases

**🎾 Create a tennis ball (small sphere)**

```bash
m.s 0.067 32 16  0 0 0
```

Radius 0.067, segments 32, rings 16, location (X = 0, Y = 0, Z = 0).
Radius ≈ 6.7cm (regulation tennis ball).

**🌍 Create a planet (large sphere)**

```bash
m.s 5 64 32  0 0 0
```

Radius 5, segments 64, rings 32, location (X = 0, Y = 0, Z = 0).
High segments/rings for smooth planet.

**Create a low-poly decorative ball**

```bash
m.s 1 8 6  0 0 0
```

Radius 1, segments 8, rings 6, location (X = 0, Y = 0, Z = 0).
8 segments, 6 rings → octahedron-like faceted sphere.

**🥚 Create an egg shape (non-uniform scale)**

```bash
m.s 1 32 16  0 0 0  0 0 0  1 1.2 0.8
```


Radius 1, segments 32, rings 16, location (X = 0, Y = 0, Z = 0), rotation(X = 0, Y = 0, Z = 0), Scale(X = 1, Y = 1.2, Z = 0.8) → egg-shaped.

**🏀 Floating spheres at different heights**

```bash
m.s 0.5 32 16  -2 0 0
m.s 0.5 32 16   0 1 0
m.s 0.5 32 16   2 2 0
```

Three spheres at increasing Y heights.

---

## ⚡ Why Use This?

| Step / Task        | Manual Workflow                                                          | Command Master Pro                          |
|------------------|---------------------------------------------------------------------------|---------------------------------------------|
| Workflow Steps   | Add sphere → Set radius → Set segments/rings → Move → Rotate → Scale      | `m.s 2 24 12  0 2 0  45 0 0  2 2 2`         |
| Execution Style  | Multiple clicks and panels                                                | One line, half a second ⚡                  |
| Reusability      | Repetitive for each sphere                                                | Instant reuse (copy/paste command)          |
---

## 💡 Pro Tips

- **Segments vs Rings:** Higher values = smoother sphere but more geometry. For preview, use low values (16, 8).
- Use non-uniform scale to create ellipsoids (e.g., egg, rugby ball).
- Leave trailing parameters empty to use defaults: <br>
    m.sc 1.5 24 → radius 1.5, segments 24, rings default 16.
- Combine with m.c (cube) and m.cy (cylinder) for complex scenes.

---

## Summary

```bash
m.sc [radius] [segments] [rings]  [locX locY locZ]  [rotX rotY rotZ]  [scaleX scaleY scaleZ]
```

Type once → sphere created instantly 😎
No clicks. No delays. Just Command Master Pro.

---


Need more? Check out [Commands Documents](../../) or Raise an issue.



