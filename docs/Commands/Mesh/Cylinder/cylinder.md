---
title: Cylinder Commands
order: 3
---

> ⚠️ **Note**
>
> All parameter values in this tool follow Blender’s scene unit system (default: meters).
>
> For example:
> `m.cy 1.5` creates a cylinder with **radius = 1.5 meters**.
>
> If you want to use different units (e.g., mm or cm), you must change the **Scene Unit Settings** in Blender.
>
> All commands below assume the default unit is **meters (m)**.

#  Cylinder Commands

Create and control cylinders instantly using **Command Master Pro** – no menus, no clicks.

##  Command Syntax

```bash
m.cy radius depth vertices  locX locY locZ  rotX rotY rotZ  scaleX scaleY scaleZ
```


## Parameters

All parameters are positional and optional (defaults shown below).

| Parameter | Type  | Description                          | Default |
|----------|------|--------------------------------------|---------|
| radius   | float | Cylinder radius                     | 1.0     |
| depth    | float | Cylinder height (along Z)           | 2.0     |
| vertices | int   | Number of vertices (smoothness)     | 32      |
| locX     | float | Location X in 3D space              | 0       |
| locY     | float | Location Y in 3D space              | 0       |
| locZ     | float | Location Z in 3D space              | 0       |
| rotX     | float | Rotation X in degrees               | 0       |
| rotY     | float | Rotation Y in degrees               | 0       |
| rotZ     | float | Rotation Z in degrees               | 0       |
| scaleX   | float | Scale factor X                      | 1       |
| scaleY   | float | Scale factor Y                      | 1       |
| scaleZ   | float | Scale factor Z                      | 1       |

---

## Basic Examples

**🔹 Default cylinder**

```bash
m.cy
```

Creates cylinder: radius=1m, depth=2m, vertices=32, at origin.

**🔹 Custom radius**

```bash
m.cy 1.5
```

Radius = 1.5m, other parameters default.

**🔹 Radius + depth**

```bash
m.cy 1.5 3
```

Radius = 1.5m, depth = 3m.

**🔹 Radius + depth + vertices**

```bash
m.cy 1.5 3 16
```

Radius 1.5m, depth 3m, 16 vertices (less smooth – octagonal look).

**🔹 Radius + depth + vertices + location**

```bash
m.cy 1 2 32  2 1 3
```

Radius 1m, depth 2m, 32 vertices, location (X = 2m, Y = 1, Z = 3).


**🔹 Radius + depth + vertices + location + rotation**

```bash
m.cy 1 2 32  2 1 3  5 6 7
```
Radius 1m, depth 2m, 32 vertices, location (X = 2m, Y = 1, Z = 3). rot(X = 5, Y = 6, Z = 7)

**🔹 Radius + depth + vertices + location + rotation + scale**

```bash
m.cy 1 2 32  2 1 3  5 6 7  9 8 4
```
Radius 1m, depth 2m, 32 vertices, location (X = 2m, Y = 1, Z = 3). rot(X = 5, Y = 6, Z = 7). scale(X = 9, Y = 8, Z = 4)

**🔹 With location only**

```bash
m.cy 1 2 32  1 5 2 
```

Radius 1m, depth 2m, 32 vertices, location (X = 1m, Y = 5m, Z = 2m).


**🔹 With rotation only**

```bash
m.cy 1 2 32  0 0 0 1 2 3 
```

Radius 1m, depth 2m, 32 vertices, rotation (X = 1m, Y = 2m, Z = 3m).



**🔹 With scale only**

```bash
m.cy 1 2 32  0 0 0  0 0 0  2 1 1
```

Scaled 2× on X axis.

**🔹 Full control**

```bash
m.cy 1.5 3 24  2 1 0  0 30 0  1.5 1 1
```

What Values <br>
Radius 1.5m <br>
Depth 3m <br>
Vertices 24 <br>
Location (2m, 1m, 0)  <br>
Rotation (0°, 30°, 0°)  <br>
Scale (1.5, 1, 1)  <br>

✅ One command = fully modeled cylinder with transform.

---

## Practical Use Cases

 **Create a wooden log (short and wide)**

```bash
m.cy 0.8 1.5 24  0 0 0
```

Radius 0.8m, depth 1.5m, vertices 24, location 0 – like a short log.

**Create an oil drum (tall cylinder)**

```bash
m.cy 0.6 2.2 32  0 0 0
```
Radius 0.6m, depth 2.2m, vertices 32, location 0 - Typical drum proportions.

**Create a bolt (low-poly hexagon look)**

```bash
m.cy 0.5 0.3 6  0 0 0
```
Radius 0.5m, depth 0.3m, vertices 6, location 0 - hexagonal shape.

**Create a column (pillar with scale)**

```bash
m.cy 0.5 4 32  0 0 0  0 0 0  1 1 2
```
Radius 0.5m, depth 4m, vertices 32, location 0, rotation 0, scale(X = 1, Y = 1, Z = 2) - double height pillar.

**Align cylinders side by side**

```bash
m.cy 1 2 32  -2 0 0
m.cy 1 2 32   0 0 0
m.cy 1 2 32   2 0 0
```

Three cylinders spaced 2 meters apart.

---

## Why Use This?

| Step / Task              | Manual Workflow                          | Command Master Pro                          |
|------------------------|------------------------------------------|---------------------------------------------|
| Workflow Steps         | Add cylinder → set radius → set depth → move → rotate → scale |  m.cy 1.5 3 24  2 1 0  0 30 0  1.5 1 1
| Execution Style        | Multiple panels and clicks               | One line, half a second
| Create Cylinder        | Add cylinder manually                    | One command handles everything              |
| Set Radius             | Adjust radius in properties panel        | `1.5`                                       |
| Set Depth              | Adjust depth manually                    | `3`                                         |
| Set Vertices           | Change vertices for smoothness           | `24`                                        |
| Set Location           | Move tool / transform panel              | `2 1 0`                                     |
| Set Rotation           | Rotate manually                          | `0 30 0`                                    |
| Set Scale              | Scale tool                               | `1.5 1 1`                                   |
| Full Workflow          | Multiple panels and clicks               | One line, half a second ⚡                  |
| Reusability            | Repeat all steps again                   | Copy/paste command instantly                |

---

### 🧪 Example Command

```bash
m.cy 1.5 3 24  2 1 0  2 30 0  1.5 1 1
```
Radius 1.5m, depth 3m, vertices 24, location(X = 2, Y = 1, Z = 0), rotation(X = 2, Y = 30, Z = 0), scale(X = 1.5, Y = 1, Z = 1) 


## 💡 Pro Tips
- **vertices:** 32 is smooth, 8 or 16 gives faceted look (great for low-poly).
- Leave trailing parameters empty to use defaults: <br>
    m.cy 2 → only radius set, depth=2, vertices=32, rest default.
- Use decimals for precision: m.cy 0.75 1.2 24.
- Combine with m.c (cube) to build complex scenes rapidly.

---

## Summary

```bash
m.cy [radius] [depth] [vertices]  [locX locY locZ]  [rotX rotY rotZ]  [scaleX scaleY scaleZ]
```

Type once → cylinder created instantly 😎
No clicks. No delays. Just Command Master Pro.

---

Need more? Check out [Commands Documents](docs/Commands) or Raise an issue.
