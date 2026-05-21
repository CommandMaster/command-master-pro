---
title: Cube Commands
order: 3
---

# Cube Commands

Create and control cubes instantly using **Command Master Pro** – no menus, no clicks.

##  Command Syntax

```bash
m.c posX posY posZ rotX rotY rotZ scaleX scaleY bevelWidth bevelSegments
```

All parameters are positional and optional (defaults to zero/origin/1).

Parameter Type Description Default
posX posY posZ float Cube location in 3D space 0 0 0
rotX rotY rotZ float Rotation in degrees 0 0 0
scaleX scaleY float X and Y scale (Z scale = 1) 1 1

---

## Basic Examples

🔹 Default cube at origin

```bash
m.c
```

Adds a cube at (0,0,0) with no bevel.

### 🔹 Cube with custom location

```bash
m.c 2 1 2
```

Cube at X=2, Y=1, Z=2.

🔹 Cube with location + rotation

```bash
m.c 2 1 2  3 4 5
```

Position (2,1,2), rotation (3°,4°,5°).

🔹 Full control (location + rotation + scale + bevel)

```bash
m.c 2 1 2  3 4 5  6 2  0.1 2
```

What Values
Location (2, 1, 2)
Rotation (3°, 4°, 5°)
Scale (6, 2, 1)
Bevel width 0.1
Bevel segments 2

✅ One command = fully modeled cube + bevel modifier.

---

🧱 Practical Use Cases

🏠 Create a wall (wide + thin)

```bash
m.c 0 0 0  0 0 0  5 0.2  0.05 2
```

Scale X=5, Y=0.2 → wide flat wall, beveled edges.

🧱 Create a floor

```bash
m.c 0 0 0  0 0 0  10 10  0 0
```

Large flat plane (no bevel).

🏢 Create a pillar (tall)

```bash
m.c 0 0 0  0 0 0  0.5 3  0.1 3
```

Scale X=0.5, Y=3 → tall pillar with smooth bevel.

🧊 Stack cubes vertically

```bash
m.c 0 0 0
m.c 0 0 1
m.c 0 0 2
```

Three cubes stacked at Y=0,1,2.

---

⚡ Why Use This?

Manual workflow Command Master Pro
Add cube → move → rotate → scale → add bevel → adjust settings m.c 2 1 2 3 4 5 6 2 0.1 2
Multiple clicks and panels One line, half a second
Repetitive for each cube Instant reuse

---

💡 Pro Tips

· Leave trailing parameters empty to use defaults:
    m.c 2 1 → only posX and posY set, rest default.
· Bevel is only applied if bevelWidth > 0.
· Use decimals for precise control: 0.05 for micro bevels.

---

🏁 Summary

```bash
m.c [posX posY posZ] [rotX rotY rotZ] [scaleX scaleY] [bevelWidth bevelSegments]
```

Type once → cube created instantly 😎
No clicks. No delays. Just Command Master Pro.

---

Need more? Check out All Features or Raise an issue.

```

---
