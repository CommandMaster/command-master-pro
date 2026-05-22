# Command Master Pro

> Turn complex Blender workflows into simple, blazing-fast commands.

![Blender Version](https://img.shields.io/badge/Blender-5.1%2B-orange?logo=blender)
![Status](https://img.shields.io/badge/Status-Beta-yellow)

---

# Command Master Pro Documentation

Welcome to the official documentation for **Command Master Pro** – “Command Master Pro is a command-based system for Blender that turns complex 3D modeling tasks into fast, simple instructions—making creation quicker, smarter, and more efficient.”

---

## What is Command Master Pro?

Blender workflows are often slow, repetitive, and full of clicks. This add-on solves that by letting you run short & powerful commands like:

- `m.c`
Add cube in your sean
- `m.c 2  1 2 3`
Add cube with size,  location x y z
- `m.c 2 1 2 3  4 5 6`
  Add cube with size,  location x y z,  rotation x y z
- `m.c 2  1 2 3  4 5 6  2 0.1 2`
Add cube with size,   location x y z,  rotation x y z,  scale x y z

👉 **work complete in seconds** 😎

---

##  Why Command Master?

Blender workflows are often **slow, repetitive, and full of clicks**, especially for repeated modeling and setup tasks.

**Command Master Pro** converts complex actions into simple commands — saving time and effort.

---

##  Features

| Feature | Description |
|---------|-------------|
|  One-line object creation | `mesh.cube.create` |
|  Smart extrude system | Parameter-based extrusions without manual dragging |
|  Automated lighting setup | 3-point lighting in one command |
|  Command-based workflow | Use Blender Text Editor or Python Console |
|  Easy to extend | Add custom commands quickly |

---

## Before vs After

| Before | After |
|--------|------|
| Add → Mesh → Cube | `m.c` |
| quick create wall | `m.c 2 0 0 0  0 0 0. 2 0.1 2 ` |
| Add → Mesh → Cylinder | `m.cy` |

---

##  Who is this for?

- Beginners learning Blender  
- Technical artists automating workflows  
- Developers who love scripting  
- Power users optimizing speed  

---

## 🎬 Demo

![Demo](https://via.placeholder.com/800x400?text=Add+Your+Demo+GIF+Here)

---

##  Installation

1. Download ZIP from Releases  
2. Open Blender → Preferences → Add-ons  
3. Click Install → Select ZIP file
4. restart blender 
5. Enable “Command Master Pro”
6. ctrl+spacebar 
7. Start using commands in Blender  

---

## ⚡ Quick Example

```python
mesh.cube.create
modifier.bevel width=0.1

mesh.sphere.create radius=0.5

light.three_point.setup intensity=1.2



## 🚀 Installation

For full setup instructions, see:

👉 [Installation Guide](docs/installation.md)
