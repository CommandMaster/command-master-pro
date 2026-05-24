---
title: Plane Commands
order: 4
---

> ⚠️ **Note**
>
> All parameter values in this tool follow Blender’s scene unit system (default: meters).
>
> For example:
> `m.p 5` will create a plane with a size of **5 meters**.
>
> If you want to use different units (e.g., mm or cm), you must change the **Scene Unit Settings** in Blender.
>
> All commands below assume the default unit is **meters (m)**.

# Plane Commands

Create and control planes instantly using **Command Master Pro** – no menus, no clicks.

##  Command Syntax

```bash
m.p size locX locY locZ rotX rotY rotZ scaleX scaleY scaleZ
```

## Parameters

All parameters are positional and optional (defaults shown below). <br>


| Parameter                  | Type  | Description                          | Default     |
|---------------------------|-------|--------------------------------------|-------------|
| size                      | float | Plane width and height (square)      | 2.0         |
| locX locY locZ            | float | Plane location in 3D space           | 0 0 0       |
| rotX rotY rotZ            | float | Rotation in degrees                  | 0 0 0       |
| scaleX scaleY scaleZ      | float | Scale factor                         | 1 1 1       |

> Note: 
> The plane is a flat mesh (X-Y plane by default). Scaling X/Y stretches it non-uniformly.

---

## Basic Examples

**🔹 Default plane at origin**

```bash
m.p
```

Creates a default plane at location (0,0,0).

**🔹 Custom size**

```bash
m.p 5
```

Plane with size = 5m.

**🔹 Size + location**

```bash
m.p 3  1 2 0
```

Size 3m, location (X = 1m, Y = 2, Z = 0).


**🔹 Size + location + rotation**

```bash
m.p 3  1 2 0  0 45 0
```

Size 3m, location (X = 1, Y = 2, Z = 0), rotated(X = 0, Y = 45deg, Z = 0)


**🔹 Size + location + rotation + scale**

```bash
m.p 3  1 2 0  0 45 0  1 2 1
```

Size 3m, location (X = 1, Y = 2, Z = 0), rotated(X = 0, Y = 45deg, Z = 0), scale(X = 1, Y = 2, Z = 1)

**🔹 Full control (size + location + rotation + scale)**

```bash
m.p 3  1 2 0  0 45 0  2 2 1
```

What Values <b>
- Size 3m (base width/height)
- Location (X = 1m,Y = 2m,Z = 0)
- Rotation (X = 0°,Y = 45°,Z = 0°)
- Scale (X = 2,Y = 2,Z = 1)

✅ One command = fully modeled plane with transform.

---

## Practical Use Cases
 
**🔹 Create a ground plane**

```bash
m.p 10  0 0 -0.1
```
Size 10m, location (X = 0, Y = 0,Z = -0.1) Large ground plane slightly below origin.

**🔹 Create a mirror surface (non-uniform)**

```bash
m.p 2  0 0 0  0 0 0  5 1 1
```

Size 2, location (X = 0, Y = 0, Z = 0) rotated(X = 0, Y = 0, Z = 0), scale(X = 5, Y = 1, Z = Wide rectangular plane – perfect for mirror or water.

**🔹 Create a picture frame backplate**

```bash
m.p 1.5  0 0 1  90 0 0  1 1 0.05
```

Size 1.5, location (X = 0, Y = 0, Z = 1) rotated(X = 90, Y = 0, Z = 0), scale(X = 1, Y = 1, Z = 0.05) Rotated 90° on X → vertical plane, thin scale on Z.

**🔹 Create a ramp (rotated)**

```bash
m.p 4  0 0 1  30 0 0
```
Size 4, location (X = 0, Y = 2, Z = 1), rotated(X = 30, Y = 0, Z = 0)
Rotated 30° around X – slanted ramp.


**🔹 Align multiple planes as walls**

```bash
m.p 4  -2 0 0  0 90 0    # left wall (rotated 90° Y)
m.p 4   2 0 0  0 90 0    # right wall
m.p 4   0 2 0            # back wall (default rotation)
```

Three walls forming a room corner.

---

## Why Use This?

| Step / Task        | Manual Workflow                              | Command Master Pro                     |
|------------------|----------------------------------------------|----------------------------------------|
| Workflow Steps   | Add plane → Set size → Move → Rotate → Scale | `m.p 3  1 2 0  0 45 0  2 2 1`          |
| Execution Style  | Multiple clicks and panels                   | One line, half a second ⚡             |
| Reusability      | Repetitive for each plane                    | Instant reuse (copy/paste command)     |

---

## Pro Tips

- **Scale vs Size:** size sets the base width/height. scale multiplies it.<br>
    Example: m.p 2 ... scale 3 3 1 → final 6×6 plane.
- Use rotation to make vertical walls: m.p 2  0 0 0  90 0 0 (rotate 90° on X).
- Leave trailing parameters empty to use defaults: <br>
    m.p 4 0 0 0 → size 4, rest default.
- Combine with m.c (cube) and m.cy (cylinder) to build scenes fast.

---

## Summary

```bash
m.p [size] [locX locY locZ] [rotX rotY rotZ] [scaleX scaleY scaleZ]
```

Type once → plane created instantly 😎 <br>
No clicks. No delays. Just Command Master Pro.

---

Need more? Check out [Commands Documents](../../) or Raise an issue.
