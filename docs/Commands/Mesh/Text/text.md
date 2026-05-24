---
title: Text Commands
order: 6
---

> ⚠️ **Note**
>
> All parameter values in this tool follow Blender’s scene unit system (default: meters).
>
> For example:
> `text Hello 2` will create text with font size of **2 meters**.
>
> If you want to use different units (e.g., mm or cm), you must change the **Scene Unit Settings** in Blender.
>
> All commands below assume the default unit is **meters (m)**.

# Text Commands

Create and control 3D text objects instantly using **Command Master Pro** – no menus, no clicks.

## Command Syntax

```bash
text "content" fontSize  locX locY locZ  rotX rotY rotZ  scaleX scaleY scaleZ
```

## Parameters

| Parameter                  | Type   | Description                                      | Default     |
|---------------------------|--------|--------------------------------------------------|-------------|
| "content"                 | string | The text to display                              | "Text"      |
| fontSize                  | float  | Font size in meters                              | 1.0         |
| locX locY locZ            | float  | Text location in 3D space                        | 0 0 0       |
| rotX rotY rotZ            | float  | Rotation in degrees                              | 0 0 0       |
| scaleX scaleY scaleZ      | float  | Scale factor (multiplies font size)              | 1 1 1       |---


 ## Basic Examples


**🔹 Default text content at origin**

```bash
text Hello
```

Add Text "Hello" at origin

**🔹 Multiple words (use quotes)**

```bash
text "Hello World"
```

Add Text "Hello World" (with space) at origin.

**🔹 Custom font size**

```bash
text Hello 2
```

Add text "Hello" with Font size = 2m.

**🔹 Font size + location**

```bash
text Hello 2  0 2 0
```

Add text "Hello" with Font size 2, location (X = 0,  Y = 2, Z = 0).

**🔹 Font size + location + rotation**

```bash
text Hello 2  0 2 0  45 0 0
```
Add text "Hello" with Font size 2, location (X = 0,  Y = 2, Z = 0), rotation (X = 45,  Y = 0, Z = 0)<br>
Rotated 45° around X axis.

**🔹 Full control (content + size + location + rotation + scale)**

```bash
text Hello 2  0 2 0  45 0 0  2 2 2
```

What Values
- Content "Hello"
- Font size 2
- Location (X = 0, Y = 2, Z = 0)
- Rotation (X = 45°, Y = 0°, Z = 0°)
- Scale (X = 2, Y = 2, Z = 2) → final size 4m

✅ One command = fully modeled 3D text with transform.

---

## Practical Use Cases

**Create a simple label**

```bash
text "Door" 0.5  0 0 1
```

Add text "Door" with Font size 0.5, location (X = 0,  Y = 0, Z = 1).<br>
Small text "Door" floating above a door.

**Create a title sign (large)**

```bash
text "WELCOME" 3  -5 0 2
```

Add text "WELCOME" with Font size 3, location (X = -5,  Y = 0, Z = 2).<br>
Large 3m text at location.

**Stretch text horizontally (non-uniform scale)**

```bash
text "WIDE" 1  0 0 0  0 0 0  2 1 1
```

Add text "WIDE" with Font size 1, location (X = 0,  Y = 0, Z = 0), rotation(X = 0°, Y = 0°, Z = 0°), scale(X = 2, Y = 1, Z = 1)<br>
Scale X = 2 → text stretched horizontally.

**Rotated text along a path**

```bash
text "Curved" 1  0 0 0  0 0 45
```

Add text "WIDE" with Font size 1, location (X = 0,  Y = 0, Z = 0), rotation(X = 0°, Y = 0°, Z = 45°). <br>
Rotated 45° around Z axis.

**Multiple text objects for a scene**

```bash
text "Front" 1  -2 1 0
text "Back"  1   2 1 0  0 180 0
text "Left"  1   0 1 -2  0 -90 0
text "Right" 1   0 1 2   0 90 0
```

Four directional labels around a center point.

---

## ⚡ Why Use This?

| Step / Task        | Manual Workflow                                              | Command Master Pro                          |
|------------------|--------------------------------------------------------------|---------------------------------------------|
| Workflow Steps   | Add text → Type content → Set font size → Move → Rotate → Scale | `text "Hello" 2  0 2 0  45 0 0  2 2 2`      |
| Execution Style  | Multiple clicks and panels                                   | One line, half a second ⚡                  |
| Reusability      | Repetitive for each text object                              | Instant reuse (copy/paste command)          |
---

## 💡 Pro Tips

- **Quotes are important**: For text with spaces, always use double quotes:<br>
    text "My Label" ✅ <br>
    text My Label ❌ 
- Scale vs Font Size: fontSize sets the base height. scale multiplies it.<br>
    Example: text A 1 ... scale 2 2 2 → final height 2m.
- Font defaults to Blender's default font. You can change it later in the Object Data properties.
- Leave trailing parameters empty to use defaults:<br>
    text Title 1.5 0 0 0 → only content "Title", font size 1.5, rest default.
- Use decimals for precise control: text Tiny 0.2.

---

## Summary

```bash
text "content" [fontSize]  [locX locY locZ]  [rotX rotY rotZ]  [scaleX scaleY scaleZ]
```

Type once → 3D text created instantly 😎 <br>
No clicks. No delays. Just Command Master Pro.

---

Need more? Check out [Commands Documents](../../) or Raise an issue.

