---
title: Collection Commands
order: 6
---

> ⚠️ **Note**
>
> Collection commands work directly with Blender’s outliner. Colors are applied using Blender’s built‑in collection color tags.
>
> Available color names: `red`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `gray`, `black`, `white`, or hex codes like `#ff6600`.

# Collection Commands

Manage collections, move objects, and organise your scene instantly using **Command Master Pro** – no outliner dragging, no right‑click menus.

## Command Syntax

All commands use the `col.` prefix for collections and `obj.` for objects.

| Command | Description |
|---------|-------------|
| `col.new name1, name2, ...` | Create one or multiple collections |
| `col.new parent;color>child;color` | Create nested collections with colors |
| `col.add collection;color` | Move selected objects into a collection (auto‑creates if missing, sets color) |
| `col.sel collection1, collection2, ...` | Select all objects inside given collections |
| `col.hide collection1, collection2, ...` | Hide all objects in given collections |
| `col.show collection1, collection2, ...` | Unhide all objects in given collections |
| `col source move target` | Move an entire collection inside another collection |
| `obj.move collection;color` | Move selected objects into a collection (auto‑create, set color) |
| `obj obj1, obj2, ... move collection;color` | Move specific objects by name into a collection |

> 💡 **Tip:** Use `;color` after any collection name to set or change its color tag.

---

## 🚀 Basic Examples

**🔹 Create a single collection**
```bash
col.new city
```

Creates an empty collection named city.

**🔹 Create a single collection with color**
```bash
col.new city;red
```

Creates an empty collection named city color red.

**🔹 Create multiple collections**

```bash
col.new city, ahmed, car, house
```

Creates four collections at once.


**🔹 Create multiple collections with colors**

```bash
col.new city;green, ahmed;red, car;yellow, house;blue
```

Creates four collections at once with colors.


**🔹 Move selected objects into a collection**

```bash
col.add city;green
```

Moves all currently selected objects into city. If city doesn’t exist, it is created and colored green.

**🔹 Move specific objects by name**

```bash
obj Cube, Camera, Light move city;green
```

Moves objects named Cube, Camera, Light into city (auto‑creates with green color if needed).

**🔹 Select all objects in collections**

```bash
col.sel city, environment, collection
```

Selects every object inside city, environment, and collection.

**🔹 Hide / show collections**

```bash
col.hide city, environment
```
Hide city and environment collection 

```bash
col.show city
```
Show city collection 


**🔹 Move a collection inside another**

```bash
col city move Environment 
```

Moves the entire city collection inside an existing collection named Environment.

**🔹 Nested collections with colors**

```bash
col.new city;red>buildings;green>houses;yellow
```

Creates this hierarchy:

```
city (red)
  └─ buildings (green)
       └─ houses (yellow)



**🔹 Nested collections with colors**

```bash
col.new city;red>buildings;green>houses;yellow, environment;green>tree;blue, house;pink
```

Creates this hierarchy:

```
city (red)
  └─ buildings (green)
       └─ houses (yellow)
environment (green)
  └─ tree (blue)
house (pink)
```

---

# Practical Use Cases

**Organise a city scene**

```bash
col.new city;blue
col.add city;blue          # move selected buildings into city
col.new city>roads;gray
col.new city>vegetation;green
col.new city>vehicles;red
```

Clean, colour‑coded hierarchy.

**Hide temporary collections during animation**

```bash
col.hide high_poly_props, background_characters
col.sel camera_rig, lights
# work on animation
col.show high_poly_props, background_characters
```

**Move scattered objects into a new collection**

```bash
obj Cube.001, Sphere, Cylinder move props;orange
```

Instantly groups them without dragging in outliner.

**Restructure by moving a whole collection**

```bash
col old_assets move archive
```

Moves old_assets inside archive – perfect for cleanup.

---

# ⚡ Why Use This?


| Step / Task        | Manual Workflow                                                                 | Command Master Pro                                      |
|------------------|----------------------------------------------------------------------------------|----------------------------------------------------------|
| Workflow Steps   | Open outliner → Right-click → New collection → Type name → Drag objects          | `col.new props;red + col.add props`                      |
| Selection        | Find and select objects from different collections manually                     | `col.sel city, vehicles, lights`                         |
| Visibility       | Hide each collection via eye icons                                               | `col.hide city, vehicles`                                |
| Structure        | Create nested folders with colors                                                | `col.new parent>child;green`                             |
| Execution Style  | Multiple steps, panels, and manual actions                                       | One line, instant execution ⚡                           |
| Reusability      | Repeat process for every collection setup                                        | Instant reuse (copy/paste commands)                      |

One command = seconds saved. 😎

---

💡 Pro Tips

 - Color codes work instantly – use them to visually group related collections.
 - You can mix commas for siblings and > for children in the same command.
 - col.add and obj.move are smart – they never fail; they create missing collections automatically.
 - Use obj.move without selecting anything to move specific objects by name.
 - Combine with cube/sphere commands: <br>
    m.c 2 0 0 0 → col.add buildings;red → instant organisation.

---

# Summary

```bash
col.new name1;color, name2>child;color
col.add collection;color
col.sel collection1, collection2
col.hide / col.show collection1, collection2
col source move target
obj.move collection;color
obj obj1, obj2 move collection;color
```

Type once → collections structured, objects organised, scene clean 😎 <br>
No outliner hunting. No repetitive clicking. Just Command Master Pro.

---
